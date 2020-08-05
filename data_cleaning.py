import pandas as pd
import numpy as np 
import csv
import os 

# MASS DATA
def massFunc():
  for filename in (os.listdir('/Users/danielschwartz/Desktop/simplefuture/State_Data/MA')):
    print(filename)
    df = pd.read_csv(f"/Users/danielschwartz/Desktop/simplefuture/State_Data/MA/{filename}", encoding = "ISO-8859-1", low_memory=False)
    df.rename(columns = {'Property Type Code':'property_type', 
                        'Reported Shares':'shares_reported', 
                        'Property ID':'property_id', 
                        'last_name':'owner_lastname', 
                        # 'first_name':'OWNER_FIRSTNAME', 
                        'address_line1':'owner_street_1', 
                        'address_line2':'owner_street_2', 
                        'city':'owner_city', 
                        'state':'owner_state', 
                        'zipcode':'owner_zip', 
                        'Holder Name':'holder_name', 
                        'Property Received Date':'date_reported', 
                        'Reported Cash':'cash_reported'}, 
                        inplace = True)
    
    df[''] = np.nan

    df['reported_tangible_items'] = np.nan
    df['cusip'] = np.nan 
    df['no_of_owners'] = np.nan 
    df['owner_street_3'] = np.nan 
    df['owner_country_code'] = np.nan   
    df['current_cash_balance'] = np.nan   
    df['number_of_pending_claims'] = np.nan   
    df['number_of_paid_claims'] = np.nan   
    df['date_of_last_contact'] = np.nan   
    df['holder_street_1'] = np.nan   
    df['holder_street_2'] = np.nan   
    df['holder_street_3'] = np.nan   
    df['holder_city'] = np.nan   
    df['holder_state'] = np.nan   
    df['holder_zip'] = np.nan

    # df['OWNER_FIRSTNAME'] = df['OWNER_NAME'].str.split().str[1]
    # df['OWNER_LASTNAME'] = df['OWNER_NAME'].str.split().str[0]
    df['owner_middlename'] = df['first_name'].str.split().str[1]
    df['owner_firstname'] = df['first_name'].str.split().str[0]
    df.drop(['first_name'], axis=1, inplace=True, errors='ignore')
    df = df.applymap(lambda s:s.lower() if type(s) == str else s)

    df['owner_firstname'].replace('', np.nan, inplace=True)
    df['owner_lastname'].replace('', np.nan, inplace=True)
    df['owner_city'].replace('', np.nan, inplace=True)
    df.dropna(subset=['owner_firstname'], inplace=True)
    df.dropna(subset=['owner_lastname'], inplace=True)
    df.dropna(subset=['owner_city'], inplace=True)

    df.drop(['Report Year'], axis=1, inplace=True, errors='ignore')
    df.drop(['Unnamed: 0'], axis=1, inplace=True, errors='ignore')
    df.drop(['Reported Tangible Items'], axis=1, inplace=True, errors='ignore')
    df = df[['owner_firstname', 'owner_middlename', 'owner_lastname', 'owner_street_1', 'owner_street_2', 'owner_street_3', 'owner_city', 'owner_state', 'owner_zip', 'no_of_owners', 'owner_country_code', 'current_cash_balance', 'number_of_pending_claims', 'number_of_paid_claims', 'date_of_last_contact', 'holder_name', 'holder_street_1', 'holder_street_2', 'holder_street_3', 'holder_city', 'holder_state', 'holder_zip', 'property_id', 'date_reported', 'property_type', 'cash_reported', 'shares_reported', 'reported_tangible_items', 'cusip']]
    df.drop(df.columns[0], axis=1)
    df.to_csv(f'/Users/danielschwartz/Desktop/Simplefuture/state_data/MA/new_{filename}', index=False)


