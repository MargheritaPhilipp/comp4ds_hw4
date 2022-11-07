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

import pandas as pd

covid = pd.read_csv("Documentos/hw4/git_repo/comp4ds_hw4/covid.csv")

def print_selection(data, active_cases):
    filtered_data = data[data.Active > active_cases].copy()
    filtered_data["ratio"]= filtered_data["Deaths"]/filtered_data["Confirmed"]
    average_ratio = filtered_data["ratio"].mean()

    print("The countries with more than " + str(active_cases) +
          " active cases are: " + str(filtered_data["Country"].tolist()))
    print("The average of deaths over confirmed cases among those countries is " +
          str(round(average_ratio, 3)))
    print(" ") # Including this so there is an empty space when looping prints

cases = [500, 1000, 5000]

for n in cases:
    print_selection(covid, n)


