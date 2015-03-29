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



# ---------------------------------------------------------------------



# ---------------------------------------------------------------------



# ---------------------------------------------------------------------



# ---------------------------------------------------------------------



# ---------------------------------------------------------------------
