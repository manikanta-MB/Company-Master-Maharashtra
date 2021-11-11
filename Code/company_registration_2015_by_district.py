"""This Program will display the bar chart of number of registrations
done on each District in the year of 2015.
It is divided into 3 modules:
    1.Mapping pincode to district.
    2.Mapping district to registration count.
    3.Plotting the resulting data.
"""
# importing the libraries to deal with csv files and to plot the data.
import os
import csv
from matplotlib import pyplot as plt

def map_pincode_to_district(filename):
    """It will create the dictionary that maps
    unique code(generated from pincode) to district
    """
    with open(filename,"r",encoding="utf8") as file_obj:
        reader = csv.reader(file_obj)
        next(reader,None)
        for row in reader:
            code = row[0].strip()[:4]
            district = row[1].strip()
            districts[code] = district

def map_district_to_registration_count(filename):
    """It will create the dictionary that maps district to registration count"""
    with open(filename,"r",encoding = "ISO-8859-1") as file_obj:
        reader = csv.reader(file_obj)
        next(reader,None)
        for row in reader:
            try:
                date,_,year = row[6].strip().split('-')
                if(len(date)!=4 and year=="15"):
                    address = row[12].strip()
                    pincode = address.rpartition(' ')[-1]
                    if(pincode.isdigit() and len(pincode)==6):
                        district_code = pincode[:4]
                        if district_code in districts:
                            district = districts[district_code]
                            count = registrations_by_district.get(district,0) + 1
                            registrations_by_district[district] = count
            except ValueError:
                pass

def plot_data():
    """It will create and display the bar chart"""

    # preparing x-axis and y-axis values.
    x_axis_values,y_axis_values = [],[]
    for district_name,count in registrations_by_district.items():
        x_axis_values.append(district_name)
        y_axis_values.append(count)

    # Creating and displaying the bar chart
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(10)
    fig_obj = fig.add_subplot(111)
    fig_obj.barh(x_axis_values,y_axis_values)
    # ax.set_yticklabels(y_axis_values, fontsize=5)
    plt.title("Number of Registrations in 2015 district wise",fontweight='bold')
    plt.ylabel("District",fontweight='bold')
    plt.xlabel("Number of Registrations",fontweight='bold')
    plt.show()

districts = {}
registrations_by_district={}
map_pincode_to_district(os.getcwd()+"/../Data/zipcode_district.csv")
map_district_to_registration_count(os.getcwd()+"/../Data/Maharashtra.csv")
plot_data()
