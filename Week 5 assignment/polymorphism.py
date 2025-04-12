class Cow:
    def speak(self):
        return "Moo!"

class Sheep:
    def speak(self):
        return "Bleat!"

# Polymorphism in action
for animal in [Cow(), Sheep()]:
    print(animal.speak())