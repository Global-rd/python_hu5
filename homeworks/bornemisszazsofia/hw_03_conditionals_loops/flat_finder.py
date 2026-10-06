"""search criteria
city                                                monthly rent in USD
New York, San Francisco (okay)                      < 4000
Washington (no way)                                 none
Chicago (dream)                                     none                    
anything else (okay)                                <= 3000
"""

search_criteria_city = input("Please provide a city.").title().strip()
search_criteria_rent = int(input("Please provide the monthly rent amount."))


if search_criteria_city in ["New York", "San Francisco"] and search_criteria_rent < 4000:
    search_result = "can"
elif search_criteria_city == "Washington":
    search_result = "can't"
elif search_criteria_city == "Chicago":
     search_result = "can"
elif search_criteria_rent <= 3000:
    search_result = "can"
else:
    search_result = "can't"

""""
if search_criteria_city in ["New York", "San Francisco"] and search_criteria_rent < 4000:
    search_result = "can"
else:
    if search_criteria_city == "Washington":
        search_result = "can't"
    else: 
        if search_criteria_city == "Chicago":
            search_result = "can"
        else:
            if search_criteria_city not in ["New York", "San Francisco", "Chicago", "Washington"] and search_criteria_rent <= 3000:
                search_result = "can"
            else:
                search_result = "can't"
#print(search_result)
"""

print(f"If you want to live in {search_criteria_city} and your monthly rent is {search_criteria_rent} you {search_result} live there.")