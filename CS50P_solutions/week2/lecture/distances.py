distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
}
def main():
    #for each key I have in dict
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from earth")

main()
# we also have values() method
