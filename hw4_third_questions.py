##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)

# Dictionay created to test the functions
Weekly_Cases = {'Spain': [4, 8, 2, 0, 1],
                  'France': [2, 3, 6],
                  'Italy': [6, 8, 1, 7],
                  'Germany': [1, 2, 4, 8, 16]}

# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

def total_registered_cases(data:dict, country:str) -> int: 
    return sum(data[country])

#check if function works
total_registered_cases(Weekly_Cases,'Spain')

#Not sure if there is a way of inputting the country withuot quotation marks
# i.e. replacing the str() with something that puts what's insie in ""
#def total_registered_cases(data, country): 
    #print(sum(data[str(country)]))
#total_registered_cases(Weekly_Cases, Spain)

# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#
def total_registered_cases_per_country(data:dict) -> dict:
    totals = {}
    for i in data:
        totals[i]= sum(data.get(i))
    return totals

#check if function works
total_registered_cases_per_country(Weekly_Cases)

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

#def country_with_most_cases(data:dict) -> str:
#    totals = {}
#    for i in data:
#        totals[i]= sum(data.get(i))
#    return max(totals, key=totals.get)
  
def country_with_most_cases(data:dict) -> str:
    return max(data, key=lambda x : sum(data[x]))

#check if function works
country_with_most_cases(Weekly_Cases)
