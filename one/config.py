
import configparser


class Configer:
    configer = configparser.ConfigParser()
    configer.read('config.ini')

    @classmethod
    def get(cls,section,option):
        return Configer.configer.get(section, option)

    @classmethod
    def set(cls,section,option,value):
        Configer.configer.set(section,option,value)

    @classmethod
    def save(cls):
        Configer.configer.write('config.ini')