# CAL DATA
def calFunc():
  for filename in (os.listdir('/Users/danielschwartz/Desktop/simplefuture/State_Data/CA/100_500')):
    print(filename)
    
    df = pd.read_csv(f"/Users/danielschwartz/Desktop/simplefuture/State_Data/CA/100_500/{filename}", encoding = "ISO-8859-1", low_memory=False)    
    # df = df.head(10)
    df[''] = np.nan

    df['reported_tangible_items'] = np.nan

    df['owner_firstname'] = df['OWNER_NAME'].str.split().str[1]
    df['owner_lastname'] = df['OWNER_NAME'].str.split().str[0]
    df['owner_middlename'] = df['OWNER_NAME'].str.split().str[3]
    # df['OWNER_MIDDLENAME'] = df['first_name'].str.split().str[1]
    # df['OWNER_FIRSTNAME'] = df['first_name'].str.split().str[0]
    # df.drop(['first_name'], axis=1, inplace=True, errors='ignore')
    df = df.applymap(lambda s:s.lower() if type(s) == str else s)

    df['owner_firstname'].replace('', np.nan, inplace=True)
    df['owner_lastname'].replace('', np.nan, inplace=True)
    df.rename(columns = {
                        'OWNER_CITY' : 'owner_city', 
                        'OWNER_ZIP' : 'owner_zip',
                        'OWNER_STREET_1' : 'owner_street_1', 
                        'OWNER_STREET_2' : 'owner_street_2', 
                        'OWNER_STREET_3' : 'owner_street_3', 
                        'OWNER_STATE' : 'owner_state',	
                        'NO_OF_OWNERS' : 'no_of_owners',	
                        'OWNER_COUNTRY_CODE' : 'owner_country_code',	
                        'CURRENT_CASH_BALANCE' : 'current_cash_balance',	
                        'NUMBER_OF_PENDING_CLAIMS' : 'number_of_pending_claims',	
                        'NUMBER_OF_PAID_CLAIMS' : 'number_of_paid_claims',	
                        'DATE_OF_LAST_CONTACT' : 'date_of_last_contact', 
                        'HOLDER_NAME' : 'holder_name',	
                        'HOLDER_STREET_1' : 'holder_street_1',	
                        'HOLDER_STREET_2' : 'holder_street_2',	
                        'HOLDER_STREET_3' : 'holder_street_3',	
                        'HOLDER_CITY' : 'holder_city',	
                        'HOLDER_STATE' : 'holder_state',	
                        'HOLDER_ZIP' : 'holder_zip', 
                        'PROPERTY_ID' : 'property_id',	
                        'DATE_REPORTED' : 'date_reported',	
                        'PROPERTY_TYPE' : 'property_type',	
                        'CASH_REPORTED' : 'cash_reported',	
                        'SHARES_REPORTED' : 'shares_reported',	
                        'REPORTED_TANGIBLE_ITEMS' : 'reported_tangible_items',	
                        'CUSIP' : 'cusip'
                        }, 
                        inplace=True)
    df['owner_city'].replace('', np.nan, inplace=True)
    df.dropna(subset=['owner_firstname'], inplace=True)
    df.dropna(subset=['owner_lastname'], inplace=True)
    df.dropna(subset=['owner_city'], inplace=True)

    df['owner_zip'] = df['owner_zip'].str.replace('-', '')

    df = df[['owner_firstname', 'owner_middlename', 'owner_lastname', 'owner_street_1', 'owner_street_2', 'owner_street_3', 'owner_city', 'owner_state', 'owner_zip', 'no_of_owners', 'owner_country_code', 'current_cash_balance', 'number_of_pending_claims', 'number_of_paid_claims', 'date_of_last_contact', 'holder_name', 'holder_street_1', 'holder_street_2', 'holder_street_3', 'holder_city', 'holder_state', 'holder_zip', 'property_id', 'date_reported', 'property_type', 'cash_reported', 'shares_reported', 'reported_tangible_items', 'cusip']]
    df.to_csv(f'/Users/danielschwartz/Desktop/Simplefuture/state_data/CA/100_500/new_{filename}', index=False)


