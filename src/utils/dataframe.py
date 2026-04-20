import polars as pl
from typing import Any


def convert_to_dataframe(data: list[dict[str, Any]]) -> pl.DataFrame:
    return pl.DataFrame(data)


def sort_dataframe(
    df: pl.DataFrame,
    column: str = "value",
) -> pl.DataFrame:
    return df.sort(by=column, descending=True)


def top_n_dataframe(
    df: pl.DataFrame,
    n: int = 5,
) -> pl.DataFrame:
    return df.head(n)


def format_labels(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.concat_str(
            [
                pl.col("dimension"),
                pl.lit(" ("),
                pl.col("value").cast(pl.Utf8),
                pl.lit(")"),
            ]
        ).alias("label")
    )


def calculate_percentage(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        (pl.col("value") / pl.col("value").sum() * 100).alias("percentage")
    )
