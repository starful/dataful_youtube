import sys
import sqlite3
import pandas as pd
import bar_chart_race as bcr

file_sqlite3 = "info.db"
conn = sqlite3.connect(file_sqlite3)

df = pd.read_csv('../data/data2.csv')
# df = pd.read_sql_query("SELECT * FROM year_age_at_marriage_women", conn)

df = df.pivot_table(index='year',
    columns='location',
    values='deathsTetanusRate')

# df = df.query('year > 2000')

bcr.bar_chart_race(df=df,
        filename='video/deathsTetanusRate.mp4',
        filter_column_colors=True,
        steps_per_period=40,
        period_length=500,
        n_bars=15,
        sort='desc'
        )
