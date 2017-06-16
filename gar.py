import pandas as pd
data = pd.read_csv(r'tutorial/tutorial/spiders/datasucc.csv', encoding="ISO-8859-1")

print(data.shape)
##
##
string = "https://www.startnext.com/einguterplan"
str = string.split("/")[-1]
str = string.replace("/", " ")
print(str.strip())
