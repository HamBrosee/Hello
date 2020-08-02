import webbrowser
# This program says hello, asks your name, and makes fun of all people named Geraughty.
print('Hello, world!')
print('What is your name?')  # ask for their name
myName = str.lower(input())
if myName == 'geraughty':
    print('You a Big Bitch')
else:
    print('It is nice to meet you, ' + str.upper(myName))
    print('Your PeePee:')
    print(len(myName))
    if len(myName) == len(myName):
        print('Nut!')
myAge = int(input('How old are you?\n'))
if myName == 'geraughty' and  (myAge > 1) :
    print('It smell like bitch in here')
print('You will be ' + str(int(myAge)+ 1)+ ' in a year.')
bitch = str.lower(input('Who is a bitch?\n')) #ask for the name of a bitch
if (bitch == 'geraughty') or (bitch == 'me') : 
    print('You are Correct!')
    webbrowser.open('https://www.youtube.com/watch?v=wnedkVrgFF0')

else:
    print('Actually, its Geraughty you dummy.')
