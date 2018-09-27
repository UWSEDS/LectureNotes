def table_counter(df_arg, groupby_column):
    df_count = df_arg.groupby(groupby_column).count()
    column_name = df_arg.columns[0]
    df_count1 = df_count[[column_name]]
    df_count2 = df_count1.rename(columns={column_name: 'count'})
    return df_count2
