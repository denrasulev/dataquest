import sqlite3
import pandas as pd

# import data
academy_awards = pd.read_csv('data/academy_awards.csv', encoding = 'ISO-8859-1')
academy_awards.head(6)

# print values counts and values per column of dataframe
for i in range(5,11):
    x = ' '.join(["Unnamed:", str(i)])
    p = academy_awards[x].value_counts()
    df2 = pd.DataFrame({'value':p.index, 'count':p.values})
    print (x, '\n', df2.to_string(index=False), '\n')

# leave only four letters in year column and convert them to int64
academy_awards['Year'] = academy_awards['Year'].str[0:4]
academy_awards['Year'] = academy_awards['Year'].astype(int)
academy_awards['Year'].dtypes

# take only those after year 2000
later_than_2000 = academy_awards[academy_awards['Year'] > 2000]
later_than_2000.head()
later_than_2000.shape

awards_categories = ['Actor -- Leading Role', 'Actor -- Supporting Role', 'Actress -- Leading Role', 'Actress -- Supporting Role']
nominations = later_than_2000[later_than_2000['Category'].isin(awards_categories)]
nominations.head()

#nominations.replace({'Won?': {'NO': 0, 'YES': 1}}, inplace=True)
pd.options.mode.chained_assignment = None
replace_dict = { 'NO': 0, 'YES': 1 }
nominations['Won?'] = nominations['Won?'].map(replace_dict)
nominations.head()

nominations.rename(columns={'Won?': 'Won'}, inplace=True)
nominations.head()

final_nominations = nominations.drop(['Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1)
final_nominations.head()

additional_info_one = final_nominations['Additional Info'].str.rstrip("'}")
additional_info_one.head()

additional_info_two = additional_info_one.str.split(" {'")
additional_info_two.head()

movie_names = additional_info_two.str[0]
movie_names.head()

characters = additional_info_two.str[1]
characters.head()

final_nominations['Movie'] = movie_names
final_nominations['Character'] = characters
final_nominations.head()

final_nominations.drop(['Additional Info'], axis=1, inplace=True)
final_nominations.head()

final_nominations.dtypes

conn = sqlite3.connect('nominations.db')
final_nominations.to_sql('nominations', conn, index=False)

conn.execute('pragma table_info(nominations);').fetchall()
