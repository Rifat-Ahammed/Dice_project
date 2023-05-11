import random


class Dice:

    """Here Dice class represent a dice with given
    dice and sides attribute.
    Where dice and sides int type
    """
    lst = [1, 2, 3, 4]

    def __init__(self, dice, sides, time):
        """Initialize a new dice object with given number of
            dice, sides and time
        Args:
            dice, sides and time (int) which is how many time need to die and
            number of sides of the die.
        """

        self.dice = dice
        self.sides = sides
        self.time = time

    def dice_roll(self):
        """dice_roll method returns a random number from 1 to self.sides

        Returns:
            dict: _random number from 1 to self.slide.
        """
        result_dict = {}

        for t in range(0, self.time):
            roll = []
            for i in range(0, self.dice):
                face = random.randint(1, self.sides)
                # i thought to extra 1 in the evry side, so that's why i just deleted 1.
                roll.append(face)
            result_dict[t + 1] = roll
        return result_dict


# rolling_history = {}
# # empty dict to store the value for 100 time
# count = 1

# while True:
#     dice = int(input("Dice - between 1 to 5: "))

#     if dice < 1 or dice > 5:
#         print("please, enter valid dice")
#         exit()

#     sides = int(input("sides between 1 to 100:  "))

#     if sides < 1 or sides > 100:
#         print("please, enter valid sides")
#         quit()

#     time = int(input("How many times you want to play: "))

#     dice_obj = Dice(dice, sides, time)

#     roling_info = dice_obj.dice_roll()

#     rolling_history[count] = roling_info
#     # storing value into empty dictonary

#     if count - 100 > 0:
#         first = next(iter(rolling_history))
#         rolling_history.pop(first)

#     count += 1

#     print(f"Rolling dice: {roling_info}")

#     print()
#     option = input("If you want to play again press (Y/N): ").upper()
#     if option == "N":
#         break

# print(f"Total amount of rolling : {rolling_history}")

# for key, value in rolling_history.items():
#     print(value)
