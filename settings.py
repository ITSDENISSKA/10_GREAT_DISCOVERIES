import pygame
from moviepy.video.io.VideoFileClip import VideoFileClip

WIDTH = 1280
HEIGHT = 720
TILE_HEIGHT = 40
TILE_WIDTH = 40
MUSIC_SETTINGS = 44100, -16, 1, 512
END_VIDEO = VideoFileClip('video/123.mp4')
CLICK_SOUND = pygame.mixer.Sound("sounds/button.wav")