# NY DATA
def nyFunc():
  for filename in (os.listdir('/Users/danielschwartz/Desktop/simplefuture/State_Data/NY')):
    df = pd.read_csv (f'/Users/danielschwartz/Desktop/Simplefuture/State_Data/NY/{filename}', header = None, error_bad_lines=False, delimiter='|')
    df.columns = ['owner_name', 'owner_street_1', 'owner_street_2', 'owner_city', 'owner_state', 'owner_zip', 'holder_name', 'delete', 'property_type', 'no_of_owners', 'property_id', 'cusip', 'date_reported']
    # df.drop(['delete'])
    df['owner_firstname'] = df['owner_name'].str.split().str[1]
    df['owner_lastname'] = df['owner_name'].str.split().str[0]
    df['owner_middlename'] = df['owner_name'].str.split().str[2]
    
    df['owner_firstname'].replace('', np.nan, inplace=True)
    df['owner_lastname'].replace('', np.nan, inplace=True)
    df['owner_city'].replace('', np.nan, inplace=True)
    df.dropna(subset=['owner_firstname'], inplace=True)
    df.dropna(subset=['owner_lastname'], inplace=True)
    df.dropna(subset=['owner_city'], inplace=True)

    df['shares_reported'] = np.nan
    df['cash_reported'] = np.nan
    df['reported_tangible_items'] = np.nan
    df['cusip'] = np.nan 
    df['no_of_owners'] = np.nan 
    df['owner_street_3'] = np.nan 
    df['owner_country_code'] = np.nan   
    df['current_cash_balance'] = np.nan   
    df['number_of_pending_claims'] = np.nan   
    df['number_of_paid_claims'] = np.nan   
    df['date_of_last_contact'] = np.nan   
    df['holder_street_1'] = np.nan   
    df['holder_street_2'] = np.nan   
    df['holder_street_3'] = np.nan   
    df['holder_city'] = np.nan   
    df['holder_state'] = np.nan   
    df['holder_zip'] = np.nan

    df['owner_zip'] = df['owner_zip'].apply(lambda x: x if type(x) == float else np.nan)
    df['owner_zip'] = df['owner_zip'].apply(lambda x: int(x) if x == x else "")

    df = df[['owner_firstname', 'owner_middlename', 'owner_lastname', 'owner_street_1', 'owner_street_2', 'owner_street_3', 'owner_city', 'owner_state', 'owner_zip', 'no_of_owners', 'owner_country_code', 'current_cash_balance', 'number_of_pending_claims', 'number_of_paid_claims', 'date_of_last_contact', 'holder_name', 'holder_street_1', 'holder_street_2', 'holder_street_3', 'holder_city', 'holder_state', 'holder_zip', 'property_id', 'date_reported', 'property_type', 'cash_reported', 'shares_reported', 'reported_tangible_items', 'cusip']]

    df = df.applymap(lambda s:s.lower() if type(s) == str else s)

    filename = filename.split('.')[0]
    df.to_csv (f'/Users/danielschwartz/Desktop/simplefuture/State_Data/NY/new_{filename}.csv', index=None)
    print(filename)
