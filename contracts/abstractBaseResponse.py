from abc import ABCMeta, abstractmethod


class AbstractBaseResponse(metaclass=ABCMeta):

    @abstractmethod
    def set_weather_list(self):
        pass
