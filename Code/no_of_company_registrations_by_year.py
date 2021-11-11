"""This Program displays the bar chart of Number of Company registrations
on Each Year.
It is divided into 3 modules:
    1.Mapping year to registration count.
    2.Sort registration count by year.
    3.Plot the resulting data.
"""

# importing the libraries to deal with csv files and to plot the data.
import os
import csv
from matplotlib import pyplot as plt

def get_registrations_by_year(filename):
    """It will create the data of no.of registrations done by year, from scratch file"""
    with open(filename,"r",encoding = "ISO-8859-1") as file_obj:
        reader = csv.reader(file_obj) # skipping the headers.
        next(reader,None)
        for row in reader:
            try:
                date,_,year = row[6].strip().split('-')
                if len(date)==4:
                    # print(date)
                    registrations_by_year[date] = registrations_by_year.get(date,0) + 1
                elif int(year) in range(0,22):
                    year = '20'+year
                    registrations_by_year[year] = registrations_by_year.get(year,0) + 1
                else:
                    year = '19'+year
                    registrations_by_year[year] = registrations_by_year.get(year,0) + 1
            except ValueError:
                pass
def sort_data_by_year():
    """Sorting the no.of registrations by year"""
    data = []
    for year,count in registrations_by_year.items():
        data.append([year,count])
    data.sort(key=lambda x:int(x[0]))
    for year,reg_count in data:
        x_axis_values.append(year)
        y_axis_values.append(reg_count)

def plot_data():
    """Creating and displaying the bar chart"""
    fig = plt.figure()
    fig.set_figheight(35)
    fig.set_figwidth(10)
    fig_obj = fig.add_subplot(111)
    fig_obj.barh(x_axis_values,y_axis_values)
    # ax.set_yticklabels(y_axis_values, fontsize=5)
    plt.title("Number of Registrations year wise",fontweight='bold')
    plt.ylabel("Year",fontweight='bold')
    plt.xlabel("Number of Registrations",fontweight='bold')
    plt.show()

registrations_by_year = {}
x_axis_values,y_axis_values = [],[]
get_registrations_by_year(os.getcwd()+"/../Data/Maharashtra.csv")
sort_data_by_year()
plot_data()
