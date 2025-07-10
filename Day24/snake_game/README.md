# Snake Game Project

**Developer:** Daniel Alejandro Castillo Martín

---

This folder contains all the scripts and resources created for the Snake Game Project (you might remember playing this game in your phone if you had one in the early 2000's), part of **Days 20 and 21** of _Udemy’s 100 Days of Code: The Complete Python Pro Bootcamp_, developed and taught by Dr. Angela Yu. The game has been updated in **Day 24** by adding the *Highest Score* tracking feature.

## About this project

- The program can be executed by running the `main.py` file, which calls the main program functions located in the `src` folder, and pops up the game using a Screen object from the Turtle module.
- The game tracks your current score and the highest score ever achieved. The highest score is saved in a `data.txt` file in the project directory, and is automatically loaded and updated each time you play.
  - `src/snake`: Contains all functions that make the snake object.
  - `src/food`: Contains all functions related to the "food" that the snake will be eating each time you score a point.
  - `src/scoreboard`: Contains all functions related to the scoreboard that is displayed on the game screen, updating it every time you score one point, or "eat food", and handling the saving/loading of the high score from `data.txt`.

> **Note:** The status of the current Bootcamp is still **In Progress**, so new files and projects will be added regularly to the main repository.