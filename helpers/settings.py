from moviepy.video.io.VideoFileClip import VideoFileClip
from pygame import Color

menu = True
music_playing = True

lvl_number = 1
count_of_incorrect_answers = 1
level = False
question = False
statistic_window = False
players_name = None

STATUS_BAR_COLOR = Color(187, 187, 187)
STATUS_BAR_VISIBILITY = 200
FONT_COLOR = Color(0, 0, 0)
MENU_BUTTON_INACTIVE_COLOR = Color(13, 162, 58)
MENU_BUTTON_ACTIVE_COLOR = Color(23, 204, 50)
LINE_EDIT_INACTIVE_COLOR = Color(167, 25, 163)
LINE_EDIT_ACTIVE_COLOR = Color(255, 0, 0)
QUESTION_BUTTON_INACTIVE_COLOR = Color(255, 140, 0)
QUESTION_BUTTON_ACTIVE_COLOR = Color(255, 215, 0)
WHITE_BACKGROUND = Color(255, 255, 255)
TABLE_COLOR = Color(0, 0, 0)

WIDTH = 1280
HEIGHT = 720
TILE_HEIGHT = 40
TILE_WIDTH = 40
MUSIC_SETTINGS = 44100, -16, 1, 512
END_VIDEO = VideoFileClip('./video/123.mp4')
FPS = 60
FONT = "Font/Text.ttf"

QUESSTION_BUTTONS_TEXT = \
    {
        "level1": ["Колесницы", "Бумагу", "Порох"],
        "level2": ["Колесо", "Изолента", "Камень"],
        "level3": ["Кремень", "Мрамор", "Известняк"],
        "level4": ["в Африке", "В Америке", "в Азии"],
        "level5": ["Танк", "Очки", "Карантин"],
        "level6": ["Бумага", "Воск", "Папирус"],
        "level7": ["Велосипед", "Телевизор", "Автомобиль"],
        "level8": ["Швейную  машину", "Штаны", "Кроссовки"],
        "level9": ["IBM", "Apple", "Samsung"],
        "level10": ["Илон Маск", "Стив Джобс", "Билл Гейтс"]
    }
