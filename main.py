import pandas as pd

print('blackx6looklikeapanda')

def fill_and_group_missing_dates(df, column_to_fill_name, main_group_column_name='id', day_column_name='day'):
  dates = pd.date_range(df[day_column_name].min(), df[day_column_name].max(), freq='D')
  id_dfs = {}
  for name, group in df.groupby([main_group_column_name, day_column_name], as_index=False).sum().groupby(main_group_column_name):
    id_dfs[name] = pd.Series(group[column_to_fill_name].values, index=pd.to_datetime(group[day_column_name])).reindex(dates, fill_value=0)
  return id_dfs

def fill_missing_dates(df, column_to_fill_name, day_column_name='day'):
  dates = pd.date_range(df[day_column_name].min(), df[day_column_name].max(), freq='D')
  return pd.Series(df[column_to_fill_name].values, index=pd.to_datetime(df[day_column_name])).reindex(dates, fill_value=0)
