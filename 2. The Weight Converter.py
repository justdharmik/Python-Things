#******PROJECT WEIGHT CONVERTER******

weight = input('Enter your weight : ')
l_or_k = input('(L)bs or (K)g : ')

if l_or_k == str('k') or l_or_k == str('K'):                            #...instead-of-defining-string-can-use-"K"
    print(f'Your weight in Lbs is : {int(weight) / 0.45} Pounds')       #...here-you-can-mention-int-while-taking-input-initially
elif l_or_k == str('l') or l_or_k == str('L'):                          #...instead-of-defining-string-can-use-"L"
    print(f'Your weight in Kgs is : {int(weight) * 0.45} Kilos')        #...here-you-can-mention-int-while-taking-input-initially
else:
    print('Error: Please define unit.')

#------------------------------------------------------

