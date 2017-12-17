# each item in the manifest is an item and its weight
manifest = [["machine that goes ping!", 120], ["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["tea chests", 10], ["cheeses", 0]]

from operator import itemgetter, attrgetter
manifest.sort(key=itemgetter(1))
print(manifest)
