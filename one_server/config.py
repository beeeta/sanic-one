
import configparser
import os

cur_dir = os.path.dirname(__file__)
config_path = os.path.abspath(os.path.join(cur_dir,'config.ini'))

class Configer:
    configer = configparser.ConfigParser()
    configer.read(config_path)

    @classmethod
    def get(cls,section,option):
        return Configer.configer.get(section, option)

    @classmethod
    def set(cls,section,option,value):
        Configer.configer.set(section,option,value)

    @classmethod
    def save(cls):
        Configer.configer.write('config.ini')


