from itertools import zip_longest

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

print("========================================================")
print("=======Normal Loops=====")
print("========================================================")
longest_name = None
max_letter = 0

for i in range(len(names)):
  count = letters[i]
  if count > max_letter:
    longest_name = names[i]
    max_letter = count
print(longest_name)

print("========================================================")
print("=======Enumerate=====")
print("========================================================")
longest_name = None
max_letter = 0
for i, name in enumerate(names):
  count = letters[i]
  if count > max_letter:
    longest_name = name
    max_letter = count
print(longest_name)

print("========================================================")
print("=======With Zip=====")
print("========================================================")
longest_name = None
max_letter = 0
for name, count in zip(names, letters):
  if count > max_letter:
    longest_name = name
    max_letter = count


print("========================================================")
print("=======With Zip Concept=====")
print("========================================================")
names.append('Rosalind')
for name, count in zip(names, letters):
  print(name)

"""
Zip keeps yielding tuples until a wrapped iterator is exhausted.
1. The zip built-in function can be used to iterate over multiple iterators in parallel.
2. In Python 3, zip is a lazy generator that produces tuples. 
   In Python 2, zip returns the full result as a list of tuples.
3. zip truncates its output silently if you supply it with iterators of different lengths.
4. The zip_longest function from the itertools built-in module lets you iterate over multiple iterators in parallel regardless of their lengths
"""
print("========================================================")
print("=======With Zip_longest Concept=====")
print("========================================================")
names.append('Rosalind')
for name, count in zip_longest(names, letters): # from itertools import zip_longest
  print(name, count)