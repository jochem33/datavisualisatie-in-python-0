import pandas as pd
dfGames = pd.read_csv("games.csv")
kolommen = ["Name", "EU_Sales"]

dfGamesKlein = dfGames[kolommen]
dfGamesKleinSorted = dfGamesKlein.sort("EU_Sales")
dfGamesKleinSorted = dfGamesKleinSorted[dfGamesKleinSorted.sort == "PS4"]
print (dfGamesKleinSorted.head(10))
