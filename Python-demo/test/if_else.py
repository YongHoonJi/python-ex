
#if-else
print('Have u lunch today?');
have_lunch = input();

if(have_lunch =='y'):
    print('I am full :)')
else:
    print('No. I am starving...')

#if-elseif-else
print('Are u feeling well?')
answer1 = '1:funking great'
answer2 = '2:go away!'
answer3 = '3:Not bad'

my_feeling_today = input()

if(my_feeling_today == '1'):
    print(answer1)
elif(my_feeling_today == '2'):
    print(answer2)
elif(my_feeling_today == '3'):
    print(answer3)
else:
    print('you choose wrong answer')
