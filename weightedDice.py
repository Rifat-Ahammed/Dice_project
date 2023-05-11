import random


class Dice:
    def __init__(self, dice, sides, weights=None):
        """here 'weights' that takes a list of weights for
        each of the die. If 'weights' is not provided, then
        we can assume that all faces have an equal probability
        of beign rolled.
        """
        self.dice = dice
        self.sides = sides
        legth = len(weights)
        if weights:
            if legth != sides:
                raise ValueError("Number of weights must match number of sides")
                # lentgh of weigth has to be equal of side
                # if the length of weights equal to side it
                # will store the value into selt.weights
            else:
                self.weights = weights
        else:
            """if weights=None that means user didn't provide a list
            then code the else block gonna be excuted. In that case we
            can assume that all faces of the die have equal probability
            of beign rolled
            """
            self.weights = [1 / sides] * sides

    def roll(self):
        roll = []
        for i in range(self.dice):
            face = random.choices(range(1, self.sides + 1), weights=self.weights)[0]
            roll.append(face)
        return roll


# Create a weighted 6-sided die where the first face has a 50% chance of being rolled
# and the remaining faces have an equal chance of being rolled
dice_object = Dice(dice=1, sides=6, weights=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1])

# Roll the die 10 times
for i in range(20):
    print(dice_object.roll(), end=" ")
