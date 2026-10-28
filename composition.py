"""Composition: A house creates and owns its rooms."""
class Room:
    def __init__(self, label):
        self.label = label

class House:
    def __init__(self):
        self.rooms = [Room('Kitchen'), Room('Bedroom')]

    def describe(self):
        print('House rooms: ' + ', '.join(room.label for room in self.rooms))

if __name__ == '__main__':
    house = House()
    house.describe()
