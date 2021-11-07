import random


# couple of lines needed to be taken from assignment since I was not able to complete it on my own
# TODO: Define the Thrower class here.
class Thrower:
    def __init__(self):
        self.dice = []
        self.num_throws = 0

    def can_throw(self):
        # if self.dice == 5 or self.dice == 0 or self.num_throws == 0:
        #     return True

        return (self.dice.count(5) > 0 or self.dice.count(1) > 0
                or self.num_throws == 0)
        # throw = True
        # return throw

    def get_points(self):
        points = 0
        for points in self.dice:
            if self.dice == 1:
                points *= 100
            elif self.dice == 5:
                points *= 50
            else:
                return points

    # return self.dice.count(5) * 50 + self.dice.count(1) * 100

    def throw_dice(self):
        self.dice.clear()
        for i in range(5):
            result = random.randint(1, 6)
            self.dice.append(result)
        self.num_throws += 1
