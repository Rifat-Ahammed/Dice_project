# riahamm-DE1.1


# Rolling Dice Game








## Description

The "Dice Rolling Game with Rolling History" is a simple game that allows the user to roll a dice or multiple dice with a specified number of sides and number of rolls. After each roll, the game displays the result and prompts the user to roll again or exit. The game also keeps track of the rolling history for the last 100 rolls, allowing the user to review their previous rolls. 

The game is suitable for anyone who enjoys playing dice games or wants to practice their math skills. It can be played alone or with friends, and the rolling history feature makes it easy to keep track of previous rolls and analyze the results.
## Badges

python: https://www.python.org/downloads/release/python-390/  

This link will help you to understand depth knowledge of python.
## Visualization/Demo

    Dice - between 1 to 5: 4  
    sides between 1 to 100:  20  
    How many times you want to play: 2  
    Rolling dice: {1: [13, 5, 15, 13], 2: [9, 8, 10, 12]}

    If you want to play again press (Y/N): Y  
    Dice - between 1 to 5: 3  
    sides between 1 to 100:  56  
    How many times you want to play: 3  
    Rolling dice: {1: [18, 20, 17], 2: [26, 14, 31], 3: [56, 44, 7]}

    If you want to play again press (Y/N): Y  
    Dice - between 1 to 5: 2  
    sides between 1 to 100:  45  
    How many times you want to play: 4  
    Rolling dice: {1: [1, 12], 2: [12, 19], 3: [12, 22], 4: [6, 35]}

If you want to play again press (Y/N): N   
When you will click "N" that means you don't want to play anymore and want to close the game.

## Installation

If you are new in programming, you will need to install Python on your computer to run the "Dice Rolling Game with Rolling History" code. You can download the latest version of Python from the official website: https://www.python.org/downloads/

Once you have installed Python, you can run the code in a Python IDE (Integrated Development Environment) such as  
PyCharm:https://www.jetbrains.com/pycharm/download/#section=windows  
VS Code: https://code.visualstudio.com/download  
IDLE (Integrated Development and Learning Environment) which comes bundled with Python.

There are also online code editors that you can use to run Python code, such as Repl.it, CodeSandbox, or Google Colab.

In addition to Python, the "Dice Rolling Game with Rolling History" code does not require any additional libraries or dependencies, so you should be able to run it without any issues once you have installed Python and set up your development environment.

## Usage

Here is a step-by-step guide on how to use the "Dice Rolling Game with Rolling History" code:

1. Install Python on your computer if you haven't already done so. You can download the latest version of Python from the official website: https://www.python.org/downloads/

2. Download the "Dice Rolling Game with Rolling History" code from the source where you found it.

3. Open a Python IDE such as PyCharm, Visual Studio Code, or IDLE.

4. Open the "Dice Rolling Game with Rolling History" code in your IDE.

5. Run the code by clicking on the "Run" button or pressing the "F5" key.

6. Follow the prompts in the console window to enter the number of dice, sides, and times you want to roll the dice.

7. The program will display the results of each roll in the console window, as well as a rolling history of the last 100 rolls.

8. After each roll, the program will prompt you to play again. Enter "Y" to play again or "N" to exit the program.

9. Once you are finished playing, close the console window to exit the program.

That's it! The "Dice Rolling Game with Rolling History" code should be easy to use and provide an enjoyable experience for anyone who wants to roll dice in a virtual setting.
# Flask API
## Description

The "Dice Rolling Game with Rolling History" is a simple game that allows the user to roll a dice or multiple dice with a specified number of sides and number of rolls. After each roll, the game displays the result and prompts the user to roll again or exit. The game also keeps track of the rolling history for the last 100 rolls, allowing the user to review their previous rolls. 

The game is suitable for anyone who enjoys playing dice games or wants to practice their math skills. It can be played alone or with friends, and the rolling history feature makes it easy to keep track of previous rolls and analyze the results.
## Description For API

We know that there are six commonly used HTTP request methods, which are

    GET
    POST
    PUT
    DELETE
    PATCH
    HEAD

In this Flask Dice Roller API is a web application that provides a RESTful API for generating random dice rolls. The API allows clients to create dice objects with a specified number of dice, sides, and times to roll, generate random rolls for those dice, and retrieve or modify the stored results. The application is built using Flask, a popular Python web framework, and leverages the DiceRoll module to generate random rolls for each dice object. Flask Dice Roller API is useful for applications that require random number generation, such as gaming, simulation, and testing.
## Badges For API

Flask API: https://pythonbasics.org/flask-rest-api/

To know more about Flask API you can check this website.  

If you want to put your API online,  
use: https://www.pythonanywhere.com/?affiliate_id=00535ced 

## Demo for API


