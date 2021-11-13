"""This Program will display the Grouped Bar Chart of Top 5
Principal business activites in last 10 years.
It is divided into 3 modules:
    1.Map pba to registration count from last 10 years data.
    2.get top 5 pbas and order them based on increasing order of year.
    3.Plot the resulting data.
Note: pba means principal business activity.
"""

# importing libraries to deal with csv files and to plot the data.
import os
import csv
from matplotlib import pyplot as plt

LAST_10_YEARS = [str(year) for year in range(2012,2022)]

def map_pba_to_registration_count_by_year(filename):
    """It will create a dictionary that maps principal business activity
    to registration count from last 10 years data, and will return
    that dictionary.
    """
    pba_to_registration_count = {}
    with open(filename,"r",encoding = "ISO-8859-1") as file_obj:
        company_registration_reader = csv.DictReader(file_obj)
        for current_registration_info in company_registration_reader:
            try:
                date,_,year = current_registration_info["DATE_OF_REGISTRATION"].strip().split('-')
                if len(date)==4:
                    year = date
                elif int(year) in range(0,22):
                    year = '20'+year
                else:
                    year = '19'+year
            except ValueError:
                continue
            else:
                if int(year) in range(2012,2022):
                    principal_business_activity = \
                    current_registration_info["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"].strip()
                    if principal_business_activity not in pba_to_registration_count:
                        pba_to_registration_count[principal_business_activity] = {}
                    count = pba_to_registration_count[principal_business_activity].get(year,0) + 1
                    pba_to_registration_count[principal_business_activity][year] = count
    return pba_to_registration_count

def get_top_5_pba_s(pba_to_registration_count):
    """It will fetch the top 5 principal business activities based on
    the no.of the registrations done over last 10 years.
    """
    pba_to_registration_count_ordered = {}
    pba_names = list(pba_to_registration_count.keys())
    pba_names.sort(key=lambda name:sum(pba_to_registration_count[name].values()),reverse=True)
    top_5_pba_names = pba_names[:5][::-1]
    # Ordering the top 5 pba_s in the increasing order of year
    for pba in top_5_pba_names:
        pba_to_registration_count_ordered[pba] = []
        for year in LAST_10_YEARS:
            registration_count = pba_to_registration_count[pba].get(year,0)
            pba_to_registration_count_ordered[pba].append(registration_count)
    return pba_to_registration_count_ordered,top_5_pba_names
def plot_data(pba_to_registration_count_ordered,top_5_pba_names):
    """Creating and displaying the Bar Chart"""
    no_years = 10
    prev_start = list(range(0,no_years))
    bar_width=0.1
    figure_width,figure_height = 15,10
    plt.figure(figsize=(figure_width,figure_height))
    for pba in top_5_pba_names:
        registration_count_by_year = pba_to_registration_count_ordered[pba]
        label_name = " ".join(pba.strip().split(" ")[:2])
        plt.bar(prev_start,registration_count_by_year,width=bar_width,label=label_name)
        prev_start = [i+bar_width for i in prev_start]
    # Adding xtick labels
    start_pos = [i for i in range(no_years)]
    plt.xticks(start_pos,LAST_10_YEARS)
    plt.legend(loc='upper right')
    plt.title("Top 5 principal business activities in last 10 years",fontweight="bold")
    plt.xlabel("Year",fontweight="bold")
    plt.ylabel("Number of registrations",fontweight="bold")
    plt.show()

def execute():
    """It will call all the helper functions to achieve our aim"""
    file_path = os.getcwd()+"/../Data/Maharashtra.csv"
    pba_to_registration_count = map_pba_to_registration_count_by_year(file_path)
    pba_to_registration_count_ordered,top_5_pba_names = get_top_5_pba_s(pba_to_registration_count)
    plot_data(pba_to_registration_count_ordered,top_5_pba_names)

execute()
