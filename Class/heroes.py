import hero_class
import random

names = {
    1:'Super Cool',
    2:'Spider Lover',
    3:'Iron Spider',
    4:'Average Joe',
}

powers = {
    1:'Flying',
    2:'Beat Boxing',
    3:'Super Leg Strength',
    4:'Good at driving'
}

colors = {
    1:'Neon Black',
    2:'Deep Ocean Red',
    3:'Aqua Yellow',
    4:'Dark White'
}

weakness = {
    1:'Ladies',
    2:'Kryptoday',
    3:'Weak Arms'
}

def main(names,powers,colors,weakness):
    name = names[random.randint(1,4)]
    powers = powers[random.randint(1,4)]
    colors = colors[random.randint(1,4)]
    weakness = weakness[random.randint(1,3)]

    hero = hero_class.Hero(name,powers,colors,weakness)
    print(f'\nThe name of your hero is {hero.get_name()}'\
          f'\nYour hero\'s power is {hero.get_powers()}'\
          f'\nYour hero\'s favorite color is {hero.get_colors()}'\
          f'\nYour hero\'s weakness is {hero.get_weakness()}')

main(names,powers,colors,weakness)