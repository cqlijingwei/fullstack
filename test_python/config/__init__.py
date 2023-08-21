import configparser
import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.join(ROOT_PATH, 'config.ini'))
