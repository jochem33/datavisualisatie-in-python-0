import pandas as pd
sNum = pd.Series([6,7,8,4,5.5,6.5,7,2,5,4,3,8,9,9.8,9.7,9.4,2,5,7,8,6.2,5.7,8,9])
print ("hij heeft ", sNum.count(), "cijfers gehaald")
print ("het gemiddlede is", sNum.mean())
print ("het laagste cijfer is: ", sNum.min())
