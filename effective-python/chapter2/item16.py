"""
consider generator instead of returning list
"""

def index_words(text):
  result = []
  if text:
    result.append(0)
  for index, letter in enumerate(text):
    if letter == ' ':
      result.append(index + 1)
    return result

address = 'Four score and seven years ago…'
result = index_words(address) 
print(result[:3])

print("========================================================")
print("=======Using Iterator=====")
print("========================================================")
def index_words_itr(text):
  if text:
    yield 0
  for index, letter in enumerate(text):
    if letter == ' ':
      yield index + 1


print("========================================================")
print("=======Using Iterator=====")
print("========================================================")
def index_file(handle):
  offset = 0 
  for line in handle:
    if line:
      yield offset 
    for letter in line:
      offset += 1 
      if letter == ' ': 
        yield offset

"""
1. Using generators can be clearer than the alternative of returning lists of accumulated results.
2. The iterator returned by a generator produces the set of values passed to yield expressions 
   within the generator function’s body.
3. Generators can produce sequence of output for arbitrarily large input because 
   their working memory doesn't include all input and output
"""