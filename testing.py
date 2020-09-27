class Animal:
    def __init__(self, voice):
        self.voice = voice

    def sound(self):
        return 'I heard a {}'.format(self.voice)

cat = Animal('Meow')
print(cat.sound())