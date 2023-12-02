import os
import re

os.chdir(os.path.dirname(os.path.realpath(__file__)))

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

#TEST DATA
TEST_DATA = [
'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

def serialize(input):
    game_json = {}
    game_id = int(re.findall(r'\d+', input.split(":")[0])[0])
    game_json['game_id'] = game_id
    draws = [x.strip() for x in input.split(":")[1].split(";")]
    game_json['draws'] = {}
    for i in range(len(draws)):
        game_json['draws'][i] = {}
        game_json['draws'][i]['red'] = 0
        game_json['draws'][i]['green'] = 0
        game_json['draws'][i]['blue'] = 0
        colors = [x.strip() for x in draws[i].split(",")]
        for color in colors:
            number = int(re.findall(r'\d+', color)[0])
            if 'red' in color:
                game_json['draws'][i]['red'] = number
            elif 'green' in color:
                game_json['draws'][i]['green'] = number
            elif 'blue' in color:
                game_json['draws'][i]['blue'] = number  
    return game_json 

def check_game(game):
    for draw in game['draws']:
        if game['draws'][draw]['red'] > RED_LIMIT or game['draws'][draw]['green'] > GREEN_LIMIT or game['draws'][draw]['blue'] > BLUE_LIMIT:
            return False
    return True


# test_powers = []
# #Test case
# for game in TEST_DATA:
#     game = serialize(game)
#     max_red = 0
#     max_green = 0
#     max_blue = 0
#     for draw in game['draws']:
#         if game['draws'][draw]['red'] > max_red:
#             max_red = game['draws'][draw]['red']
#         if game['draws'][draw]['green'] > max_green:
#             max_green = game['draws'][draw]['green']
#         if game['draws'][draw]['blue'] > max_blue:
#             max_blue = game['draws'][draw]['blue']
#     power = max_red*max_green*max_blue
#     test_powers.append(power)
# print(test_powers)
# print(sum(test_powers))

        
powers = []
with open("input.txt") as f:
    for line in f.readlines():
        game = serialize(line)
        max_red = 0
        max_green = 0
        max_blue = 0
        for draw in game['draws']:
            if game['draws'][draw]['red'] > max_red:
                max_red = game['draws'][draw]['red']
            if game['draws'][draw]['green'] > max_green:
                max_green = game['draws'][draw]['green']
            if game['draws'][draw]['blue'] > max_blue:
                max_blue = game['draws'][draw]['blue']
        power = max_red*max_green*max_blue
        powers.append(power)
print(powers)
print(sum(powers))
        