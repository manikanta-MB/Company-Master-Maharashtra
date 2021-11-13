"""This Program will display the Histogram of Authorized Capital
with some intervals.
"""
# importing the libraries to deal with csv files and to plot the data.
import os
import csv
from matplotlib import pyplot as plt

def get_authorized_capital_data(file_path):
    """It will extract all the authorized capital data from the file"""
    authorized_capital = []
    with open(file_path,"r",encoding = "ISO-8859-1") as file_obj:
        company_registration_reader = csv.DictReader(file_obj)
        for current_registration_info in company_registration_reader:
            authorized_capital.append(float(current_registration_info["AUTHORIZED_CAP"].strip()))
    return authorized_capital

def plot_data(authorized_capital):
    """It will create and display the histogram"""
    # These are the intervals we will show in histogram.
    intervals = [1e3,2e3,3e3,4e3,5e3]
    plt.hist(authorized_capital,intervals,ec="red")
    plt.xticks(intervals,["1T","2T","3T","4T","5T"])
    plt.title("Histogram of Authorized Capital",fontweight="bold")
    plt.xlabel("Range",fontweight="bold")
    plt.ylabel("Number of Authorized Capitals",fontweight="bold")
    plt.show()

def execute():
    """It will call all the helper functions to achieve our aim"""
    file_path = os.getcwd()+"/../Data/Maharashtra.csv"
    authorized_capital = get_authorized_capital_data(file_path)
    plot_data(authorized_capital)

execute()
