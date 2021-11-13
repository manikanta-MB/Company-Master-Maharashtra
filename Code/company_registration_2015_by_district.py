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
    districts = {}
    with open(filename,"r",encoding="utf8") as file_obj:
        district_reader = csv.DictReader(file_obj)
        for current_district_info in district_reader:
            code = current_district_info["Pin Code"].strip()[:4]
            district = current_district_info["District"].strip()
            districts[code] = district
    return districts

def map_district_to_registration_count(filename,districts):
    """It will create the dictionary that maps district to registration count"""
    registrations_by_district = {}
    with open(filename,"r",encoding = "ISO-8859-1") as file_obj:
        company_registration_reader = csv.DictReader(file_obj)
        for current_registration_info in company_registration_reader:
            try:
                date,_,year = current_registration_info["DATE_OF_REGISTRATION"].strip().split('-')
                if len(date)!=4 and year=="15":
                    address = current_registration_info["Registered_Office_Address"].strip()
                    pincode = address.rpartition(' ')[-1]
                    if pincode.isdigit() and len(pincode)==6:
                        district_code = pincode[:4]
                        if district_code in districts:
                            district = districts[district_code]
                            count = registrations_by_district.get(district,0) + 1
                            registrations_by_district[district] = count
            except ValueError:
                pass
    return registrations_by_district
def plot_data(registrations_by_district):
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

def execute():
    """It will call all the helper functions to achieve our aim"""
    file_path = os.getcwd()+"/../Data/zipcode_district.csv"
    districts = map_pincode_to_district(file_path)
    file_path = os.getcwd()+"/../Data/Maharashtra.csv"
    registrations_by_district = map_district_to_registration_count(file_path,districts)
    plot_data(registrations_by_district)

execute()
