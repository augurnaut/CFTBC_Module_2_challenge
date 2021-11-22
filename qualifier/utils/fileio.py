# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

# moved save_csv function here to refine system design 
# starter files also literally says "save csv file"
    
def save_csv(qualifying_loans, output_path):

    # function description: saves all of the filtered results locally
    # args: 
    #   qualifying_loans (list[lists]): (has the data that needs to be saved)
    #   ouput_path (string): location of saved csv file 
    # returns: nothing; csv create in path

    # creating a path

    csvpath = Path(output_path)

    # naming the header.

    header = ["bank_data", "credit_score", "debt", "income", "loan_amount", "home_value"] 

    # write the list of lists as a csv

    with open(csvpath, "w", newline='') as csvfile:

        # create a csvwriter

        csvwriter = csv.writer(csvfile, delimiter=",")

        # write the header to the csv file

        csvwriter.writerow(header)

        # write the data rows

        for row in qualifying_loans:
                csvwriter.writerow(row)
