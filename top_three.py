def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    return sorted(input_list, reverse=True)[:3]

print(top_three([4,3,5,2,8]))
