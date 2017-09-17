print('hey Hossein!')
string=raw_input("Enter a name: ")
print "You Entered " + string





x=[1,2,2,3,4]
print 'x: ' + str(x)
y=[5,9,7,8]
print 'y: ' + `y`
print "count 2 in x: " + str(x.count(2))
y.append(9)
print "append 9 to y: " + `y`
x.extend(y)
print 'extend x with y: ' + `x`
x.reverse()
print 'reverse the x: ' + `x`
x.sort()
print 'sort x: ' + `x`
y = sorted(y)
print 'sort y with sorted: ' + `y`
print 'find the index of 2 in x: ' + str(x.index(2))
x.insert(5, 22)
print 'insert 22 in 5th position of x: ' + `x`
x.pop(5)
print 'delet(pop) the 5th element in x: ' + `x`
x.remove(2)
print 'remove the element valued 2 in x: ' + `x`



string = 'hey %s go %s'
print 'string with varible: ' + string
var = ('hossein', 'home')
print 'tuples: ' + str(var)
print 'tuple placement into string: ' + string % var

print string.find('go')



example = "Hi hossein you ARE the best"
print 'an arbitrary string: ' + example
print 'change all characters to lower case: ' + example.lower()
print 'replacing \'Hi\' with \'hey\': ' + example.replace('Hi', 'hey')



family = {'Dad':'Bob', 'Mom':'Lisa', 'Bro':'Sam'}
print 'Dictionary Family: ' + str(family)
print 'value of the key "Dad" in Dic family: ' + family['Dad']
print 'value of the key "Mom" in Dic family: ' + family['Mom']
print 'value of the key "Bro" in Dic family: ' + family['Bro']
book = family.copy()
print 'copy Dic family to Dic book: ' + str(book)
print 'if the Dic book has the member "Dad": ' + str(book.has_key('Dad'))
print 'if the Dic book has the member "sis": ' + str(book.has_key('sis'))
family.clear()
print 'clear the content of Dic family: ' + str(family)

ages={'hossein':29, 'Dad':70, 'Bro':38}
print 'ages Dic: ' + str(ages)


print 'an if/else statement example: '
fish = 'tuna'
if fish=='bass':
	print 'the fish is bass'
elif fish=='tuna':
	print 'the fish is tuna'
else:
	print 'I don\'t know'
     

print "an if/else statement:"
thing = 'animal'
animal = 'cat'

if thing == 'animal':
	if animal == 'cat':
		print 'the animal is cat'
	elif animal == 'dog':
		print 'the animal is dog'
	else:
		print 'I dont know what the animal is'
else:
	print 'I dont know what the thing is'


x=5
if x > 3 and x < 7:
	print 'x is between 3 and 7'

x=[1,2,3]
y=z=[1,2,3]
print 'x==y operator: ' + str(x==y)
print 'x is y operator: ' + str(x is y)
print 'x is z operator: ' + str(x is z)

pizza = 'pizzahut'
print 'pizza: ' + pizza
print 'p in pizza operator: ' + str('p' in pizza)


print 'a while loop:'
n=1
while n<= 10:
	print `n`
	n+=1


print 'a for loop:'
gl=['bread', 'beef', 'milk', 'fruit']
for food in gl:
	print 'food is ' + food


print 'for loop using enumerate function'
for idx, food in enumerate(gl):
	print '#%d, %s' % (idx, food)


print 'a for loop with Dictionary:'
ages = {'Dad':42, 'Mom':48, 'Bro':20}
for item in ages:
	print item, ages[item]

print 'build a dictionary using list comprehension'
x = range(10)
print 'x: ' + str(x)
d = {z:z**2 for z in x if z % 2 == 0}
print 'd: ' + str(d)


print 'for loop in list comprehension'
x = range(7)
print 'x:' + str(x)
y = [z for z in x if z<5]
print 'y = (x<5)' + str(y)


print 'a while 1 loop'
while 1:
	string = raw_input('Enter a name: ')
	if string == 'quit': break


print 'define function mean(x,y)'
def mean(x,y):
	return (x+y)/2
print 'run mean(2.0,7):' + str(mean(2.0,7))


print 'define a function with default argument:'
def mean(x=2,y=8):
	return (x+y)/2
print 'run mean():' + str(mean())
print 'run mean(15):' + str(mean(15))
print 'run mean(y=30):' + str(mean(y=30))


print 'define a functione with pointer argument:'
def list(*food):
	print food
print 'run list("apple", "orange", "pich"):'
list("apple", "orange", "pich")


print 'define a function with Dictionary argument:'
def profile(**items):
	print items
print 'run profile(jimmy=12,sasy=21)'
profile(jimmy=12,sasy=21)


print 'define a function and pass a Dic as argument'
def someFunc(**dic):
	print dic
profile = {'dad':32, 'mom':42}
print 'Dic profile: ' + str(profile)
print 'run someFunc(**profile): ' 
someFunc(**profile)


print 'define a function and pass tuple as argument'
def math3(a,b,c):
	return a+b*c
tuna = (2,3,7)
print 'tuple tuna: ' + str(tuna)
print 'run math3(*tuna): ' + str(math3(*tuna))




print 'create a class:'
class newClass:
	eye = 'brown'
	age = 29
	height = 177
	def myfunc(self, x,y,z):
		return (x*y)/z

first = newClass()
print 'create an object of type newClass: ' + str(first)
print 'newClass elements: ' 
print '.age: ' + str(first.eye)
print '.height: ' + str(first.age) 
print '.eye: ' + str(first.height)
print '.myfunc(x,y,z): ' + str(first.myfunc(3,4,5.0))


print 'create a chid class inherit newClass totally:'
class child1(newClass):
	pass

print 'create a child class inherit the newClass except eye:'
class child2(newClass):
	eye='blue'

kid1=child1()
kid2=child2()
print 'kid1.eye: ' + str(kid1.eye)
print 'kid2.eye: ' + str(kid2.eye)



print 'create classes Mom and Dad and the class child inherits Mom and Dad:'
class Mom:
	age = 36
	eye = 'blue'

class Dad:
	age = 42
	height = 178

class Child(Mom, Dad):
	eye = 'brown'

child = Child()
print 'Child.age: ' + str(child.age)
print 'Child.height: ' + str(child.height)
print 'Child.eye: ' + str(child.eye)




print 'create a new Class with constructor __init__: '
class new:
	def __init__(self):
		print 'the constructor class new:'
		x = 10
		y = 20

print 'define myclass as the type of new():'
myclass = new()
print 'class elements: '


import math
dir(math)
help(math)


print 'create new file:'
fob = open('/home/hossein/Desktop/a.txt', 'w')
fob.write('hey Im here')
fob.close()

print 'read a file'
fob = open('/home/hossein/Desktop/a.txt', 'r')
print str(fob.read(3))
print str(fob.read())
fob.close()











