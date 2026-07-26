list = ["Apple", "blue", "green"]
list.sort()
print(list)
list.reverse()
print(list)
list.append("=this is list")
print(list)
print(list.index("blue"))
list.insert(1, "red")
print(list)
r = ["rainbow"]
list.extend(r)
print(list)

num = [1,5,3,6,2,1,3,5,2,6]
print(type(num))
num.sort()
print(num)
print(num.index(1))
num.sort(reverse=True)
print(num)
num.append(f"this is the sum of the list = {sum(num)}")
print(num)
print(num.count(1))
print(num.copy())
end = [26]
num.extend(end)
print(num)