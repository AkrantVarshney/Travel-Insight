# raw data    -  process data
# app -- data

import pandas as pd
import os
import inspect
from calendar import month_name

def processReviews(data, outputFileName='processed_reviews.csv'):
    processedData = (data
        .sort_values(by='published_at_date')
        .assign(published_at_date=lambda x: pd.to_datetime(x['published_at_date']))
        .assign(month=lambda x: x['published_at_date'].dt.strftime('%B'))
        .groupby('month')
        .size()
        .reset_index(name='reviewCount')
    )
    
    # Create a DataFrame with all months
    allMonths = pd.DataFrame({'month': list(month_name)[1:]})  # Excludes the empty string at index 0
    
    # Merge all months with the processed data
    processedData = allMonths.merge(processedData, on='month', how='left').fillna(0)
    processedData['reviewCount'] = processedData['reviewCount'].astype(int)
    
    # Sort the DataFrame by month order
    monthOrder = {month: index for index, month in enumerate(month_name[1:])}
    processedData['monthOrder'] = processedData['month'].map(monthOrder)
    processedData = processedData.sort_values('monthOrder').drop('monthOrder', axis=1)   
    # Define seasons
    seasons = {
        "January": "Winter", "February": "Spring", "March": "Spring",
        "April": "Spring", "May": "Summer", "June": "Summer",
        "July": "Summer", "August": "Monsoon", "September": "Monsoon",
        "October": "Monsoon", "November": "Winter", "December": "Winter"
    } 
    # Add season information
    processedData['season'] = processedData['month'].map(seasons)
    
    # Create the "testData" folder if it doesn't exist
    if not os.path.exists('Data/processedData'):
        os.makedirs('Data/processedData')
    
    # Determine the output filename
    if outputFileName is None:
        frame = inspect.currentframe().f_back
        calling_var = [var for var, val in frame.f_locals.items() if val is data][0]
        outputFileName = f"{calling_var}.csv"
    else:
        outputFileName = os.path.basename(outputFileName)
        
    # Save the processed data to a CSV file in the "testData" folder
    outputPath = os.path.join('Data/processedData', outputFileName)
    processedData.to_csv(outputPath, index=False)
    
    print(f"CSV file saved as: {outputPath}")
    
    return processedData


#Agra
# Taj Mahal Data
# Read CSV files
reviewsTajMahal1 = pd.read_csv("Data/tajMahal.csv")
reviewsTajMahal2 = pd.read_csv("Data/tajMahalHighestRev.csv")
reviewsTajMahal3 = pd.read_csv("Data/tajMahalLowestRev.csv")
reviewsTajMahal4 = pd.read_csv("Data/tajMahalMostRelevant.csv")

# Remove 'total_number_of_reviews_by_reviewer' column from each DataFrame
reviewsTajMahal1 = reviewsTajMahal1.drop(columns=['total_number_of_reviews_by_reviewer'])
reviewsTajMahal2 = reviewsTajMahal2.drop(columns=['total_number_of_reviews_by_reviewer'])
reviewsTajMahal3 = reviewsTajMahal3.drop(columns=['total_number_of_reviews_by_reviewer'])
reviewsTajMahal4 = reviewsTajMahal4.drop(columns=['total_number_of_reviews_by_reviewer'])

# Combine all DataFrames
reviewsTajMahal = pd.concat([reviewsTajMahal1, reviewsTajMahal2, reviewsTajMahal3, reviewsTajMahal4], ignore_index=True)
reviewsTajMahal = reviewsTajMahal.drop_duplicates(subset='review_id', keep='first')

#Processing the Data
tajMahalBestMonth=processReviews(reviewsTajMahal, "tajMahal.csv")
print(tajMahalBestMonth)

#Dal Lake Jammu and Kashmir
dalLake=pd.read_csv("Data/dalLake1.csv")
dalLake=processReviews(dalLake, "dalLake.csv")
print(dalLake)

