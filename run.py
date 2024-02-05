#!/usr/bin/python3
import gspread
from google.oauth2.service_account import Credentials



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREADS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREADS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)
print("hello world")
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def get_sales_data():
    """Get sales figures input from the user"""
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")
    
        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("data is valid")
            break
    
    return sales_data
 
def validate_data(values):
    """
    Inside this try coverts all string values to ints. 
    raises ValueError if strings cannot be converted. 
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values are required, you provided {len(values)}"
            )
    
    except ValueError as e: 
        print(f"Invalid data: {e} \n")
        return False
    
    return True
 
 
 

data = get_sales_data()