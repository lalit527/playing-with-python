"""
try/except/else/finally
"""
# handle = open('/tmp/random_data.txt') # May raise IOError 
# try:
#   data = handle.read() # May raise UnicodeDecodeError 
# finally:
#   print('closing file')
#   handle.close()

print("========================================================")
print("=======try with except=====")
print("========================================================")
handle = open('/tmp/random_data.txt') # May raise IOError 
try:
  data = handle.read() # May raise UnicodeDecodeError 
except ValueError as e:
  print('closing file')
  handle.close()
else:
  print('Not in error')


print("========================================================")
print("=======All exception block=====")
print("========================================================")
UNDEFINED = object()
def divide_json(path):
  handle = open(path, ‘r+’) 
  try:
    data = handle.read() 
    op = json.loads(data) 
    value = ( op[‘numerator’] / op[‘denominator’]) 
  except ZeroDivisionError as e:
    return UNDEFINED 
  else:
    op[‘result’] = value 
    result = json.dumps(op) 
    handle.seek(0) 
    handle.write(result) 
  finally:
    handle.close()

"""
1. The try/finally compound statement lets you run cleanup code regardless of whether exceptions were raised in the try block.
2. The else block helps you minimize the amount of code in try blocks and visually distinguish the success case from the try/except blocks.
3. An else block can be used to perform additional actions after a successful try block but before common cleanup in a finally block.
"""