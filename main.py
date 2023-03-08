# create a lambda expression that will square the items in the list

my_list = [5,4,3]

print(list(map(lambda item: item ** 2, my_list)))

# sort the list in ascending order starting with the tuple that has -1
a = [(0,2),(4,3),(9,9),(10,-1)]
print(list(sorted(a, key=lambda a: a[1])))