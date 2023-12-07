#imports
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import regex as re

#get a list of links to all ferraris
#pattern is the first_record number changes because I sorted by 100 listings per page
first_record = [100, 200, 300, 400, 500, 600, 700, 800, 900] #autotrader gets weird after 1k results, so ill sort by ascending price 1k and descending price 1k

#looping to get 1800 results
#for loop in action:
all_pages_to_scrape = []
total_links = []

for i in first_record:
    general_page_link_asc = 'https://www.autotrader.com/cars-for-sale/all-cars/ferrari/santa-ana-ca?firstRecord=' + str(i) + '&isNewSearch=false&numRecords=100&searchRadius=0&sortBy=derivedpriceASC&zip=92701'
    general_page_link_desc = 'https://www.autotrader.com/cars-for-sale/all-cars/ferrari/santa-ana-ca?firstRecord=' + str(i) + '&isNewSearch=false&numRecords=100&searchRadius=0&sortBy=derivedpriceDESC&zip=92701'
    
    all_pages_to_scrape.append(general_page_link_asc)
    all_pages_to_scrape.append(general_page_link_desc)

for url_100 in all_pages_to_scrape:
    #getting individual car urls from a page list of 100
    
    url = url_100

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = bs(response.text, 'html.parser')

        # Find all the links on the page
        links = soup.find_all('a', href=True)

        # Print the links
        for link in links:
            try:
                if link['href'].startswith('/cars-for-sale/vehicle'):
                    total_links.append(link['href'])

            except:
                print(link['href'])
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)



#turning the 'a' tag data into useable links by adding a base to them, also using SET to ensure no duplicates
base = 'https://autotrader.com'
individual_cars = []
for item in set(total_links):
    completed_link = base + item
    individual_cars.append(completed_link)

#storing car data in a list
car_dict_list = []
for i in range(0,2207):
    #getting car info from scraping individual page put together and putting into a dict
    try:
        url = individual_cars[i]

        response = requests.get(url)
        soup = bs(response.text, 'html.parser')

        #this gets the title which is like "New Ferrari 458 Italia" etc
        car_name = soup.find('h1').text  

        #a list to pull out all nice easy car attributes
        car_info = []

        #this gets the list of common traits from the cars (mileage, engine, mpg, ext color, int color, transmission, rwd/awd/fwd)
        index = 0
        for item in soup.find_all(class_='list-bordered list-condensed'):
            car_attribute = item.find(class_='display-flex col-xs-10 margin-bottom-0').text
            car_info.append(car_attribute)
            #print(car_attribute + '\n')

        #this gets the price
        price = soup.find(class_='first-price').text

        #all vars I need
        car_name = car_name
        #new
        condition = car_name.split()[0]
        #new
        year = car_name.split()[1]
        price = price
        mileage = car_info[0].split()[0]
        engine = car_info[1]
        mpg = car_info[2]
        ext_color = car_info[3]
        int_color = car_info[4]
        transmission = car_info[5]
        rwd = 'yes'
        if "FF" in car_name:
            rwd = 'no'
        if "SF90" in car_name:
            rwd = 'no'
        #appending the cars info to the list
        car_dict_list.append({'name': car_name, 'price': price, 'mileage': mileage, 'engine': engine, 'mpg': mpg, 'ext_color': ext_color, 'int_color': int_color, 'transmission': transmission,
                                'rwd': rwd, 'condition': condition, 'year': year})
    except:
        print('there was an error on this car')

#use the list of dictionaries to create a df
car_df = pd.DataFrame(car_dict_list)

#data cleaning
#it seems like a few rows of the table didnt get scraped correctly for some reason
#checking a column to see the weird values that need to be fixed
print(car_df['transmission'].unique())

#creating a copy of the df in case something messes up I dont need to rescrape
cleaned_df = car_df

#removing weird values from transmission
cleaned_df = cleaned_df.loc[(cleaned_df['transmission'] == '7-Speed Automatic Transmission') | (cleaned_df['transmission'] == '6-Speed Automatic Transmission')
                            | (cleaned_df['transmission'] == '8-Speed Automatic Transmission') | (cleaned_df['transmission'] == 'Automatic Transmission') 
                            | (cleaned_df['transmission'] == '6-Speed Manual Transmission') | (cleaned_df['transmission'] == 'Manual Transmission')
                            | (cleaned_df['transmission'] =='7-Speed Shiftable Automatic Transmission') | (cleaned_df['transmission'] =='6-Speed Shiftable Automatic Transmission')]

