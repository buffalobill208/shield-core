def tag_count(xml_count):
    """
    Function that takes as its argument a list of strings.  It return a count of how many of those strings are XML tags.
    """
    count = 0
    for x in xml_count:
        if x[0] == '<' and x[-1] == '>':
            count = count + 1
    return count

# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))
