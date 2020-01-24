items = [1, 2, 3, 4]
item_len = len(items)
print(item_len)

for i in items:
    print(i)

for i in range(0,3,2):
    print(items[i])

items2 = [100,200,300,400,500,600,700]
my_range = range(len(items), 2)
print(my_range)

items = [100, 200, 300, 400, 500, 600, 700, 800, 900, 100]

for i in range(1, len(items) - 1, 2):
    print(items[i])