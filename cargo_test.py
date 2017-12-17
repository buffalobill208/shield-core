manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

#sorted(manifest, key=lambda weight: weight[1], reverse=True)
manifest.sort(key=lambda weight: weight[1], reverse=True)
print(manifest)
