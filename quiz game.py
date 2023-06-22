
print ('welcome to my Quiz Game ')

playing = input ('Do want to play quiz game? ').lower()

if playing != 'yes':
    quit()
else:
    print ('                      ')
    print ('     Let"s                ')
    print ('        start              ')
    print ('             the          ')
    print ('                 game     ')
    print ('                      ')
    print ('                      ')

score = 0

answer = input ('Which country have the higest population? ').lower()
if answer == "china":
    print ('correct')
    score += 1
else:
    print ('incorrect')
answer = input ('Which country have the talles building ? ').lower()
if answer == "uae":
    print ('correct')
    score += 1
else:
    print ('incorrect')
answer = input ('Which country have the higest death rate? ').lower()
if answer == "bulgaria":
    print ('correct')
    score += 1
else:
    print ('incorrect')
answer = input ('Which country have the higest nummber of cars? ').lower()
if answer == "san marino":
    print ('correct')
    score += 1
else:
    print ('incorrect')
answer = input ('Which country have the higest mountain? ').lower()
if answer == "nepal":
    print ('correct')
    score += 1
else:
    print ('incorrect')
answer = input ('Which country have the higest nummber of dogs? ').lower()
if answer == "usa":
    print ('correct')
    score += 1
else:
    print ('incorrect')

answer = input ('Which country have the higest nummber of cows? ').lower()
if answer == "india":
    print ('correct')
    score += 1
else:
    print ('incorrect')

# result = (int((score/7)*100))
print ('You got ' +(str((score / 7)*100))+ '% correct.')

quit ()
