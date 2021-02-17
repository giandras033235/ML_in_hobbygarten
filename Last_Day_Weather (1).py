import csv
import codecs
import urllib.request
import sys
import pandas as pd
from pandas import read_csv
from datetime import date
from datetime import timedelta
import time
def fahrenheit_to_celsius(tempinF):
    tempinC = round((tempinF -32)*(5/9),2)
    return tempinC
def inches_to_cm(inch):
    mm = round(inch * 25.4,2)
    return mm

# This is the core of our weather query URL
BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/'
print("asd")
yesterday = date.today() - timedelta(days=1)
today = date.today()
Time_Is_Now = time.localtime()
print(Time_Is_Now)
print(Time_Is_Now.tm_hour)

if (Time_Is_Now.tm_hour == 5):
    print("Morning shower")
    Date_Interval_lower= (str(yesterday))
    Date_Interval_upper= (str(yesterday))
else:
    print('Evening shower')
    Date_Interval_lower= (str(today))
    Date_Interval_upper= (str(today))
    print(Date_Interval_lower)
print('')
Location = "Miskolc, BZ, HU"
Form = 'HISTORY'
Api_Key = 'G0F4LUQZXYYFH0I8MTDB7XNHY'
#Date_Interval_lower= (str(yesterday))
#Date_Interval_upper= (str(yesterday))
print(Date_Interval_lower)
print(Date_Interval_upper)
print(' - Requesting weather for: ',Location )

# Set up the location parameter for our query
QueryLocation = '&location=' + urllib.parse.quote(Location)

# Set up the query type parameter for our query ('FORECAST' or 'HISTORY')
QueryType=Form.upper()

# Set up the key parameter for our query
QueryKey = '&key=' + Api_Key

# Set up the date parameters for our query. Used only for historical weather data requests
#if len(sys.argv) >4:
FromDateParam = Date_Interval_lower
ToDateParam = Date_Interval_upper





# Set up the specific parameters based on the type of query
if QueryType == 'FORECAST':
    print(' - Fetching forecast data')
    QueryTypeParams = 'forecast?&aggregateHours=24&unitGroup=us&shortColumnNames=false'
else:
    print(' - Fetching history for date: ', FromDateParam,'-',ToDateParam)

    # History requests require a date.  We use the same date for start and end since we only want to query a single date in this example
    QueryDate = '&startDateTime=' + FromDateParam + 'T00:00:00&endDateTime=' +ToDateParam + 'T00:00:00'
    QueryTypeParams = 'history?&aggregateHours=24&unitGroup=us&dayStartTime=0:0:00&dayEndTime=0:0:00' + QueryDate


# Build the entire query
URL = BaseURL + QueryTypeParams + QueryLocation + QueryKey

print(' - Running query URL: ', URL)
print()

# Parse the results as CSV
CSVBytes = urllib.request.urlopen(URL)
CSVText = csv.reader(codecs.iterdecode(CSVBytes, 'utf-8'))



filename = 'Last_Day_Data.csv'
with open(filename, 'w') as csvfile:  
                # creating a csv writer object  
    csvwriter = csv.writer(csvfile)

    RowIndex = 0

# The first row contain the headers and the additional rows each contain the weather metrics for a single day
# To simply our code, we use the knowledge that column 0 contains the location and column 1 contains the date.  The data starts at column 4
    for Row in CSVText:
        if RowIndex == 0:
            FirstRow = Row
        else:
            print('Weather in ', Row[0], ' on ', Row[1])

            ColIndex = 0
            for Col in Row:
              
                if ColIndex >= 4:
                
                    print('   ', FirstRow[ColIndex], ' = ', Row[ColIndex])
                    #csvwriter.writerow(Row)
                    
                ColIndex += 1
            csvwriter.writerow(FirstRow)
            csvwriter.writerow(Row)
        
        RowIndex += 1

# If there are no CSV rows then something fundamental went wrong
    if RowIndex == 0:
        print('Sorry, but it appears that there was an error connecting to the weather server.')
        print('Please check your network connection and try again..')

# If there is only one CSV  row then we likely got an error from the server
    if RowIndex == 1:
        print('Sorry, but it appears that there was an error retrieving the weather data.')
        print('Error: ', FirstRow)

input_file = 'Last_Day_Data.csv'
output_file = 'Last_Day_Data_Clear.csv'
cols_to_remove = [0,1,2,3,5,7,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24] # Column indexes to be removed (starts at 0)

cols_to_remove = sorted(cols_to_remove, reverse=True) # Reverse so we remove from the end first
row_count = 0 # Current amount of rows processed

with open(input_file, "r") as source:
    reader = csv.reader(source)
    with open(output_file, "w", newline='') as result:
        writer = csv.writer(result) 
        for row in reader:
            row_count += 1
            print('\r{0}'.format(row_count), end='') # Print rows processed
            for col_index in cols_to_remove:
                del row[col_index]
            
            writer.writerow(row)



print()
