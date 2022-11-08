#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:43:25 2022

"""

###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #
import os
import pandas as pd
dir = os.path.dirname(os.path.realpath(__file__))
# dir_path=os.path.realpath(__file__)
# pwd=os.getcwd()
path1=dir+'/covid.csv'
path2 = dir+'/data/covid.csv'
# print(path1,path2)
try:
      covid = pd.read_csv(path1)
except:

      covid = pd.read_csv(path2)

# ideally we just want to specify the path from the github working directory
# where the csv file is in the folder called data that falls under gitignore



def print_selection(data, active_cases):
    filtered_data = data[data.Active > active_cases].copy()
    filtered_data["ratio"]= filtered_data["Deaths"]/filtered_data["Confirmed"]
    average_ratio = filtered_data["ratio"].mean()

    print(f"\n The countries with more than {active_cases} \
active cases are: {', '.join(filtered_data['Country'].tolist())} \n \
The average of deaths over confirmed cases among these countries is \
{round(average_ratio, 3)}\n")

cases = [500, 1000, 5000]

for n in cases:
    print_selection(covid, n)