import string
# TX Data
def txFunc():
# for filename in (os.listdir('/Users/danielschwartz/Desktop/simplefuture/State_Data/TX')):
  # with open('/Users/danielschwartz/Desktop/Simplefuture/State_Data/TX/TXcopy.txt', 'r') as copy:
  #   whitespace = string.whitespace.replace(" ", "")
  #   df = pd.read_csv('/Users/danielschwartz/Desktop/Simplefuture/State_Data/TX/TXcopy.txt', header = None, error_bad_lines=False, delimiter=whitespace)
  #   df.to_csv(f'/Users/danielschwartz/Desktop/simplefuture/State_Data/TX/neww.csv', index=None)
  
    # df.columns = ['owner_lastname', 'owner_firstname', 'owner_middle', 'no_of_owners', 'property_id', 'data_reported', 'cash_reported', 'unkown', 'property_type', 'merge_property_type', 'owner_state', 'owner_zip', 'holder_name', 'delete', 'property_type', 'no_of_owners', 'cusip', 'date_reported']
  with open('/Users/danielschwartz/Desktop/Simplefuture/State_Data/TX/txcopy.txt') as infile:
    with open('/Users/danielschwartz/Desktop/Simplefuture/State_Data/TX/neww2.csv', 'w') as outfile:
      for line in infile:
        fields = line.split(" ")
        outfile.write('|'.join(fields))
      df = pd.read_csv('/Users/danielschwartz/Desktop/Simplefuture/State_Data/TX/txcopy.txt', header = None, error_bad_lines=False, delim_whitespace=True)
      df.to_csv(f'/Users/danielschwartz/Desktop/simplefuture/State_Data/TX/neww2.csv', index=None)


  # df['OWNER_FIRSTNAME'] = df['OWNER_NAME'].str.split().str[1]
  # df['OWNER_LASTNAME'] = df['OWNER_NAME'].str.split().str[0]
  # df['OWNER_MIDDLENAME'] = df['OWNER_NAME'].str.split().str[3]
  
  # df['OWNER_FIRSTNAME'].replace('', np.nan, inplace=True)
  # df['OWNER_LASTNAME'].replace('', np.nan, inplace=True)
  # df['OWNER_CITY'].replace('', np.nan, inplace=True)
  # df.dropna(subset=['OWNER_FIRSTNAME'], inplace=True)
  # df.dropna(subset=['OWNER_LASTNAME'], inplace=True)
  # df.dropna(subset=['OWNER_CITY'], inplace=True)

  # df['REPORTED_TANGIBLE_ITEMS'] = np.nan
  # df['CUSIP'] = np.nan
  # df['OWNER_STREET_3'] = np.nan 
  # df['OWNER_COUNTRY_CODE'] = np.nan   
  # df['CURRENT_CASH_BALANCE'] = np.nan   
  # df['NUMBER_OF_PENDING_CLAIMS'] = np.nan   
  # df['NUMBER_OF_PAID_CLAIMS'] = np.nan   
  # df['DATE_OF_LAST_CONTACT'] = np.nan   
  # df['HOLDER_STREET_1'] = np.nan   
  # df['HOLDER_STREET_2'] = np.nan   
  # df['HOLDER_STREET_3'] = np.nan   
  # df['HOLDER_CITY'] = np.nan   
  # df['HOLDER_STATE'] = np.nan   
  # df['HOLDER_ZIP'] = np.nan
  # df['SHARES_REPORTED'] = np.nan
  # df['CASH_REPORTED'] = np.nan

  # df['OWNER_ZIP'] = df['OWNER_ZIP'].apply(lambda x: x if type(x) == float else np.nan)
  # df['OWNER_ZIP'] = df['OWNER_ZIP'].apply(lambda x: int(x) if x == x else "")

  # df = df[['OWNER_FIRSTNAME', 'OWNER_MIDDLENAME', 'OWNER_LASTNAME',	'OWNER_STREET_1', 'OWNER_STREET_2', 'OWNER_STREET_3', 'OWNER_CITY',	'OWNER_STATE',	'OWNER_ZIP',	'NO_OF_OWNERS',	'OWNER_COUNTRY_CODE',	'CURRENT_CASH_BALANCE',	'NUMBER_OF_PENDING_CLAIMS',	'NUMBER_OF_PAID_CLAIMS',	'DATE_OF_LAST_CONTACT', 'HOLDER_NAME',	'HOLDER_STREET_1',	'HOLDER_STREET_2',	'HOLDER_STREET_3',	'HOLDER_CITY',	'HOLDER_STATE',	'HOLDER_ZIP', 'PROPERTY_ID',	'DATE_REPORTED',	'PROPERTY_TYPE',	'CASH_REPORTED',	'SHARES_REPORTED',	'REPORTED_TANGIBLE_ITEMS',	'CUSIP']]

  # df = df.applymap(lambda s:s.lower() if type(s) == str else s)

  # filename = filename.split('.')[0]
    # new.to_csv(f'/Users/danielschwartz/Desktop/simplefuture/State_Data/TX/new_.csv', index=None)
  # print(filename)

def moFunc():
  df = pd.read_csv ('/Users/danielschwartz/Desktop/Simplefuture/State_Data/mo/MOtestt.csv', header = None, error_bad_lines=False)
  
  df.columns = ['property_id', 'OWNER NAME', 'owner_street_1', 'owner_city', 'owner_state', 'owner_zip', 'holder_name', 'cash_reported']
  df['owner_zip'] = df['owner_zip'].str.replace('-', '')
  df['owner_firstname'] = df['OWNER NAME'].str.split().str[1]
  df['owner_lastname'] = df['OWNER NAME'].str.split().str[0]
  df['owner_middlename'] = df['OWNER NAME'].str.split().str[2]
  df['owner_firstname'].replace('', np.nan, inplace=True)
  df['owner_lastname'].replace('', np.nan, inplace=True)
  df['owner_city'].replace('', np.nan, inplace=True)
  df.dropna(subset=['owner_firstname'], inplace=True)
  df.dropna(subset=['owner_lastname'], inplace=True)
  df.dropna(subset=['owner_city'], inplace=True)
  df['reported_tangible_items'] = np.nan
  df['no_of_owners'] = np.nan
  df['cusip'] = np.nan
  df['owner_street_2'] = np.nan 
  df['owner_street_3'] = np.nan 
  df['owner_country_code'] = np.nan   
  df['current_cash_balance'] = np.nan
  df['date_reported'] = np.nan  
  df['number_of_pending_claims'] = np.nan   
  df['property_type'] = np.nan  
  df['number_of_paid_claims'] = np.nan   
  df['date_of_last_contact'] = np.nan   
  df['holder_street_1'] = np.nan   
  df['holder_street_2'] = np.nan   
  df['holder_street_3'] = np.nan   
  df['holder_city'] = np.nan   
  df['holder_state'] = np.nan   
  df['holder_zip'] = np.nan
  df['shares_reported'] = np.nan
  df = df[['owner_firstname', 'owner_middlename', 'owner_lastname', 'owner_street_1', 'owner_street_2', 'owner_street_3', 'owner_city', 'owner_state', 'owner_zip', 'no_of_owners', 'owner_country_code', 'current_cash_balance', 'number_of_pending_claims', 'number_of_paid_claims', 'date_of_last_contact', 'holder_name', 'holder_street_1', 'holder_street_2', 'holder_street_3', 'holder_city', 'holder_state', 'holder_zip', 'property_id', 'date_reported', 'property_type', 'cash_reported', 'shares_reported', 'reported_tangible_items', 'cusip']]
  df = df.applymap(lambda s:s.lower() if type(s) == str else s)
  df.to_csv('/Users/danielschwartz/Desktop/Simplefuture/State_Data/mo/MO.csv', index=None)

