# Use List Comprehention Instead of map and filter
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)
"""
Unless you’re applying a single-argument function, list comprehensions are clearer 
than the map built-in function for simple cases.
"""
# squares = a.map(lamda x: x ** 2, a)

chile_ranks = {"ghost": 1, 'habanero': 2, 'cayenne': 3} 
rank_dict = {rank: name for name, rank in chile_ranks.items()} 
chile_len_set = {len(name) for name in rank_dict.values()} 
print(rank_dict) 
print(chile_len_set)