# each item in the manifest is an item and its weight
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

cargo_weight = 0
cargo_hold = []

for elem in manifest:
    if (manifest.index(elem))+1 != len(manifest):
        thiselem = elem
        nextelem = manifest[manifest.index(elem)+1]
        print("debug: this cargo",thiselem)
        print("debug: next cargo",nextelem)

        for cargo in manifest:
            print("debug: the cargo weight is currently: {}".format(cargo_weight))
            if cargo_weight + cargo[1] >= 100:
                print("debug: breaking loop now!")
                break
            else:
                print("debug: adding item: {}".format(cargo[0]))
                print("debug: with weight: {}".format(cargo[1]))
                cargo_hold.append(cargo[0])
                cargo_weight += cargo[1]

    else:
        print("debug: this cargo",manifest[manifest.index(elem)])
        print("debug: next cargo",manifest[manifest.index(elem)])


print(cargo_weight)
print(cargo_hold)
