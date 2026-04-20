from typing import Any

import polars as pl
from polars.datatypes.classes import NumericType


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


def validate_kpi(df: pl.DataFrame) -> None:
    if df.height == 0:
        raise ValueError("Empty dataframe")

    if df.select(pl.col("value").is_null().any()).item():
        raise ValueError("Null values found")

    if not isinstance(df.schema["value"], NumericType):
        raise ValueError("Column 'value' must be numeric")

    if df.select((pl.col("value") < 0).any()).item():
        raise ValueError("Negative values found")

    if df.select(pl.col("value").sum()).item() == 0:
        raise ValueError("Sum of values is zero")
