from flask import Flask, jsonify, request
import json
from DiceRoll import Dice

dice_dct = {}

app = Flask(__name__)


@app.route("/create", methods=["POST"])
def create_dice():
    data = request.get_json()
    dice = data["dice"]
    side = data["side"]
    time = data["time"]
    dice_objt = Dice(dice, side, time)
    roll = dice_objt.dice_roll()
    dice_dct[len(dice_dct)] = roll

    return jsonify({"message": " Created successfully"})


@app.route("/get_data", methods=["GET"])
def get_data():
    return jsonify(dice_dct)


@app.route("/update_data/<int:index>", methods=["PUT"])
def update_data(index):
    for key, value in dice_dct.items():
        for k1, v1 in value.items():
            print(k1, v1)
            if k1 == index:
                dice_dct[0][k1] = [5, 6, 1, 25]
    return dice_dct


@app.route("/delete_data/<int:index>", methods=["DELETE"])
def delelte_data(index):
    dice_dct[0].pop(index)
    return dice_dct


if __name__ == "__main__":
    app.run(debug=True)
