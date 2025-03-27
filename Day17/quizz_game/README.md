# Quiz GAME

<strong>Developer: Daniel Alejandro Castillo Martín</strong>

---
<p style="text-align:justify;">This folder contains all of the scripts and resources made for the Quiz Game project, which was part of Day 17 of the <em><strong>Udemy's 100 Days of Code: The Complete Python Pro Bootcamp</strong></em>, developed and taught by Dr. Angela Yu. 

</p>

<b>About this project:</b>

- The program can be executed in the <em>main.py</em> file, which executes the main program functions, which can be found under the *src* folder, in the *question_model.py* and *quiz_brain.py* files.
- The *src* folder contains every essential function and module for the program's main logic.
    - The *question_model.py* file contains the skeleton for each question in the game, with the attributes text (question) and answer (correct answer). It is later used in the *main.py* file to store the data as *Question* generated objects.
- The *quiz_brain* contains the class for the game's essential functions, so it can work dynamically in the *main.py*.
- The *data* folder contains a .txt with the link for the *Open Trivia Database*. Dr. Angela Yu designed the game's data you can get more quizzes via this database's API to change the inputs for this game as you wish by just copying the response JSON file into *question_data* variable, located in *data/game_data.py*. Then, you would need to keep just the value for *results* key in the JSON file (question dictionary list) and change the name of the corresponding keys in the *main.py*.

> <em>Note: The status of the current Bootcamp is still <b>In Progress</b>, so new files and projects will be added constantly into the main repository.</em>