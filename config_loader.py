import os
import tkinter.messagebox
from shutil import copyfile
from configparser import ConfigParser

import settings
import tools

CFG_EXAMPLE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_example.ini')
CFG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')


class CfgLoader:
    def __init__(self):
        self.settings = settings.Settings()
        try:
            f = open(CFG_PATH)
            f.close()
            conf = ConfigParser()
            conf.read(CFG_PATH, encoding='utf-8')
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
                tools.debug('no file')
                copyfile(CFG_EXAMPLE_PATH, CFG_PATH)
            except IOError:
                tkinter.messagebox.showwarning(message='无法访问文件夹，请尝试换个文件夹。')

    def load(self) -> settings.Settings:
        return self.settings
