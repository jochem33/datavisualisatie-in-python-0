import matplotlib.pyplot as plt
import pandas as pd

print(".")

dfgames = pd.read_csv("games.csv")
print(".")

kol = ["Name", "Platform", "Global_Sales"]
print(".")
dfgames = dfgames[kol]
print(".")
dfgames = dfgames[dfgames.Platform == "PS4"]
dfgames = dfgames.head(20)
print(".")
dfgames.plot(kind="barh", x="Name", y="Global_Sales")
print(".")


plt.show()
print("klaar")
