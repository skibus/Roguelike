intro ='''
                                                    ███        ▄█    █▄     ▄█     ▄████████    ▄████████
                                                ▀█████████▄   ███    ███   ███    ███    ███   ███    ███
                                                   ▀███▀▀██   ███    ███   ███▌   ███    █▀    ███    █▀
                                                    ███   ▀  ▄███▄▄▄▄███▄▄ ███▌  ▄███▄▄▄      ▄███▄▄▄
                                                    ███     ▀▀███▀▀▀▀███▀  ███▌ ▀▀███▀▀▀     ▀▀███▀▀▀
                                                    ███       ███    ███   ███    ███    █▄    ███
                                                    ███       ███    ███   ███    ███    ███   ███
                                                   ▄████▀     ███    █▀    █▀     ██████████   ███
                                                   '''

story = '''            In this game we identify with the most wanted thief in Miami. Our goal is to steal artifacts from different places. First stage is quite easy
            and its rather warm up than a real robbery. Our hero is really hungry and his mission is to steal some food from the farm. The mad farmer (owner)
            will try to hinder us and save his fortune. When we complete first level we pass to the next levels: apartament, museum and bank. Every place
            holds the obstacles to be handled and enemies to be defeated. Stolen items will be added to our private backpack and displayed on the screen.
            Collected items can be exchanged for lives or extra stuff. You are able to open doors by picking keys hidden on the board. We hope you will
            enjoy our game. Have fun!'''


tutorial = '''                                              Game is really simple. If you want to move just press:
                                                                    w - move up,
                                                                    s - move down,
                                                                    a - move left,
                                                                    d - move right.

            Try to avoid enemies and other obstacles. Your mission is to steal as many items as it possible and of course to survive.'''

def introduce_screen():
    print (intro + 3*'\n')
    print (story + 1*'\n')
    print (tutorial)


introduce_screen()
