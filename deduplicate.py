source = ["bananas", "mattresses", "tea", "dog", "tea", "cheeses"]

print(len(source))

def remove_duplicate(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)

    return target

print(remove_duplicate(source))