#verifying that weird values have been removed
print(cleaned_df['transmission'].unique())

#cleaning the transmission table errors eliminated 145 structure errors
car_df.shape
cleaned_df.shape

#taking the condition out of the car name
cleaned_df['name'] = cleaned_df['name'].replace('Used ', '', regex=True)
cleaned_df['name'] = cleaned_df['name'].replace('Certified ', '', regex=True)
cleaned_df['name'] = cleaned_df['name'].replace('New ', '', regex=True)

#checking year values to remove from name
cleaned_df['year'].unique()

#taking the year out of the cars name
for year in cleaned_df['year'].unique():
    cleaned_df['name'] = cleaned_df['name'].replace(year, '', regex=True)

#taking the word "Ferrari" out of name because they are all ferraris
cleaned_df['name'] = cleaned_df['name'].replace('Ferrari', '', regex=True)

#removing commas from price and mileage so they can be numeric values
cleaned_df['price'] = cleaned_df['price'].replace(',', '', regex=True)
cleaned_df['mileage'] = cleaned_df['mileage'].replace(',', '', regex=True)

cleaned_df[['price', 'mileage']] = cleaned_df[['price', 'mileage']].apply(pd.to_numeric)

#expanding the engine column to accomodate num of cylinders and size
cleaned_df[['engine_size', 'engine_info']] = cleaned_df['engine'].str.split(' ', 1, expand=True)

print(cleaned_df['engine_size'].unique())

#removing the 'L' from engine size
cleaned_df['engine_size'] = cleaned_df['engine_size'].replace('L', '', regex=True)

#filter out some weird remaining values from engine size so it can be a numeric variable
cleaned_df = cleaned_df.loc[(cleaned_df['engine_size'] == '3.9') | (cleaned_df['engine_size'] == '6.3') | (cleaned_df['engine_size'] == '6.5') | (cleaned_df['engine_size'] == '3.6')
                            | (cleaned_df['engine_size'] == '4.3') | (cleaned_df['engine_size'] == '4.5') | (cleaned_df['engine_size'] == '5.7') | (cleaned_df['engine_size'] == '6.0')
                            | (cleaned_df['engine_size'] == '2.0')]

#making a numeric veriable
cleaned_df['engine_size'] = cleaned_df['engine_size'].apply(pd.to_numeric)

#dropping the engine column because i split it to engine size and engine info
cleaned_df.drop(columns=['engine'], inplace=True)

#looking at mpg column
print(cleaned_df['mpg'].unique())

# i think mpg shold be a numeric column not a categorical column in current format, assigning some averages to better suit the column description
#using regex to replace each value with the avg
cleaned_df['mpg'] = cleaned_df['mpg'].replace('16 City / 23 Highway ', '19.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('16 City / 22 Highway ', '19', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('15 City / 22 Highway ', '18.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('12 City / 16 Highway ', '14', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('10 City / 15 Highway ', '12.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('14 City / 19 Highway ', '16.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('12 City / 18 Highway ', '15', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('12 City / 15 Highway ', '13.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('17 City / 22 Highway ', '19.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('13 City / 17 Highway ', '15', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('15 City / 18 Highway ', '16.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('15 City / 19 Highway ', '17', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('13 City / 19 Highway ', '16', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('9 City / 16 Highway ', '12.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('15 City / 20 Highway ', '17.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('11 City / 16 Highway ', '13.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('12 City / 17 Highway ', '14.5', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('11 City / 15 Highway ', '13', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('11 City / 17 Highway ', '14', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('15 City / 21 Highway ', '18', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('10 City / 16 Highway ', '13', regex=True)
cleaned_df['mpg'] = cleaned_df['mpg'].replace('9 City / 15 Highway ', '12', regex=True)

#changing mpg after the cleaning to a numeric datatype
cleaned_df['mpg'] = cleaned_df['mpg'].apply(pd.to_numeric)

#changing year to a numeric datatype
cleaned_df['year'] = cleaned_df['year'].apply(pd.to_numeric)

#checking dtypes of the df
print(cleaned_df.dtypes)

#writing pre-cleaned data to csv (car_df)
car_df.to_csv('precleaned_data_python_script.csv',index=False)

#writing cleaned data to csv (cleaned_df)
cleaned_df.to_csv('clean_data_python_script.csv', index=False)




