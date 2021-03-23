#******FIELD LENGTH CALC******

name = input('Enter your name : ')
if len(name) < 3:
    print('Name must be at east 3 characters long!')
elif len(name) > 25:
    print('Name must be less than 15 characters!ss')
else:
    print('Name looks good!')
