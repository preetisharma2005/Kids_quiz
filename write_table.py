#write table.
x = int(input("Enter number: "))
print('Table of', x, '!')


def mul():
    y = 1
    while y <= 10:
        z = x * y
        print(x, 'X', y, '=',  z)
        y += 1
    else:
        quit()
mul()



