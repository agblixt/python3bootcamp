import termcolor
import pyfiglet
import random
# here is a really really long string that is way too long and really
# should be made shorter if the autopep8 module is working correctly. Lets
# check and see
text_message = input('What message would you like to display? ')
valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
print('Valid colors are: red, green, yellow, blue, magenta, cyan, white')
text_color = input('What color would you like your message to be ?')
if text_color not in valid_colors:
    text_color = random.choice(valid_colors)
f = pyfiglet.Figlet(font='slant')
print(termcolor.colored(f.renderText(text_message), color=text_color))
