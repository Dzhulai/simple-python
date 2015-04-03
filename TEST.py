# ---------------------------------------------------------------------
def hotel_cost(days):
    return days * 140
def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475
    else:
        return False
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3 and days < 7:
        cost -= 20
    return cost
    
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print trip_cost("Los Angeles",5,600)


# ---------------------------------------------------------------------
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    return total
def get_average(students):
    homework = average(students['homework'])
    quizzes = average(students['quizzes'])
    tests = average(students['tests'])
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print get_letter_grade(get_average(lloyd))


def get_class_average(students):
    results = []
    for item in students:
        studentAver = get_average(item)
        results.append(studentAver)
    return average(results)


# ---------------------------------------------------------------------

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"


# ---------------------------------------------------------------------

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left  > 0 :
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print 'You win!'
        break
else:
    print 'sorry'
guesses_left -= 1


# ---------------------------------------------------------------------

print "Counting..."

for i in range(20):
    print i
    
# ---------------------------------------------------------------------



hobbies = []

for hobby in range(3):
    hobby = raw_input("Type your hobbies: ")
    hobbies.append(hobby)
for hobby in hobbies:
    print hobby

# ---------------------------------------------------------------------
#__________________
x = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,11]
y = [[1, 2, 3], [7, 8, 9], [1, 2, 3]]
z = ["spam", "eggs", "eggs", "ham"]

def count(sequence, item):
    number = 0
    for i in sequence:
        if i == item:
            number += 1
    return number

print count(x, 5),
print count(y, [1, 2, 3]),
print count(z, "eggs")


# ---------------------------------------------------------------------

def anti_vowel(text):
    for char in text:
        if char in 'AEIOUaeiou':
            text = text.replace(char,'')
    return text
print anti_vowel('cars')

# ---------------------------------------------------------------------

def censor(text, word):
    lst = text.split()
    for s in lst:
        if s == word:
            lst[lst.index(s)] = "*" * len(word)
    return " ".join(lst)




# ---------------------------------------------------------------------

thing = "spam!"

for c in thing:
    print c,

word = "eggs!"

# Your code here!
for c in word:
    print c


# ---------------------------------------------------------------------
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == "A" or char == "a":
        print "X",
    else:
        print char,



#Don't delete this print statement!
print


## ---------------------------------------------------------------------
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num,
for num in numbers:
    print num**2


# ---------------------------------------------------------------------
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    if d[key] > 0:
        print key, d[key]       




# choices -------------------------------------------------------------
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print (index + 1), str(item)


# ---------------------------------------------------------------------
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
    
    print 'A', f
else:
    print 'A fine selection of fruits!'


# ---------------------------------------------------------------------
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
    
else:
    print 'A fine selection of fruits!'
    print 'A', f
# ---------------------------------------------------------------------

# list_workers
list_workers = {'Luis' : 10, 'Ana' : 4, 'Maria' : 8, 'Marco' : 7, 'Jose' : 3, 'Angela' : 7, 'Din' : 9 }

print "Who's the best worker?"

for key in list_workers:
    if list_workers[key] == 10:
        print key, "is the best worker, no doubt"
    elif list_workers[key] > 7:
        print key, "is a very good worker, quite close to the best"
    elif list_workers[key] > 5:
        print key, "is a good worker, but not the best"
else:
    print key, "is not such a good worker and has failed"

# ---------------------------------------------------------------------

# is_even
x = [2, 3, 0]

def is_even(x):
    return x % 2 == 0

# ---------------------------------------------------------------------

def is_int(x):
    if x - int(x) == 0:
        return True
    else:
        return False

# ---------------------------------------------------------------------

def digit_sum(n):
    n = str(n)
    sum = 0
    for digit in n:
        sum = sum + int(digit)
    return sum

print digit_sum(1234)

# ---------------------------------------------------------------------

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

# ---------------------------------------------------------------------

def is_prime(x):
    if x < 2:
        return False
    else:
        n = 2
        while n < x:
            if x % n == 0:
                return False
                break
            n = n + 1
        else:
            return True


# ---------------------------------------------------------------------

def reverse(text):
    r = ''
    i = 0
    while i < len(text):
        r += text[len(text) - 1 - i]
        i += 1
    print len(text)
    return r

# ---------------------------------------------------------------------

def anti_vowel(text):
    for char in text:
        if char in 'AEIOUaeiou':
            text = text.replace(char,'')
    return text
print anti_vowel('wertyuioplkjhgfdsweddcvvfrrewwww')

# ---------------------------------------------------------------------

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
    x = 0
    word = word.lower()
    for i in word:
        x = x + score[i]
    return x


# ---------------------------------------------------------------------

def censor(text, word):
    lst = text.split()
    for s in lst:
        if s == word:
            lst[lst.index(s)] = "*" * len(word)
    return " ".join(lst)

# ---------------------------------------------------------------------

def purify(spisok):
    newspisok = []
    for n in spisok:
        if n % 2 == 0:
            newspisok.append(n)
    return newspisok

# ---------------------------------------------------------------------

def product(item):
    result = 1
    for i in item:
        result *= i
    return  result 
print product([4, 5, 5]) 


