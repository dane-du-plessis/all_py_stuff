a = list('abc')
b = list('cba')

try:
    b.remove('b')
except ValueError:
    print('not a damn')
else:
    print('ok!')
