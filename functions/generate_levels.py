from functions.load_image import load_image

from sprites import block, door, players, road
from sprites.all_sprites_groups.spritres_groups import all_sprites, doors, roads, blocks


def generate_maze_level(level, level_number):
    new_player, x, y = None, None, None
    px, py = 0, 0
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                road.Road(load_image(f'lvl{level_number}/road.png'), x, y, roads, all_sprites)
            elif level[y][x] == 'x':
                block.Block(load_image(f'lvl{level_number}/block.png'), x, y, blocks, all_sprites)
            elif level[y][x] == 'd':
                road.Road(load_image(f'lvl{level_number}/road.png'), x, y, roads, all_sprites)
                door.Door(load_image("door.png"), x, y, doors, all_sprites)
            elif level[y][x] == '@':
                road.Road(load_image(f'lvl{level_number}/road.png'), x, y, roads, all_sprites)
                px, py = x, y

    new_player = players.PlayerForMaze(load_image(f'lvl{level_number}/player.png'), px, py, all_sprites)
    return new_player, x, y


def generate_platformer_level(level, level_number):
    new_player, x, y = None, None, None
    px, py = 0, 0
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 'x':
                block.Block(load_image(f'lvl{level_number}/block.png'), x, y, blocks, all_sprites)
            elif level[y][x] == 'd':
                door.Door(load_image("door.png"), x, y, doors, all_sprites)
            elif level[y][x] == '@':
                px, py = x, y

    new_player = players.PlayerForPlatformer(load_image(f'lvl{level_number}/player.png'), px, py, all_sprites)
    return new_player, x, y, load_image("background.png")
