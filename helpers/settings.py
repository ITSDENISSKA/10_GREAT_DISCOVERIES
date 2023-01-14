from moviepy.video.io.VideoFileClip import VideoFileClip

lvl_number = 1
WIDTH = 1280
HEIGHT = 720
TILE_HEIGHT = 40
TILE_WIDTH = 40
MUSIC_SETTINGS = 44100, -16, 1, 512
END_VIDEO = VideoFileClip('./video/123.mp4')
FPS = 60

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
