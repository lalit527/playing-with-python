# import random
# random_bits = 0
# for i in range(64):
#   if randint(0, 1):
#     random_bits |= 1 << i

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry'] 
for flavor in flavor_list:
  print('%s is delicious' % flavor)

"""
to iterate over a list and also know the index of the current item in the list
"""

for i, flavour in enumerate(flavor_list):
  print('%d: %s' %(i + 1, flavor))

"""
a second parameter to enumerate to specify the number from which to begin counting
"""