import pandas as pd
'''
myData={
    'cars': ["BMW", "Volvo", "Ford", "Tata", "Audi"],
    'Passings':[3, 7, 2, 5, 9]
}
myVar=pd.DataFrame(myData)
print(myVar)

# this is for checking the version
a = [1, 7, 2, 9, 3, 6, 12]
myVar=pd.Series(a)
print(myVar)
print(myVar[0])

# This is for creating label
b=[1, 7, 2]
myVar= pd.Series(b, index=["x", "y", "z"])
print(myVar)

# key/value objects as series
calories={"day1": 420, "day2": 380, "day3": 390}
myVar=pd.Series(calories)
print(myVar)

# for selecting only one
calories={"day1": 420, "day2": 380, "day3": 390}
myVar=pd.Series(calories, index=["day1", "day2", "day3"])
print(myVar)

# This example returns a pandas series.
myData={
    'cars': ["BMW", "Volvo", "Ford", "Tata", "Audi"],
    'Passings':[3, 7, 2, 5, 9]
}
myVar=pd.DataFrame(myData)
print(myVar)
print(myVar.loc[[0, 1]]) # Note: When using [], the result is a pandas DataFrame

# 
data={
    "calories": [420, 380, 360, 123, 450],
    "duration": [12, 34, 23, 152, 30]
}
df=pd.DataFrame(data, index=["day1", "day2", "day3", "day4", "day5"])
print(df)
print(df.loc["day2"])

# Without using to_string Pandas will return only the first 5 rows and the last 5 rows
df=pd.read_csv('data.csv')
print(df)

# this will return entire data
df=pd.read_csv('data.csv')
print(df.to_string()) # use to_string() to print the entire DataFrame

# this is for setting the max_rows.
pd.options.display.max_rows = 9999
df=pd.read_csv('data.csv')
print(df)

# Reading JSON
df=pd.read_json('data.json')
print(df.to_string())

# this is for creating json
data={
    "Duration": {
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "4":67,
        "5":34,
    },
    "Pulse": {
        "0":110,
        "1":117,
        "2":104,
        "3":203,
        "4":102,
        "5":101,
    },
    "MaxPulse": {
        "0":130,
        "1":145,
        "2":135,
        "3":189,
        "4":117,
        "5":103,
    },
    "Calories": {
        "0":409,
        "1":479,
        "2":340,
        "3":286,
        "4":400,
        "5":300,
    }
}
df = pd.DataFrame(data)
print(df)

df=pd.read_csv('data.csv')
# print(df.head()) # If the number of rows is not specified, the head() method will returns the top 5 rows.
# print(df.tail(10))

# for printing the information about the data.
print(df.info())

# cleaning empty cells
df = pd.read_csv('data.csv')
new_df = df.dropna() # by default, the dropna() method returns a new DataFrame, and will not change the original.
print(new_df.to_string())

# If you want to change the original DataFrame, use the inplace=True

df = pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df.to_string())
'''

df = pd.read_csv('data.csv')
print(df.fillna(1, inplace=True))