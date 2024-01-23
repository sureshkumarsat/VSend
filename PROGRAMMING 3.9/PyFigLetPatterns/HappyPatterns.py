import time
import pyfiglet
from colorama import Fore
from subprocess import call


MSG = """I LOVE YOU"""


HEART = """
████████████████████████████████████████
██████▀        ▀████████▀▀       ▀██████
████▀            ▀████▀            ▀████
██▀                ▀▀                ▀██
██                  ███               ██
██                 ▄▀░█               ██
██          ████▄▄▄▀░░▀▀▀▀▄           ██
██▄         ████░░░░░░░░░░█          ▄██
████▄       ████░░░░░░░░░░█        ▄████
██████▄     ████▄▄▄░░░░░░░█      ▄██████
████████▄   ▀▀▀▀   ▀▀▀▀▀▀▀     ▄████████
██████████▄                  ▄██████████
████████████▄              ▄████████████
██████████████▄          ▄██████████████
████████████████▄      ▄████████████████
██████████████████▄▄▄▄██████████████████
"""


def print_message():
    f = pyfiglet.Figlet(font="slant")
    call("clear")
    for col in [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.YELLOW] * 10:
        print(col + f.renderText(MSG))
        print(HEART)
        time.sleep(0.05)
        call("clear")
    print(Fore.MAGENTA + f.renderText(MSG))
    print(HEART)


print_message()
