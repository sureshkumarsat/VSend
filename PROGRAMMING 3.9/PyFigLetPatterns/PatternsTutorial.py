import os
import time
import pyfiglet
from colorama import Fore
from subprocess import call


MSG = "I LOVE YOU"
FONT = "slant"
FIREWORKS = """
                                       .
              . .                     -:-             .  .  .
            .'.:,'.        .  .  .     ' .           . \ | / .
            .'.;.`.       ._. ! ._.       \          .__\:/__.
             `,:.'         ._\!/_.                     .';`.      . ' .
             ,'             . ! .        ,.,      ..======..       .:.
            ,                 .         ._!_.     ||::: : | .        ',
     .====.,                  .           ;  .~.===: : : :|   ..===.
     |.::'||      .=====.,    ..=======.~,   |"|: :|::::::|   ||:::|=====|
  ___| :::|!__.,  |:::::|!_,   |: :: ::|"|l_l|"|:: |:;;:::|___!| ::|: : :|
 |: :|::: |:: |!__|; :: |: |===::: :: :|"||_||"| : |: :: :|: : |:: |:::::|
 |:::| _::|: :|:::|:===:|::|:::|:===F=:|"!/|\!"|::F|:====:|::_:|: :|::__:|
 !_[]![_]_!_[]![]_!_[__]![]![_]![_][I_]!//_:_\\![]I![_][_]!_[_]![]_!_[__]!
 -----------------------------------"---''''```---"-----------------------
"""


def clear():
    call("clear", shell=True)


def print_ily_msg():
    f = pyfiglet.Figlet(font=FONT)
    clear()
    for col in [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.YELLOW] * 10:
        print(col + f.renderText(MSG))
        print(FIREWORKS)
        time.sleep(0.05)
        clear()
    print(Fore.WHITE + f.renderText(MSG))
    print(FIREWORKS)


print_ily_msg()
