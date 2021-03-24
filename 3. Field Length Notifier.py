#******COMPARISON OPERATOR TASK******

name = input('Enter your name : ')
if len(name) < 3:
    print('Name must be at east 3 characters long!')
    print(f"Character Length: {len(name)}")
elif len(name) > 25:
    print('Name must be less than 25 characters!')
    print(f"Character Length: {len(name)}")
else:
    print('Name looks good!')
