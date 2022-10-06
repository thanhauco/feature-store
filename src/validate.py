import great_expectations as ge
def validate(df):
    ge_df = ge.from_pandas(df)
    return ge_df.expect_column_values_to_not_be_null('id')