import pandas as pd
df = pd.read_html("https://en.wikipedia.org/wiki/List_of_highest-grossing_films")
print(df[1])

df[1].to_excel("movies.xlsx")