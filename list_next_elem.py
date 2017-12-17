li = ["do", "re", "mi", "fa", "sol"]

for elem in li:
    if (li.index(elem))+1 != len(li):
        thiselem = elem
        nextelem = li[li.index(elem)+1]
        print('thiselem',thiselem)
        print('nextel',nextelem)
    else:
        print('thiselem',li[li.index(elem)])
        print('nextel',li[li.index(elem)])
