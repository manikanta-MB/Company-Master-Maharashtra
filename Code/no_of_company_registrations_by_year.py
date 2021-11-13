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

def get_registrations_by_year(file_path):
    """It will create a dictionary that maps year to registration count,
    and will return that dictionary.
    """
    registrations_by_year = {}
    with open(file_path,"r",encoding = "ISO-8859-1") as file_obj:
        company_registration_reader = csv.DictReader(file_obj)
        for current_registration_info in company_registration_reader:
            try:
                date,_,year = current_registration_info["DATE_OF_REGISTRATION"].strip().split('-')
                if len(date)==4:
                    registrations_by_year[date] = registrations_by_year.get(date,0) + 1
                elif int(year) in range(0,22):
                    year = '20'+year
                    registrations_by_year[year] = registrations_by_year.get(year,0) + 1
                else:
                    year = '19'+year
                    registrations_by_year[year] = registrations_by_year.get(year,0) + 1
            except ValueError:
                pass
    return registrations_by_year
def sort_data_by_year(registrations_by_year):
    """Sorting the no.of registrations by year"""
    # considering the years only those having no.of registrations > 2000
    years = registrations_by_year.keys()
    top_years = list(filter(lambda year:registrations_by_year[year]>2000,years))
    top_years_sorted = sorted(top_years)
    x_axis_values,y_axis_values = [],[]
    for year in top_years_sorted:
        registration_count = registrations_by_year[year]
        x_axis_values.append(year)
        y_axis_values.append(registration_count)
    return x_axis_values,y_axis_values

def plot_data(x_axis_values,y_axis_values):
    """Creating and displaying the bar chart"""
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(10)
    fig_obj = fig.add_subplot(111)
    fig_obj.barh(x_axis_values,y_axis_values)
    # ax.set_yticklabels(y_axis_values, fontsize=5)
    plt.title("Number of Registrations year wise",fontweight='bold')
    plt.ylabel("Year",fontweight='bold')
    plt.xlabel("Number of Registrations",fontweight='bold')
    plt.show()

def execute():
    """It will call all the helper functions to achieve our aim"""
    file_path = os.getcwd()+"/../Data/Maharashtra.csv"
    registrations_by_year = get_registrations_by_year(file_path)
    x_axis_values,y_axis_values = sort_data_by_year(registrations_by_year)
    plot_data(x_axis_values,y_axis_values)

execute()
