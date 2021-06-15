def transform_dataframe(df):
    df.columns = [x.lower() for x in df.columns]
    return df

