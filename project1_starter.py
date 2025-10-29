"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Miles Johnson]
Date: [10/26/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    
    level = 1
    gold = 100
    strength, magic, health = calculate_stats(character_class, level)
    return {"name": name, "class": character_class, "level": level, "strength": strength, "magic": magic, "health": health, "gold": gold}
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation


def calculate_stats(character_class, level):
    primary_bonus = 4
    secondary_bonus = 2
    tertiary_bonus = 1
    level_multiplier = level - 1

    if character_class == "Rogue":
        strength = 45 + (primary_bonus * level_multiplier)
        magic = 5 + (tertiary_bonus * level_multiplier)
        health = 80 + (secondary_bonus * level_multiplier)
    elif character_class == "Cleric":
        strength = 10 + (tertiary_bonus * level_multiplier)
        magic = 40 + (secondary_bonus * level_multiplier)
        health = 85 + (primary_bonus * level_multiplier)    
    elif character_class == "Mage":
        strength = 5 + (tertiary_bonus * level_multiplier)  
        magic = 80 + (primary_bonus * level_multiplier)
        health = 45 + (secondary_bonus * level_multiplier)
    elif character_class == "Warrior":
        strength = 50 + (primary_bonus * level_multiplier)
        magic = 5 + (tertiary_bonus * level_multiplier)
        health = 75 + (secondary_bonus * level_multiplier)
    else:
        strength = 0
        magic = 0
        health = 0
    return (strength, magic, health)
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)


def save_character(character, character_file):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    with open(character_file, 'w') as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True
    # TODO: Implement this function
    # Remember to handle file errors gracefully

import os
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as file:
        lines = file.readlines()
        character = {}
        for line in lines:
            key, value = line.strip().split(": ")
            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)
    return character
        
    # TODO: Implement this function
    # Remember to handle file not found errors


def display_character(character):
    
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    # TODO: Implement this function


def level_up(character):

    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character['level'] += 1
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health

    # TODO: Implement this function
    # Remember to recalculate stats for the new level


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    char = create_character("Aria", "Mage")
    display_character(char)
    save_character(char, "test_char.txt")
    loaded = load_character("test_char.txt")
    display_character(loaded)
    
    level_up(char)
    display_character(char)
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
