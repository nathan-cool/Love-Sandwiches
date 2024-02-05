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
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")
    input_data = input("Enter your data here: ")
    print(f"The data provided is {input_data}")
 
get_sales_data()