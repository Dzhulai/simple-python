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

