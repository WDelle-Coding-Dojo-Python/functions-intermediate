x = [ [5,2,3], [10,8,9] ] 
x[1].pop(0)
x[1].insert(0,15)
#print(x)

#students = [
#    {'first_name':  'Michael', 'last_name' : 'Jordan'},
#    {'first_name' : 'John', 'last_name' : 'Rosales'}
#]
#students[0]['last_name'] = 'Bryant'
#print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
#print(z)

def iterateDictionary(x):
    for v in x:
        for key,val in v.items():
            print(key+ "-"+ val)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#iterateDictionary(students)

def iterateDictionary2(key_name, x):
    for v in x:
        for key,val in v.items():
            if key == key_name:
                print(val)

#iterateDictionary2('first_name', students)

def printInfo(x):
    for key, val in x.items():
        print(len(val) ,' ' , key)
        for i in range(0,len(val)):
            print(val[i])


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
