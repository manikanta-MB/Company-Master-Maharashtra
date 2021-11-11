"""This Program will display the Grouped Bar Chart of Number of registrations
done in each Principal Business Activity in Each Year.
It is divided into 4 modules:
    1.Map year to registration count by pba.
    2.Map pba to registration count by year.
    (deleting some years which have low registration count).
    3.Sort registration count by year.
    4.Plot the resulting data.
Note: pba means principal business activity.
"""
# importing libraries to deal with csv files and to plot the data.
import os
import csv
from matplotlib import pyplot as plt

def map_year_to_registration_count_by_pba(filename):
    """It will create a dictionary that maps Each year to
    registration count by corresponding principal business activity
    """
    with open(filename,"r",encoding = "ISO-8859-1") as file_obj:
        reader = csv.reader(file_obj) # skipping the headers.
        next(reader,None)
        for row in reader:
            try:
                date,_,year = row[6].strip().split('-')
                if len(date)==4:
                    year = date
                elif int(year) in range(0,22):
                    year = '20'+year
                else:
                    year = '19'+year
            except ValueError:
                continue
            else:
                if year not in registration_count_by_year:
                    registration_count_by_year[year] = {}
                principal_business_activity = row[11].strip()
                count = registration_count_by_year[year].get(principal_business_activity,0) + 1
                registration_count_by_year[year][principal_business_activity] = count

def update_registration_count_by_pba(pba_s,year):
    """It will update the registration count by principal business activity"""
    for pba,count in pba_s.items():
        if pba not in registration_count_by_pba:
            registration_count_by_pba[pba] = {}
        registration_count_by_pba[pba][year] = count

def map_pba_to_registration_count_by_year():
    """It will create a dictionary that maps principal business activity
    to registration count by year
    """
    for year,pba_s in registration_count_by_year.items():
        total_registrations = sum(pba_s.values())
        if total_registrations > 3000:
            years.add(year)
            update_registration_count_by_pba(pba_s,year)

def sort_registration_count_based_on_year():
    """It will create a dictionary that maps principal business activity
    to registration count sorted by year
    """
    for pba,reg_count_by_year in registration_count_by_pba.items():
        registration_count_by_pba_ordered[pba] = []
        for year in sorted_years:
            count = reg_count_by_year.get(year,0)
            registration_count_by_pba_ordered[pba].append(count)

def plot_data():
    """Creating and displaying the Bar Chart"""
    no_years = len(sorted_years)
    prev_start = list(range(0,no_years))
    bar_width=0.2
    fig = plt.figure()
    fig.set_figheight(12)
    fig.set_figwidth(12)
    fig_obj = fig.add_subplot(111)
    # Shrink current axis by 20%
    box = fig_obj.get_position()
    fig_obj.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    for pba,reg_count in registration_count_by_pba_ordered.items():
        label_name = "".join([w[0] for w in pba.split(" ")])
        fig_obj.bar(prev_start,reg_count,width=bar_width,label=label_name)
        prev_start = [i+bar_width for i in prev_start]
    # Adding xtick labels
    start_pos = [i+2 for i in range(no_years)]
    plt.xticks(start_pos,sorted_years)
    # Put a legend to the right of the current axis
    fig_obj.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title("Number of registrations done in each Principal Business Activity in Each Year")
    plt.xlabel("Year")
    plt.ylabel("Number of registrations")
    plt.show()

registration_count_by_year = {}
registration_count_by_pba = {}
years = set()
map_year_to_registration_count_by_pba(os.getcwd()+"/../Data/Maharashtra.csv")
map_pba_to_registration_count_by_year()
sorted_years = sorted(list(years))
registration_count_by_pba_ordered = {}
sort_registration_count_based_on_year()
plot_data()