#Chilika lake Odisha
chilikaLake=pd.read_csv("Data/chilikaLake.csv")
chilikaLake=processReviews(chilikaLake, "chilikaLake.csv")
print(chilikaLake)

#Somnath Temple gujarat
somnathTemple=pd.read_csv("Data/somnathTemple.csv")
somnathTemple=processReviews(somnathTemple, "somnathTemple.csv")
print(somnathTemple)

# GOA Data
goa=pd.read_csv("Data/goa.csv")
goa = processReviews(goa, "goa.csv")
print(goa)

# Andaman and Nicobar Islands

cellularJail=pd.read_csv("Data/cellularJail.csv")
cellularJail=processReviews(cellularJail, "cellularJail.csv")
print(cellularJail)

# Madhya Pradesh

madhyaPradesh=pd.read_csv("Data/madhyaPradesh.csv")
cellularJail=processReviews(madhyaPradesh, "madhyaPradesh.csv")
print(cellularJail)

# Sikkim 

sikkim=pd.read_csv("Data/sikkim.csv")
cellularJail=processReviews(sikkim, "sikkim.csv")
print(sikkim)

# Haryana

haryana=pd.read_csv("Data/haryana.csv")
cellularJail=processReviews(haryana, "haryana.csv")
print(haryana)

# West bengal

westBengal=pd.read_csv("Data/westBengal.csv")
westBengal=processReviews(westBengal, "westBengal.csv")
print(westBengal)

# Meghlaya 

meghlaya=pd.read_csv("Data/meghlaya.csv")
meghlaya=processReviews(meghlaya, "meghlaya.csv")
print(meghlaya)

# Tamil Nadu

tamilNadu=pd.read_csv("Data/tamilNadu.csv")
tamilNadu=processReviews(tamilNadu, "tamilNadu.csv")
print(tamilNadu)

# Kerala

kerala=pd.read_csv("Data/kerala.csv")
kerala=processReviews(kerala, "kerala.csv")
print(kerala)

# Assam

assam=pd.read_csv("Data/assam.csv")
assam=processReviews(assam, "assam.csv")
print(assam)

# Karnatka

karnataka=pd.read_csv("Data/karnataka.csv")
karnataka=processReviews(karnataka, "karnataka.csv")
print(karnataka)

# Himachal Pradesh

himachalPradesh=pd.read_csv("Data/himachalPradesh.csv")
himachalPradesh=processReviews(himachalPradesh, "himachalPradesh.csv")
print(himachalPradesh)

# Rajashtan

rajasthan=pd.read_csv("Data/rajasthan.csv")
rajasthan=processReviews(rajasthan, "rajasthan.csv")
print(rajasthan)

# Maharashtra

maharashtra=pd.read_csv("Data/maharashtra.csv")
maharashtra=processReviews(maharashtra, "maharashtra.csv")
print(maharashtra)

# Punjab

punjab=pd.read_csv("Data/punjab.csv")
punjab=processReviews(punjab, "punjab.csv")
print(punjab)

# Uttrakhand

uttarakhand=pd.read_csv("Data/uttarakhand.csv")
uttarakhand=processReviews(uttarakhand, "uttarakhand.csv")
print(uttarakhand)

# Chhattisgarh

chattisgarh=pd.read_csv("Data/chattisgarh.csv")
chattisgarh=processReviews(chattisgarh, "chattisgarh.csv")
print(chattisgarh)

# Bihar

bihar=pd.read_csv("Data/bihar.csv")
bihar=processReviews(bihar, "bihar.csv")
print(bihar)

# Jharkhand

jharkhand=pd.read_csv("Data/jharkhand.csv")
jharkhand=processReviews(jharkhand, "jharkhand.csv")
print(jharkhand)

# Andhra Pradesh

andhraPradesh=pd.read_csv("Data/andhraPradesh.csv")
andhraPradesh=processReviews(andhraPradesh, "andhraPradesh.csv")
print(andhraPradesh)
