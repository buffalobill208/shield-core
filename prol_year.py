Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}


def most_prolific(Beatles_Discography):
    #We will store a dictionary of years and number of albums per year
    years_dict = {}
    for album_title, year in Beatles_Discography.iteritems():
        if year in year_dict:
            years_dict[year] += 1
        else:
            years_dict[year] = 1

    max_albums = 0
    max_year = 0
    for year, album_nums in years_dict.iteritems():
        if album_nums > max_albums:
            max_albums = album_nums
            max_year = year
    return max_year

print(most_prolific(Beatles_Discography))
