import pygame
import sys
from moviepy.editor import VideoFileClip

pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()


w = 1280
h = 720

test = True
menu = True
level1 = True
level2 = False
level3 = False
level4 = False
level5 = False
level6 = False
level7 = False
level8 = False
level9 = False
level10 = False
question = False
flPause = False

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('10 GREAT DISCOVERIES')
click = pygame.mixer.Sound("sounds/button.wav")
pygame.mixer.music.load("sounds/music.wav")
pygame.mixer.music.play(-1)

clip = VideoFileClip('video/123.mp4')

all_sprites = pygame.sprite.Group()
roads = pygame.sprite.Group()
blocks = pygame.sprite.Group()
doors = pygame.sprite.Group()


def load_level(lvl, lvl_number):
    px, py = 0, 0
    file = open(lvl, "r", encoding="utf-8")
    x = y = 0
    for line in file.readlines():
        for char in line:
            if char == "d":
                Door(f"lvl{lvl_number}/door.png", x, y)
            if char == "x":
                Block(f"lvl{lvl_number}/block.png", x, y)
            if char == ".":
                Road(f"lvl{lvl_number}/road.png", x, y)
            if char == "@":
                Road(f"lvl{lvl_number}/road.png", x, y)
                px, py = x, y
            x = x + 40
        x = 0
        y = y + 40
    file.close()
    return px, py


def print_text(message, x, y, font_color=(0, 0, 0), font_type="Font/Text.ttf", font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.menu = True
        self.question = True
        self.false = True
        self.clicked = False

    def draw(self, x, y, message, font_size=120):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        click_btn = pygame.mixer.Sound("sounds/vote_btn.wav")

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))

            if click[0] == 1:
                self.clicked = True
                click_btn.play()
            else:
                self.clicked = False

        else:
            pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))

        print_text(message=message, x=x + 10, y=y + 10, font_size=font_size)


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__(all_sprites)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if args:
            if args[0] == pygame.K_w and self.rect.y > 0:
                self.rect.y -= 40
            if args[0] == pygame.K_s and self.rect.y < h - 40:
                self.rect.y += 40
            if args[0] == pygame.K_d and self.rect.x < w - 40:
                self.rect.x += 40
            if args[0] == pygame.K_a and self.rect.x > 0:
                self.rect.x -= 40
            if pygame.sprite.spritecollideany(self, blocks):
                if args[1][0]: self.rect.y += 40
                if args[1][1]: self.rect.y -= 40
                if args[1][2]: self.rect.x += 40
                if args[1][3]: self.rect.x -= 40


