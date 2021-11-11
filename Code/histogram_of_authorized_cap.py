"""This Program will display the Histogram of Authorized Capital
with some intervals.
"""
# importing the libraries to deal with csv files and to plot the data.
import os
import csv
from matplotlib import pyplot as plt

# Extracting all the authorized capital data from the file.
authorized_capital = []
with open(os.getcwd()+"/../Data/Maharashtra.csv","r",encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader,None) # skipping the headers
    for row in reader:
        authorized_capital.append(float(row[8].strip()))

# These are the intervals we will show in histogram.
intervals = [1e3,2e3,3e3,4e3,5e3]
plt.hist(authorized_capital,intervals,ec="red",rwidth=0.7)
plt.xticks(intervals,["1T","2T","3T","4T","5T"])
plt.title("Histogram of Authorized Capital")
plt.xlabel("Range")
plt.ylabel("Number of Authorized Capitals")
plt.show()
