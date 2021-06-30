import pandas as pd
import requests
import os

def create_df_api_standard(url, key, item, name):
    '''
    Only for single page.
    prior to running this function need to know url and keys so as to specifiy which field within the data you 
    wish to create a DF on.
    '''
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data[key][item])
    df.to_csv(name + '.csv')
    
    return df


    def csv_to_dataframe(url, page_name, key1, key2= None, key3= None):
    ''' 
    Takes in a csv and return that dataframe.
    csv_to_dataframe(
    url: csv url,
    key1: key from dataframe,
    key2= None
    )
    '''
    items_list = []
    
    # Let's take an example url and make a get request
    response = requests.get(url)
    #create dictionary object
    data= response.json()
    
    n = data[key1][key2]
    
    if (key2 != None) & (key3 != None):
        #Adding 1 here so the last digit is not cut off (not inclusive)
        for i in range(1,n+1):
            url = f'https://python.zach.lol/api/v1/{page_name}?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_items = data[key1][key3]
            items_list += page_items
    else:
        for i in range(1,n+1):
            url = f'https://python.zach.lol/api/v1/{page_name}?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_items = data[key1]
            items_list += page_items
    
    df= pd.DataFrame(items_list)
    return df


    def germany_power():
    '''
    This function reads in the germany dataset and returns it as a pandas DataFrame.
    '''

    gp = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    return gp



    def get_data(csv, url, page_name, key1, key2= None, key3= None, cached=False):
    '''
    This function reads in items df and writes data to
    a csv file if cached == False or if cached == True reads in sales df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile(csv) == False:
        
        #Read fresh data from db into a DataFrame.
        df= csv_to_dataframe(url, page_name, key1, key2, key3)
        
        # Write DataFrame to a csv file.
        df.to_csv(csv)
        
    else:
        
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv(csv, index_col=0)
        
    return df




#### alternate this function to specify 
def new_items_page_range(alpha=1, omega=0):
    '''
    This function is specific to Zach's lol grocery dataset. It will itirate through each
    page of items and return a pandas DataFrame of all items in the page range. The arguement alpha is used as 
    a starting page, and defaults to 1. Omega is used as an ending page, and defaults to zero.
    This allows for a return of a range of pages.
    '''
    items_list = []
    base_url = 'https://python.zach.lol/api/v1'
    response = requests.get(base_url + '/items')
    data = response.json()
    n = data['payload']['max_page']
    
    if omega == 0:
        
        for i in range(alpha, n+1):
            url = 'https://python.zach.lol/api/v1/items?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_items = data['payload']['items']
            items_list += page_items
            
    else:
        
        for i in range(alpha, omega+1):
            url = 'https://python.zach.lol/api/v1/items?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_items = data['payload']['items']
            items_list += page_items
        
    return pd.DataFrame(items_list)