"""
planetary_weights.py

Prompt the user for a weight on Earth and a planet. 
Print the equivalent weight on specified planet.

Programmer: Surajit A. Bose, Date: 2024.05.10
"""

import random

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
EARTH_GRAVITY = 1.0
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    """
    Get Earth weight. Get planet. Calculate and display weight on planet.
    
    Preconditions: None
    
    Postconditions: 
    - Earth weight received from user
    - Equivalent weight on Mars printed onscreen to two decimal places.
    """
    # Prompt user for a weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Prompt user for a planet. Ensure first letter is uppercase.
    # Remove leading or trailing spaces
    planet = str.title(input('Enter a planet: ').strip())
    
    # Get gravitational constant for specified planet
    # This syntax will not work in the Code in Place IDE
    # Use if-elif-else syntax there
    match planet:
        case 'Mercury':
            gravity_constant = MERCURY_GRAVITY
        case 'Venus':
            gravity_constant = VENUS_GRAVITY
        case 'Earth':
            gravity_constant = EARTH_GRAVITY
        case 'Mars':
            gravity_constant = MARS_GRAVITY
        case 'Jupiter':
            gravity_constant = JUPITER_GRAVITY
        case 'Saturn':
            gravity_constant = SATURN_GRAVITY
        case 'Uranus':
            gravity_constant = URANUS_GRAVITY
        case 'Neptune':
            gravity_constant = NEPTUNE_GRAVITY
        case 'Mystery':
            gravity_constant = random.random()
        case _:
            gravity_constant = 0
            
    # For valid planet, display weight on planet
    if gravity_constant:
        planetary_weight = round(earth_weight * gravity_constant, 2)
        print(f'The equivalent weight on {planet}: {planetary_weight}')
    # For invalid planet, print error message
    else:
        print(f'Planet {planet} not recognized.')
    
if __name__ == '__main__':
    main()