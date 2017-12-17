beatles_discography = {"Rubber Soul": 1965, "Magical Mystery Tour": 1967, "Sgt. Pepper's Lonely Hearts Club Band": 1967, "Revolver": 1966, "The Beatles": 1968, "With the Beatles": 1963, "Beatles for Sale": 1964, "Yellow Submarine": 1963, "A Hard Day's Night": 1964, "Help": 1965, "Let It Be": 1970, "Abbey Road": 1969, "Twist and Shout": 1964, "Please Please Me": 1963}

# Define beatles_years table.
beatles_years = {}
def list_2_string(list):
    for i in list:
        l = str(i)
    return l
def most_prolific(beatles_discography):
    """
    Takes a dict table and returns the year in which the most albums were released.

    If there are multiple years with the same maximum number of releases, the function shall return a list of years.
    """

    #STEP 1 Insert album years into the beatles_years dict.
    for year in beatles_discography:
        """
        Make a tally of the number of albums released per year.
        """
        #STEP 2 If the album year is in the dict, increment its value by one to keep count
        if beatles_discography[year] in beatles_years:
            beatles_years[beatles_discography[year]] += 1
        #STEP 3 If the album year isn't in the dict already, add it and set the value to 1
        else:
            beatles_years[beatles_discography[year]] = 1
    #return beatles_years

    #STEP4 Define most_years table.
    most_years = []
    #STEP5 Calculate maximum year in beatles_years table.
    max_year = max(beatles_years.values())
    #return max_year

    #STEP 7 Insert years into the most_years dict.
    for year in beatles_years:
        #STEP 8 If the year in the beatles_years dict is equal to the max_year value, append year in the most_years dict.
        if beatles_years[year] == max_year:
            most_years.append(year)
        else:
            #year += 1
    """
    if len(most_years) == 1:
        return list_2_string(most_years)
    else:
    """
    return most_years

#Call the most_prolific function with the input "beatles_discography" and print the output
print(most_prolific(beatles_discography))
