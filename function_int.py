# 1.Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# change value 10 in x to 15
for li in x:
    for li_item in range(len(li)):
        print(li[li_item])
        if li[li_item] == 10:
            li[li_item] = 15
print(x)

# change last_name jordan to bryant
students[0]['last_name'] = 'Bryant'
print(students[0])

# Change name messi to andres
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# change value 20 -> 30
z[0]['y'] = z[0]['x'] + z[0]['y']
print(z[0])


# 2.Iterate Through a List of Dictionaries

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# iterateDictionary(students)
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterate_dictionary(some_list):
    for x in some_list:
        print(
            f"first_name - {x['first_name']}, last_name - {x['last_name']}\n")


iterate_dictionary(students)

# 3. Get Values From a List of Dictionaries


def interate_dictionary2(key_name, some_list):
    for x in range(0, len(some_list)):
        print(some_list[x][key_name])


# 4.Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key.upper())
        for x in value:
            print(x)


printInfo(dojo)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank

8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
