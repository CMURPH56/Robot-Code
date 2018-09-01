from num2words import num2words
from subprocess import call
import time, random, sys

talking = True
cmd_beg = 'espeak '
cmd_end = ' | aplay /home/pi/Desktop/Text.wav 2>/dev/null'

# Displays the commands that robot can do.
def robot_introduction(user_name):
    user_name = user_name.strip()
    intro  = user_name + ' something'
    intro  = intro.replace(' ', '_')
    call([cmd_beg + intro  + cmd_end], shell = True)

# Starts robots auto speach feature
def auto_speech(user_name):
    user_name = user_name.strip()
    text_list = ['AAHHH', '{} '.format(user_name), 'What is up'.format(user_name), 'blerp {}'.format(user_name)]
    saying = 0
    while talking:
        if saying == len( text_list) - 1:
            saying = 0
        else:
            saying = saying + 1

        text = text_list[saying]
        text = text.replace(' ', '_')
        call([cmd_beg + text + cmd_end], shell = True)
        time.sleep(2)

def talk_to_user():
    question = 'Hello my name is E 9 H 7  please enter your name so we can get to know each other better'
    question = question.replace(' ', '_')
    call([cmd_beg + question + cmd_end], shell = True)
    user_name = sys.stdin.readline()
    user_name = user_name.strip()
    
    greeting = "Hello {} nice to meet you".format(user_name) 
    greeting = greeting.replace(' ', '_')
    call([cmd_beg + greeting  + cmd_end], shell = True)
    return user_name


if __name__ == "__main__":
    user_name = talk_to_user()
    robot_introduction(user_name)
    command = sys.stdin.readline()
    while command:
        command = command.strip()
        if command == 'ok':
            auto_speech(user_name) 
        else:
            response = 'I do not understand please type the letter o than the letter k and press enter'
            response = response.replace(' ', '_')
            call([cmd_beg + response + cmd_end], shell = True)
            command = sys.stdin.readline()
            

