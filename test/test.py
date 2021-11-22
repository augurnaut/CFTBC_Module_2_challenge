import os
import pytest
from pathlib import Path

# Import Filters

from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

# import the save_csv functions we just wrote and the calculation packages

from qualifier.utils import fileio
from qualifier.utils import calculators

# make sure to import the save_csv function from file.io

from qualifier.utils.fileio import save_csv


def test_save_csv():
    
    data1 = [["West Central Credit Union - Premier Option",400000,0.9,0.35,760,2.7],
             ["namesless bank",100000,0.8,0.25,750,2.0]
             ] 

    save_csv(data1, "./data/output/qualifying_loans.csv")
    
    assert Path('./data/output/qualifying_loans_test.csv').exists() == True
    
    # removing the file post testing.
    
    os.remove("./data/output/qualifying_loans_test.csv")
    
    # giving an update.
    
    print("File saved & Tested successfully, File Removed!")
    
    save_csv(data2, "./data/output/qualifying_loans.csv")
    
    assert not Path('./data/output/qualifying_loans_test2.csv').exists() == True
    

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1000, 4000) == 0.25

    
def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(200000, 250000) == 0.80

    
def test_filters():
  
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))

    # check that the data is reading correctly
    
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    # check that the calculations are working properly
    
    monthly_debt_ratio = 0.375
    loan_to_value_ratio = 0.84

    # testing the calculate_monthly_debt function
    
    test_calculate_monthly_debt_ratio()
    
    # testing the calculate_loan_to_value function.
    
    test_calculate_loan_to_value_ratio()
    
    # Test the new save_csv code!
    
    test_save_csv()
