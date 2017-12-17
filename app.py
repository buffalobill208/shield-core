from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

country_counts = {}
#print(country_counts)
count = 0
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if country not in country_counts:
        country_counts[country] = 1
        #print(country_counts)
    else:
        country_counts[country] += 1
        #print(country_counts)
"""
print("debug: Expected answer is 6, and the actual answer is ", country_counts['Germany'])
"""
print(country_counts)