def flFunc():
  df = pd.read_csv(f"/Users/danielschwartz/Desktop/simplefuture/State_Data/fl/fl.csv", low_memory=False, error_bad_lines=False, encoding = "ISO-8859-1")    
  # df = df.head(10)
  df.columns = ['property_id', 'property_id2', 'year', 'number_of_pending_claims', 'owner_lastname', 'owner_firstname', 'owner_middlename', 'blank', 'blank', 'owner_street_1', 'owner_street_2', 'owner_street_3', 'owner_city', 'owner_state', 'owner_zip', 'num', 'holder_name', 'property_type', 'cash_reported', 'id', 'blank', 'shares_reported', 'cusip', 'blank', 'date_reported']
  df.drop(['property_id2'], axis=1, inplace=True)
  df.drop(['year'], axis=1, inplace=True)
  df.drop(['blank'], axis=1, inplace=True)

  df['reported_tangible_items'] = np.nan
  df['no_of_owners'] = np.nan
  df['owner_country_code'] = np.nan   
  df['current_cash_balance'] = np.nan
  df['number_of_pending_claims'] = np.nan   
  df['number_of_paid_claims'] = np.nan   
  df['date_of_last_contact'] = np.nan   
  df['holder_street_1'] = np.nan   
  df['holder_street_2'] = np.nan   
  df['holder_street_3'] = np.nan   
  df['holder_city'] = np.nan   
  df['holder_state'] = np.nan   
  df['holder_zip'] = np.nan

  df['owner_firstname'].replace('', np.nan, inplace=True)
  df['owner_lastname'].replace('', np.nan, inplace=True)
  df['owner_city'].replace('', np.nan, inplace=True)
  df.dropna(subset=['owner_firstname'], inplace=True)
  df.dropna(subset=['owner_lastname'], inplace=True)
  df.dropna(subset=['owner_city'], inplace=True)
  df = df[['owner_firstname', 'owner_middlename', 'owner_lastname', 'owner_street_1', 'owner_street_2', 'owner_street_3', 'owner_city', 'owner_state', 'owner_zip', 'no_of_owners', 'owner_country_code', 'current_cash_balance', 'number_of_pending_claims', 'number_of_paid_claims', 'date_of_last_contact', 'holder_name', 'holder_street_1', 'holder_street_2', 'holder_street_3', 'holder_city', 'holder_state', 'holder_zip', 'property_id', 'date_reported', 'property_type', 'cash_reported', 'shares_reported', 'reported_tangible_items', 'cusip']]
  df.to_csv('/Users/danielschwartz/Desktop/Simplefuture/State_Data/fl/flcopy.csv', index=None)

def gaFunc():
  # with open('/Users/danielschwartz/Desktop/Simplefuture/State_Data/ga/gacopy.txt') as infile:
    # with open('/Users/danielschwartz/Desktop/Simplefuture/State_Data/ga/ga.txt', 'w') as outfile:
    #   for line in infile:
    #     line.split(string.whitespace)
        
  df = pd.read_csv(f"/Users/danielschwartz/Desktop/simplefuture/State_Data/ga/ga.txt", nrows=10, encoding = "ISO-8859-1", low_memory=False, error_bad_lines=False, delim_whitespace=True)    
  # df = df.head(10)
  b[is.na(b)]<-""
  df.to_csv('/Users/danielschwartz/Desktop/Simplefuture/State_Data/ga/gacopy.csv', index=None)
gaFunc()