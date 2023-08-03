import os
import tkinter.messagebox
import shutil
from configparser import ConfigParser

from stg import settings
from stg import debug

CONFIG_EXAMPLE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_example.ini')


class ConfigLoader:
    def __init__(self):
        self.settings = settings.Settings()
        try:
            f = open('config.ini')
            f.close()
            conf = ConfigParser()
            conf.read('config.ini', encoding='utf-8')
            for key, value in conf['default'].items():
                if key == 'bg_color':
                    setattr(self.settings, key, str(value))
                elif key == 'is_full_screen':
                    if value == 'True':
                        setattr(self.settings, key, True)
                    else:
                        setattr(self.settings, key, False)
                else:
                    setattr(self.settings, key, int(value))
        except IOError:
            try:
                debug('no file')
                shutil.copyfile(CONFIG_EXAMPLE_PATH, 'config.ini')
            except IOError:
                tkinter.messagebox.showwarning(message='无法访问文件夹，请尝试换个文件夹。')

    def load(self) -> settings.Settings:
        return self.settings
