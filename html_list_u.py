def html_list(list_items):
    HTML_string = "<ul>\n"
    for item in list_items:
        HTML_string += "<li>{}</li>\n".format(item)
    HTML_string += "</ul>"
    return HTML_string

test = ['first string', 'second string']

print(html_list(test))
