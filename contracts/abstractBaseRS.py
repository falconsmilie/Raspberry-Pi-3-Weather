from abc import ABCMeta, abstractmethod


class AbstractBaseRS(metaclass=ABCMeta):

    @abstractmethod
    def set_weather_list(self):
        pass
