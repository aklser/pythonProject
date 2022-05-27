from abc import ABCMeta, abstractmethod


class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_left_arm(self):
        pass

    @abstractmethod
    def draw_right_arm(self):
        pass

    @abstractmethod
    def draw_left_foot(self):
        pass

    @abstractmethod
    def draw_right_foot(self):
        pass

    @abstractmethod
    def draw_body(self):
        pass

    @abstractmethod
    def draw_head(self):
        pass


class Thin(Builder):

    def draw_left_arm(self):
        print("左手")

    def draw_right_arm(self):
        print("右手")

    def draw_left_foot(self):
        print("左脚")

    def draw_right_foot(self):
        print("右脚")

    def draw_body(self):
        print("瘦")

    def draw_head(self):
        print("头")


class Fat(Builder):

    def draw_left_arm(self):
        print("左手")

    def draw_right_arm(self):
        print("右手")

    def draw_left_foot(self):
        print("左脚")

    def draw_right_foot(self):
        print("右脚")

    def draw_body(self):
        print("胖")

    def draw_head(self):
        print("头")


class Director:
    def __init__(self, person):
        self.person = person

    def draw(self):
        self.person.draw_left_arm()
        self.person.draw_right_arm()
        self.person.draw_left_foot()
        self.person.draw_right_foot()
        self.person.draw_body()
        self.person.draw_head()


if __name__ == '__main__':
    thin = Thin()
    fat = Fat()
    director_thin = Director(thin)
    director_thin.draw()
    director_fat = Director(fat)
    director_fat.draw()
