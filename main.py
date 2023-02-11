# x = 42
#
# if x > 42:
#     print('x is greater than 42')
# elif x < 42:
#     print('x is lower than 42')
# else:
#     print('x is 42')
from collections import defaultdict

# dict
# def print_(day_name):
#     def inner():
#         print(day_name)
#     return inner
#
# day = "mon"
# d = {
#     'sat': print_('Saturday'),
#     'sun': print_('Sunday'),
#     'mon': lambda: print_('Monday')
# }
#
# # d[day]()
# d.get(day, lambda: print('Not found'))() # Null patter design pattern

# d = defaultdict(int)
# print(d)
# print(d['magic'])
# d['xd'] = 42
# print(d)

# day = 'pon'
#
# match day:
#     case 'sat':
#         print('Saturday')
#     case 'sat':
#         print('Sunday')
#     case _:
#         print('Not found')
# for x in range(5):
#
#     print(x)
#     if x == 3:
#         continue # lub break/ continue
#
# else:
#     print('magic')


#
# x = 3
#
# while x <5:
#     print(x)
#     x -= -1
#     if x == 4:
#         break
# else:
#     print('magic')

# x =42

# try:
#     z = 10 / x
# except ZeroDivisionError:
#     print('0')
# except TypeError:
#     print('String')
# else:
#     print('magic')
# finally:
#     print('finally')

# x =42
x =0
try:
    z = 10 / x
except ZeroDivisionError:
    pass
else:
    z += 10
finally:
    z += 5
