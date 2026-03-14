a = False
b = False
c = False
d = True
if a:
    print('a')
elif b:
    print('b')
elif c:
    print('c')
else:
    a = True
    print('d')

print(f'esse é o novo valor de a: {a}')

def soma(a, b):
    return a + b