To create a route in API use 'POST' method    
and you can use json, text etc file.  
Example: 

    {"dice": 5, "side": 25, "time": 3} 

To get data from databse use 'GET' method    
and you will get data as a json, text etc file.  
Example:

    {
        "0": {
            "1": [
                11,
                8,
                2,
                3,
                6
            ],
            "2": [
                17,
                12,
                11,
                15,
                12
            ],
            "3": [
                18,
                9,
                4,
                1,
                5
            ]
        }
    }

To update your data form databse you have to use 'PUT' method

        {
            "0": {
                "1": [
                    2,
                    3,
                    4,
                    5
                ],
                "2": [
                    17,
                    12,
                    11,
                    15,
                    12
                ],
                "3": [
                    18,
                    9,
                    4,
                    1,
                    5
                ]
            }
        }
As you can see it's updated values of number 1 key.

To delete your data form databse you have to use 'DELETE' method and need an index number which index you want to delete.

    {
        "0": {
            "2": [
                5,
                1,
                22,
                13,
                1
            ],
            "3": [
                12,
                12,
                5,
                22,
                22
            ]
        }
    }

Deleted the number 1 key and values.


## Installation for API

As a novice, you will need to install Python and Flask to run this API. Here are the steps:

1. Install Python: You can download Python from the official website (https://www.python.org/downloads/). Follow the instructions to install Python on your computer.

2. Install Flask: Once you have installed Python, you can use pip (Python's package manager) to install Flask. Open a command prompt or terminal window and run the following command:

   ```
   pip install Flask
   ```

3. Install requests (optional): If you plan to test the API using a client like Postman, you may also want to install the requests library. You can install it using pip:

   ```
   pip install requests
   ```

Once you have installed Python and Flask, you should be able to run the Flask Dice Roller API.

For Flask API you also can use Postman. 
To download Postman use   
Postman website: https://www.postman.com/downloads/
## Usages for API

To use the Flask Dice Roller API, follow these steps:

1. Run the Flask app: Open a command prompt or terminal window, navigate to the directory containing the `dice_API.py` file, and run the following command:

   ```
   python dice_API.py
   ```

2. Create a dice roll: Use a client like Postman or cURL to send a POST request to the `/create` endpoint with the following JSON data:

   ```
   {
       "dice": 2,
       "side": 6,
       "time": 1
   }
   ```

   This will create a new dice roll with 2 dice, 6 sides each, and 1 time.

3. Get all dice rolls: Use a client to send a GET request to the `/get_data` endpoint to retrieve all the dice rolls that have been created.

4. Update a dice roll: Use a client to send a PUT request to the `/update_data/1` endpoint with the index of the dice roll you want to update (e.g. `/update_data/1`). Send the updated dice roll data in the request body in the same format as the POST request.

5. Delete a dice roll: Use a client to send a DELETE request to the `/delete_data/1` endpoint with the index of the dice roll you want to delete (e.g. `/delete_data/1`).

Note: You can test the API using a client like Postman or cURL.







# Weighted Dice
## Description for Weighted Dice

In this weighted dice code defines a class named `Dice` that simulates rolling a dice with a specified number of sides and weights. The `__init__` method initializes the instance variables `dice`, `sides`, and `weights`. The `roll` method rolls the dice and returns a list of the results. The code also includes an example of creating an instance of the `Dice` class with a weighted 6-sided die where the first face has a 50% chance of being rolled and the remaining faces have an equal chance of being rolled, and rolling the die 10 times. But you can change Rolling die 20 times istead of 10 times.
## Demo for Weighted Dice

    for 10 times

    [4] [1] [2] [1] [1] [1] [3] [1] [1] [1] 

    for 20 times

    [1] [1] [1] [4] [2] [3] [1] [1] [1] [6] 
    [4] [4] [2] [3] [3] [6] [1] [1] [2] [1] 

you can dice as much as you want and can check the probability of dice. 
## Usage for Weighted Dice

This code defines a class `Dice` that can be used to create a die with a specific number of sides and rolls. The `weights` argument can be used to create a weighted die, where certain faces have a higher probability of being rolled than others.

Here's an example usage of this code:

```python
# Create a weighted 6-sided die where the first face has a 50% chance of being rolled
# and the remaining faces have an equal chance of being rolled
dice_object = Dice(dice=1, sides=6, weights=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1])

# Roll the die 10 times
for i in range(10):
    print(dice_object.roll(), end=" ")
```

Output:
```
[1] [1] [1] [1] [1] [1] [1] [1] [1] [1] 
``` 

In this example, a weighted 6-sided die is created with a 50% chance of rolling the first face and 10% chance of rolling each of the remaining faces. The `roll` method is then called 10 times to generate a list of random rolls, each containing a single value between 1 and 6.
