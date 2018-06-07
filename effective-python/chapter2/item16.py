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