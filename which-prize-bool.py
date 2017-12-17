#Returns the prize-winning message, given a number of points
def which_prize2(points):
	prize = None
	if points <= 50:
		prize = "a wooden rabbit"
	elif 151 <= points <= 180:
		prize = "a wafer-thin mint"
	elif 181 <= points <= 200:
		prize = "a penguin"

	if prize:
		return "Congratulations! You have won a {}!".format(prize)
	else:
		return "Oh dear, no prize this time."
print(which_prize2(201))
