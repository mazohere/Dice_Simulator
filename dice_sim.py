import random

# assign variables for later
white = "\033[39m"
blue = "\033[34m"
point = blue + '+' + white
total_score = 0


# set up the presets for what the dice faces will look like + a list containing all the die faces
d_1 = '-----\n|---|\n|-' + point + '-|\n|---|\n-----'
d_2 = '-----\n|--' + point + '|\n' + '|---|\n|' + point +'--|\n-----'
d_3 = '-----\n|--' + point + '|\n|-' + point + '-|\n|' + point + '--|\n-----'
d_4 = '-----\n|' + point + '-' + point + '|\n|---|\n|' + point + '-' + point + '|\n-----'
d_5 = '-----\n|' + point + '-' + point + '|\n|-' + point + '-|\n|' + point + '-' + point + '|\n-----'
d_6 = '-----\n|' + point + '-' + point + '|\n|' + point + '-' + point + '|\n|' + point + '-' + point + '|\n-----'
die_faces = [d_1, d_2, d_3, d_4, d_5, d_6]

# create error function
def error(where):
    print('incorrect input, please try again')
    if where == 1:
        user_choice()

# create scoring function

# create random selection function
def random_selection():
    die_face = random.randint(1, 6)
    print('random number: ', die_face)
    print(die_faces[die_face - 1])
    global total_score
    total_score = total_score + die_face
    print('total score: ', total_score)

# create rolling function
def rolling_function(choice):
    if choice == '1':
        random_selection()
        print('user selected: 1')
    elif choice == '2':
        random_selection()
        random_selection()
        print('user selected: 2')

# promt the user to choose between 1 or 2 dice (function)
def user_choice():
    print('please choose between ' + blue + '1 ' + white + 'or ' + blue + '2 ' + white + ': ')
    choice = input(' ')
    if choice == '1' or choice == '2':
        rolling_function(choice)
    else:
        error(1)

user_choice()