import pandas as pd

# Read CSV files
stateData = pd.read_csv("Data/stateTouristCount.csv")
monumentData = pd.read_csv("Data/monumentData.csv")
stateOfCity = pd.read_csv("Data/stateOfCity.csv")

# Select and rename columns in stateData
stateData = stateData.drop(columns=['DTV', 'FTV'])
stateData = stateData.rename(columns={
    'States.UTs': 'States',
    'Domestic': 'domesticVT',
    'Foreign': 'foreignVT',
    'Rank.DTV': 'rankDomestic',
    'Rank.FTV': 'rankForeign'
})

# Arrange stateData by rankDomestic
stateData = stateData.sort_values(by='rankDomestic')

# Group and summarize stateOfCity
stateOfCity = stateOfCity.groupby('State').size().reset_index(name='cityCount')

# Select monumentName from monumentData
# Check if 'monumentName' column exists, if not, use 'Monument Name'
if 'monumentName' in monumentData.columns:
    monument_name = monumentData[['monumentName']]
elif 'Monument Name' in monumentData.columns:
    monument_name = monumentData[['Monument Name']]
else:
    print("Error: 'monumentName' or 'Monument Name' column not found in monumentData")
    monument_name = pd.DataFrame()  # Create an empty DataFrame

# Print the results for verification
print("State Data:")
print(stateData.head())
print("\nState of City:")
print(stateOfCity.head())
print("\nMonument Name:")
print(monument_name.head())
