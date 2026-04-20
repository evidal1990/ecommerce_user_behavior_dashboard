from src.utils.dataframe import (
    convert_to_dataframe,
    validate_kpi,
    sort_dataframe,
)


def process_kpi(data):
    df = convert_to_dataframe(data)
    validate_kpi(df)
    df = sort_dataframe(df)
    return df
