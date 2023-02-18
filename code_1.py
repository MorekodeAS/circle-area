input('Hello! Before we start i have one question for you. Can I?')
what_we_have = input('Do we have a radius or a diameter? ')
lenght = float(input('How long is it? '))
if what_we_have == 'radius':
    print('I think the area of this circle is equal', 3.14 * lenght ** 2)
else:
    rad = lenght / 2
    print('I think the area of this circle is equal', 3.14 * rad ** 2 )
print('I`m happy i could help :D')
