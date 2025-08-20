from .d_dice import Dice
import random

def simple_roll(dice: Dice):
    random_face = random.randrange(1, dice.faces + 1)
    dice.current_face = random_face
    dice.current_value = dice.faces_values[dice.current_face]
    dice.current_face_value = {dice.current_face: dice.current_value}

def complex_roll(dice: Dice, intensity: float = 0.0, spin: float = 0.0, angle: float = 0.0, height: float = 0.0, 
                 weight: float = 0.0, weighted: dict = {0: 0}, surface_friction: float = 0.0):
    # Placeholder for complex roll logic

    # This function will include some form of graphs to roughly simulate a complex dice roll 
    pass