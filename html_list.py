def html_list(input):
    """
    This Function takes one argument, a list of strings, and returns a single string which is an HTML list.
    """
    output = ["<ul>"]
    for values in input:
        #This works too but the one I used is cleaner.
        #output.append("<li>" + values + "</li>")
        output.append("<li>{}</li>".format(values))
    output.append("</ul>")
    return "\n".join(output)

test = ['first string', 'second string']

print(html_list(test))
