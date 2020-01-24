print('Hello World')

# This is a comment
number_of_students = 10
age = 15
price = 11.5
first_name = "John"
last_name = "Doe"

print(number_of_students)
print(age, price, first_name, last_name)

print(type(number_of_students))
print(type(age), type(first_name), type(last_name), type(price))

is_pass = True
is_fail = False

print(type(is_pass), type(is_fail))

full_name = first_name + ' ' + last_name
print(full_name)

items = []
items = list

items = ['item1', 'item2', 'item3', 1.1, 10]
print(items)
print(items[3])

items2 = [1,2,3, [1,2,2, ['Hello']]]
print(items2)

items.append('This is a new item')
print(items)
items.pop()
print(items)

items3 = (1, 2, 3)
print(items3)