class Road(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__(roads, all_sprites)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Door(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__(doors, all_sprites)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Block(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__(blocks, all_sprites)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    menu_background = pygame.image.load("backgrounds/background.png")
    screen.blit(menu_background, (0, 0))

    start_btn = Button(480, 145, (13, 162, 58), (23, 204, 50))

    start_btn.draw(410, 225, "Начать игру")
    menu = not start_btn.clicked
    pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while level1:
    px, py = load_level("lvl1/level1.txt", 1)

    player = Player("lvl1/player.png", px, py)

    while level1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
        if pygame.sprite.spritecollideany(player, doors):
            all_sprites.remove(all_sprites)
            doors.remove(doors)
            blocks.remove(blocks)
            roads.remove(roads)
            level1 = False
            question = True
        all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
        menu_background = pygame.image.load("backgrounds/question1.png")
        screen.blit(menu_background, (0, 0))

        true_btn = Button(382, 120, (255, 140, 0), (255, 215, 0))
        false1_btn = Button(360, 120, (255, 140, 0), (255, 215, 0))
        false2_btn = Button(350, 120, (255, 140, 0), (255, 215, 0))
        true_btn.draw(455, 268, " Колесницы", 90)
        false1_btn.draw(95, 450, "   Бумагу", 90)
        false2_btn.draw(840, 450, "    Порох", 90)
        question = true_btn.question
        if true_btn.clicked:
            question = False
            level2 = True
            click.play()
        if false1_btn.clicked:
            question = False
            level1 = True
            break
        if false2_btn.clicked:
            question = False
            level1 = True
            break

        pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while level2:
    px, py = load_level("lvl2/level2.txt", 2)

    player = Player("lvl2/player.png", px, py)

    while level2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flPause = not flPause
                        if flPause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
        if pygame.sprite.spritecollideany(player, doors):
            all_sprites.remove(all_sprites)
            doors.remove(doors)
            blocks.remove(blocks)
            roads.remove(roads)
            level2 = False
            question = True
        all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
        menu_background = pygame.image.load("backgrounds/question2.png")
        screen.blit(menu_background, (0, 0))

        true_btn = Button(355, 120, (255, 140, 0), (255, 215, 0))
        false1_btn = Button(335, 120, (255, 140, 0), (255, 215, 0))
        false2_btn = Button(350, 120, (255, 140, 0), (255, 215, 0))

        true_btn.draw(95, 450, "   Колесо", 90)
        false1_btn.draw(473, 268, " Изолента", 90)
        false2_btn.draw(840, 450, "   Камень", 90)
        question = true_btn.question
        if true_btn.clicked:
            question = False
            level3 = True
            click.play()
        if false1_btn.clicked:
            question = False
            level2 = True
            break
        if false2_btn.clicked:
            question = False
            level2 = True
            break

        pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while level3:
    px, py = load_level("lvl3/level3.txt", 3)

    player = Player("lvl3/player.png", px, py)

    while level3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level3 = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flPause = not flPause
                        if flPause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
        if pygame.sprite.spritecollideany(player, doors):
            all_sprites.remove(all_sprites)
            doors.remove(doors)
            blocks.remove(blocks)
            roads.remove(roads)
            level3 = False
            question = True
        all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        menu_background = pygame.image.load("backgrounds/question3.png")
        screen.blit(menu_background, (0, 0))

        true_btn = Button(355, 120, (30, 144, 255), (0, 191, 255))
        false1_btn = Button(352, 120, (30, 144, 255), (0, 191, 255))
        false2_btn = Button(355, 120, (30, 144, 255), (0, 191, 255))

        true_btn.draw(95, 490, "  Кремень", 90)
        false1_btn.draw(465, 305, "  Мрамор", 90)
        false2_btn.draw(840, 490, " Известняк", 90)

        if true_btn.clicked:
            question = False
            level4 = True
            click.play()
        if false1_btn.clicked:
            question = False
            level3 = True
        if false2_btn.clicked:
            question = False
            level3 = True
            break

        pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while level4:
    px, py = load_level("lvl4/level4.txt", 4)

    player = Player("lvl4/player.png", px, py)

    while level4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level4 = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flPause = not flPause
                        if flPause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
        if pygame.sprite.spritecollideany(player, doors):
            all_sprites.remove(all_sprites)
            doors.remove(doors)
            blocks.remove(blocks)
            roads.remove(roads)
            level4 = False
            question = True
        all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        menu_background = pygame.image.load("backgrounds/question4.png")
        screen.blit(menu_background, (0, 0))

        true_btn = Button(385, 120, (30, 144, 255), (0, 191, 255))
        false1_btn = Button(360, 120, (30, 144, 255), (0, 191, 255))
        false2_btn = Button(355, 120, (30, 144, 255), (0, 191, 255))

        true_btn.draw(840, 490, "  в Африке", 90)
        false1_btn.draw(465, 305, " В Америке", 90)
        false2_btn.draw(95, 490, "   в Азии", 90)

        if true_btn.clicked:
            question = False
            level5 = True
            click.play()
        if false1_btn.clicked:
            question = False
            level4 = True
        if false2_btn.clicked:
            question = False
            level4 = True
            break

        pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while level5:
    px, py = load_level("lvl5/level5.txt", 5)

    player = Player("lvl5/player.png", px, py)

    while level5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level5 = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flPause = not flPause
                        if flPause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

        if pygame.sprite.spritecollideany(player, doors):
            all_sprites.remove(all_sprites)
            doors.remove(doors)
            blocks.remove(blocks)
            roads.remove(roads)
            level5 = False
            question = True
        all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        menu_background = pygame.image.load("backgrounds/question5.png")
        screen.blit(menu_background, (0, 0))

        true_btn = Button(340, 120, (186, 85, 211), (238, 130, 238))
        false1_btn = Button(325, 120, (186, 85, 211), (238, 130, 238))
        false2_btn = Button(325, 120, (186, 85, 211), (238, 130, 238))

        true_btn.draw(465, 305, "    Танк", 90)
        false1_btn.draw(110, 490, "    Очки", 90)
        false2_btn.draw(840, 490, " Карантин", 90)

        if true_btn.clicked:
            question = False
            level6 = True
            click.play()
        if false1_btn.clicked:
            question = False
            level5 = True
        if false2_btn.clicked:
            question = False
            level5 = True
            break

        pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while level6:
    px, py = load_level("lvl6/level6.txt", 6)

    player = Player("lvl6/player.png", px, py)

    while level6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level6 = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flPause = not flPause
                        if flPause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

        if pygame.sprite.spritecollideany(player, doors):
            all_sprites.remove(all_sprites)
            doors.remove(doors)
            blocks.remove(blocks)
            roads.remove(roads)
            level6 = False
            question = True
        all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        menu_background = pygame.image.load("backgrounds/question6.png")
        screen.blit(menu_background, (0, 0))

        true_btn = Button(355, 120, (255, 140, 0), (255, 215, 0))
        false1_btn = Button(337, 120, (255, 140, 0), (255, 215, 0))
        false2_btn = Button(355, 120, (255, 140, 0), (255, 215, 0))

        true_btn.draw(840, 490, "   Бумага", 90)
        false1_btn.draw(480, 305, "    Воск", 90)
        false2_btn.draw(95, 490, "  Папирус", 90)

        if true_btn.clicked:
            question = False
            level7 = True
            click.play()
        if false1_btn.clicked:
            question = False
            level6 = True
        if false2_btn.clicked:
            question = False
            level6 = True
            break

        pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while level7:
    px, py = load_level("lvl7/level7.txt", 7)

    player = Player("lvl7/player.png", px, py)

    while level7:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level7 = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flPause = not flPause
                        if flPause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

        if pygame.sprite.spritecollideany(player, doors):
            all_sprites.remove(all_sprites)
            doors.remove(doors)
            blocks.remove(blocks)
            roads.remove(roads)
            level7 = False
            question = True
        all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        menu_background = pygame.image.load("backgrounds/question7.png")
        screen.blit(menu_background, (0, 0))

        true_btn = Button(400, 120, (255, 140, 0), (255, 215, 0))
        false1_btn = Button(400, 120, (255, 140, 0), (255, 215, 0))
        false2_btn = Button(400, 120, (255, 140, 0), (255, 215, 0))

        true_btn.draw(810, 490, "  Велосипед", 90)
        false1_btn.draw(70, 490, "  Телевизор", 90)
        false2_btn.draw(440, 305, " Автомобиль", 90)

        if true_btn.clicked:
            question = False
            level8 = True
            click.play()
        if false1_btn.clicked:
            question = False
            level7 = True
        if false2_btn.clicked:
            question = False
            level7 = True
            break

        pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while level8:
    px, py = load_level("lvl8/level8.txt", 8)

    player = Player("lvl8/player.png", px, py)

    while level8:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level8 = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flPause = not flPause
                        if flPause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

        if pygame.sprite.spritecollideany(player, doors):
            all_sprites.remove(all_sprites)
            doors.remove(doors)
            blocks.remove(blocks)
            roads.remove(roads)
            level8 = False
            question = True
        all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        menu_background = pygame.image.load("backgrounds/question8.png")
        screen.blit(menu_background, (0, 0))

        true_btn = Button(570, 120, (255, 20, 147), (255, 105, 180))
        false1_btn = Button(352, 120, (255, 20, 147), (255, 105, 180))
        false2_btn = Button(570, 120, (255, 20, 147), (255, 105, 180))

        true_btn.draw(30, 490, "Швейную  машину", 90)
        false1_btn.draw(465, 305, "   Штаны", 90)
        false2_btn.draw(680, 490, "      Кроссовки", 90)

        if true_btn.clicked:
            question = False
            level9 = True
            click.play()
        if false1_btn.clicked:
            question = False
            level8 = True
        if false2_btn.clicked:
            question = False
            level8 = True
            break

        pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while level9:
    px, py = load_level("lvl9/level9.txt", 9)

    player = Player("lvl9/player.png", px, py)

    while level9:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level9 = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flPause = not flPause
                        if flPause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

        if pygame.sprite.spritecollideany(player, doors):
            all_sprites.remove(all_sprites)
            doors.remove(doors)
            blocks.remove(blocks)
            roads.remove(roads)
            level9 = False
            question = True
        all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        menu_background = pygame.image.load("backgrounds/question9.png")
        screen.blit(menu_background, (0, 0))

        true_btn = Button(320, 120, (255, 140, 0), (255, 215, 0))
        false1_btn = Button(340, 120, (255, 140, 0), (255, 215, 0))
        false2_btn = Button(340, 120, (255, 140, 0), (255, 215, 0))

        true_btn.draw(475, 305, "    IBM", 90)
        false1_btn.draw(110, 490, "    Apple", 90)
        false2_btn.draw(820, 490, "  Samsung", 90)

        if true_btn.clicked:
            question = False
            level10 = True
            click.play()
        if false1_btn.clicked:
            question = False
            level9 = True
        if false2_btn.clicked:
            question = False
            level9 = True
            break

        pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while level10:
    px, py = load_level("lvl10/level10.txt", 10)

    player = Player("lvl10/player.png", px, py)

    while level10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level10 = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flPause = not flPause
                        if flPause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

        if pygame.sprite.spritecollideany(player, doors):
            all_sprites.remove(all_sprites)
            doors.remove(doors)
            blocks.remove(blocks)
            roads.remove(roads)
            level10 = False
            question = True
        all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        menu_background = pygame.image.load("backgrounds/question10.png")
        screen.blit(menu_background, (0, 0))

        true_btn = Button(335, 120, (255, 140, 0), (255, 215, 0))
        false1_btn = Button(352, 120, (255, 140, 0), (255, 215, 0))
        false2_btn = Button(335, 120, (255, 140, 0), (255, 215, 0))

        true_btn.draw(850, 490, "Илон Маск", 90)
        false1_btn.draw(465, 305, "Стив Джобс", 90)
        false2_btn.draw(95, 490, "Билл Гейтс", 90)

        if true_btn.clicked:
            question = False
            clip.preview()
            click.play()
        if false1_btn.clicked:
            question = False
            level10 = True
            break
        if false2_btn.clicked:
            question = False
            level10 = True
            break

        pygame.display.update()

pygame.quit()
