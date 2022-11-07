#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:35:41 2022

@author: MargheritaP
"""


#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(cvlist:list,job_title:str) -> list: 
    # users
    users=[]
    for i in cvlist:
        for j in i['jobs'] :
            if j==job_title:
                users.append(i['user'])
    return users


#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(cvlist:list) -> dict: 
    all_jobs=set()
    for i in cvlist:
        for j in i["jobs"]:
            all_jobs.add(j)
    dict={}
    for i in all_jobs:
        dict[i]= len(has_experience_as(cvlist, i))
    return dict


#check if function works


#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.
def most_popular_job(CV_list:list) -> tuple:
    jobfreq=job_counts(CV_list)
    maxjob=max(jobfreq,key=lambda x: jobfreq[x])
    return (maxjob,jobfreq[maxjob])


