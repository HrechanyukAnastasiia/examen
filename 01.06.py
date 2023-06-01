#13
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} робить звук: {self.sound}")
animal = Animal("Корова", "Мууууууу")
animal.make_sound()