# ---------------------------------------------------------------------

def remove_duplicates(elements):
    newspisok = []
    for n in elements:
        if n not in newspisok:
            newspisok.append(n)
    return newspisok

# ---------------------------------------------------------------------

def median(array):
    array = sorted(array)
    count = len(array)
    if count % 2 == 0:
        return (array[count/2 - 1] + array[count/2]) / 2.0
    else:
        return array[count/2]
        
print median([1,2,3,4,5,5,6,6,7,7,7,7,7,8,8,8,9,9])

# ---------------------------------------------------------------------

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / float(len(scores))
print grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5
variance = grades_variance(grades)  
print grades_std_deviation(variance)

# ---------------------------------------------------------------------

my_dict = {
    "Name": "dvt",
    "Age": 25,
}
print my_dict.items()

# ---------------------------------------------------------------------

my_dict = {
    "Name": "dvt",
    "Age": 25,
}
print my_dict.keys()
print my_dict.values()

# ---------------------------------------------------------------------

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

# ---------------------------------------------------------------------

cubes_by_four = [ x**3 for x in range(1,11) if (x**3) % 4 == 0]
print cubes_by_four

# ---------------------------------------------------------------------

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# ---------------------------------------------------------------------

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x[0] == 'P', languages)

# ---------------------------------------------------------------------

squares = [x**2 for x in range(1, 11)]
print filter(lambda x: x >=30 and x <=70, squares)

# ---------------------------------------------------------------------

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
} 
print movies.items()

# ---------------------------------------------------------------------

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives

# ---------------------------------------------------------------------

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
reverse = garbled[::-2]
print reverse
message = filter(lambda x: x != "X",reverse)
print message

# ---------------------------------------------------------------------

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
# print reverse
message = filter(lambda x: x != "X",garbled)
print message

# ---------------------------------------------------------------------

print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT


# ---------------------------------------------------------------------

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11


# ---------------------------------------------------------------------

def check_bit4(input):
    m= input & 0b1000

    if m>0:
        return "on"
    else:
       return "off"

# ---------------------------------------------------------------------


a = 0b10111011
mask=0b110
desired=a|mask
print bin(desired)

# ---------------------------------------------------------------------

a = 0b11101110
mask = 0b11111111
flip = a^mask
print bin(flip)

# ---------------------------------------------------------------------

class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

apple = Fruit("apple", "red", "sour", False)

apple.description()
apple.is_edible()

# ---------------------------------------------------------------------

# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry

# ---------------------------------------------------------------------

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive

# ---------------------------------------------------------------------

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method he
    def description(self):
        print self.name
        print self.age
    
hippo = Animal("Chad", 7)
hippo.description()

# ---------------------------------------------------------------------

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health   = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    # Add your method he
    def description(self):
        print self.name
        print self.age
sloth = Animal("sloth", 4)
ocelot = Animal("ocelot", 5)
hippo = Animal("Chad", 7)
ocelot.description()
print ocelot.health
sloth.description()
print sloth.health
hippo.description()
print hippo.health

# ---------------------------------------------------------------------

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name
        
    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Eric")
my_cart.add_item("UuA", 10)
my_cart.items_in_cart

# ---------------------------------------------------------------------

class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()



# ---------------------------------------------------------------------

class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3 ):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1+self.angle2+self.angle3==180:
            return True
        else:
            return False

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1=self.angle
        self.angle2=self.angle
        self.angle3=self.angle

my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

# ---------------------------------------------------------------------

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        
my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg  

# ---------------------------------------------------------------------

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print "This is a %s %s with %i MPG." % (self.color, self.model, self.mpg)

my_car = Car("DeLorean", "silver", 88)

print my_car.display_car()

# ---------------------------------------------------------------------

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print "This is a %s %s with %i MPG." % (self.color, self.model, self.mpg)
    def drive_car(self):
        self.condition = "used"
        return self.condition

my_car = Car("DeLorean", "silver", 88)
print my_car.condition

my_car.drive_car()
print my_car.condition


# ---------------------------------------------------------------------

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print "This is a %s %s with %i MPG." % (self.color, self.model, self.mpg)
    def drive_car(self):
        self.condition = "used"
        return self.condition
my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition


class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type
    def drive_car(self):
        self.condition = "like new"

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car.condition

my_car.drive_car()
print my_car.condition

# ---------------------------------------------------------------------

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
my_point = Point3D (x = 1, y = 2, z = 3)
print my_point

# ---------------------------------------------------------------------

my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

# Add your code below!

for item in my_list:
    my_file.write(str(item)+ "\n")

my_file.close()

# ---------------------------------------------------------------------

my_file = open("output.txt", "r")
print my_file.read()
my_file.close()

# ---------------------------------------------------------------------

my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

# ---------------------------------------------------------------------

# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print read_file.read()
read_file.close()

# ---------------------------------------------------------------------

with open("text.txt", "w") as textfile:
	textfile.write("Success!")
textfile.close()

# ---------------------------------------------------------------------

with open("text.txt", "w") as lookfile:
    if not lookfile.closed:
        lookfile.close()
    print lookfile.closed

# ---------------------------------------------------------------------


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------





