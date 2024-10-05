from karel.stanfordkarel import *

# This is as far as we got in section!

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    
    1. Move until on beeper
    2. Build the hospital
    3. Repeat until end of row
    """
    while no_beeper_present:
        move
    build_hospital()
    if front_is_clear:
        move()

def build_hospital():
    pass
    


if __name__ == '__main__':
    main()