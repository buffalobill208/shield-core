# each item in the manifest is an item and its weight
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

#Sorted cargo hold from heaviest to lightest
#manifest.sort(key=lambda weight: weight[1], reverse=True)
cargo_weight = 0
cargo_hold = []

# Loop through sorted manifest, stop early when cargo_hold is full.
for cargo in manifest:
    # break out of loop early if we've already filled cargo hold to capacity.
    #if cargo_weight > 100:
    #    break
    if cargo_weight + cargo[1] <= 100:
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]

print(cargo_weight)
print(cargo_hold)
