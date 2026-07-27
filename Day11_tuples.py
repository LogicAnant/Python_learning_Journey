tupp = (1, 3, 4, "this is tuple")
print(type(tupp), tupp)
if 3 in tupp:
    print("3 is present in tupp")
tupp2 = tupp[0:2]
print(tupp2)
animals = ("cat", "dog", "bat", "mouse", "pig"
, "horse", "donkey", "goat", "cow")
print(len(animals))
print(animals[::2])
print(animals[-8:-1:-2])

countries = ("japan", "america", "india", "china")
temp = list(countries)
temp.append("swizerland")
temp.pop(3)
temp[2] = ("chicago")
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = (countries + countries2)
print(southEastAsia)
print("count of india in countries is ", southEastAsia.count("india".capitalize()))

tup = (0, 1, 2, 3, 4, 1, 0, 3, 2)
print("count of 1 in tup is ", tup.count(1))
ind = tup.index(0, 2, 7)
print(ind)