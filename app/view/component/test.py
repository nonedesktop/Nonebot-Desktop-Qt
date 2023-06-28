from typing import Any


class Human:
    def __init__(self, hight) -> None:
        self.hight = hight

    def say(slef):
        print("I am human.")


class Male(Human):
    def __init__(self, hight, name) -> None:
        super().__init__(hight)
        self.name = name


a = Male(name="wrz")
a.say()