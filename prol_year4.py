Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}


def most_prolific(Beatles_Discography):
    """
    We will store a dictionary of years and number of albums per year
    """

    # STEP 1 Define beatles_years table.
    beatles_years = {}

    #STEP 2 Insert album years into the beatles_years dict.
    for year in Beatles_Discography:
        """
        Make a tally of the number of albums released per year.
        """
        #STEP 3 If the album year is in the dict, increment its value by one to keep count
        if Beatles_Discography[year] in beatles_years:
            beatles_years[Beatles_Discography[year]] += 1
        #STEP 4 If the album year isn't in the dict already, add it and set the value to 1
        else:
            beatles_years[Beatles_Discography[year]] = 1
    #return beatles_years

    # Find the year in which the maximum number of albums was published.
    #STEP 6 Define most_years table.
    most_years = []
    #STEP 7 Calculate maximum year in beatles_years table.
    max_year = max(beatles_years.values())
    return max_year

    #STEP 8 Insert years into the most_years dict.
    for year in beatles_years:
        #STEP 9 If the year in the beatles_years dict is equal to the max_year value, append year in the most_years dict.
        if beatles_years[year] == max_year:
            most_years.append(year)

    #Returns the most_years list.
    return most_years

#Call the most_prolific function with the input "Beatles_Discography" and print the output
print(most_prolific(Beatles_Discography))
