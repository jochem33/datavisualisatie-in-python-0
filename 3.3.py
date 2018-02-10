import pandas as pd

dfGames = pd.read_csv("games.csv")
kolommen = ["Name", "EU_Sales"]


dfGamesKlein = dfGames[kolommen]
print (dfGamesKlein.head(15))
