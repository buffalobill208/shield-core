# each item in the manifest is an item and its weight
manifest = [["machine that goes ping!", 120], ["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["tea chests", 10], ["cheeses", 0]]

from operator import itemgetter, attrgetter
manifest.sort(key=itemgetter(1))
cargo_weight = 0
cargo_hold = []

for cargo in manifest:
    print("debug: the weight is currently: {}".format(cargo_weight))
    nextelem = manifest[manifest.index(cargo)+0]
    print("debug: next cargo",nextelem)
    if cargo_weight + cargo[1] <= 100:
        print("debug: adding item: {}".format(cargo[0]))
        print("debug: with weight: {}".format(cargo[1]))
        cargo_hold.append(cargo[0])
        print("debug: The cargo: ",cargo_hold)
        cargo_weight += cargo[1]

print(cargo_weight)
print(cargo_hold)
