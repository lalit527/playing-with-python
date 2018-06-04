"""
Simplify a matrix
"""
print("========================================================")
print("=======Flaten a matrix=====")
print("========================================================")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)
"""
These are resonable usage of multiple loop
"""
squared = [[x ** 2 for x in row] for row in matrix]
print(squared)

"""
If this expression included another loop, the list comprehension would get so long 
that you’d have to split it over multiple lines.
"""
my_lists = [
  [[1, 2, 3], [16, 25, 36], [49, 64, 81]]
]

flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]
print(flat)

## without multiple comprehension
flat = []
for sublist1 in my_lists:
  for sublist2 in sublist1:
    flat.extend(sublist2)
print(flat)


print("========================================================")
print("=======List Comprehension with if=====")
print("========================================================")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]
print(b)
print(c)

"""
condition can be applied at each level of looping after for
"""
print("=======condition at each level of looping=====")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 ==0]
            for row in matrix if sum(row) >= 10]
print(filtered)