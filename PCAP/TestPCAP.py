
x = 0
try:
    while x < 10:
        print(x)
        x += 2
except Exception as e:
    print('Abend:',e)
finally:
    print('No error')
