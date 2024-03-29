#!/usr/bin/python3
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint




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
 
 
 


def update_worksheet(data, worksheet):
    print(f'updating working sheets{worksheet}')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)


    

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus 
    """
    print("Calculating surplus data ...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data


    
    
    
def get_last_five_entries():
    """
    Collects columns of data from the sales worksheet, collecting 
    the last 5 entries for each sandwich
    """
    sales= SHEET.worksheet("sales")
    #colum = sales.col_values(3)
    #print(colum)
    
    columns = []
    for ind in range(1,7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    return columns
    
    
    
print("Welcome to love sandwiches data automation")

def main():
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    
    

main()

get_last_five_entries()

sales_columns = get_last_five_entries()