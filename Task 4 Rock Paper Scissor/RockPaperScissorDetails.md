<h2>Task 4: Rock Paper Scissor</h2>

The provided Python code is a command-line implementation of the Rock-Paper-Scissors game. It allows a player to play multiple rounds against the computer, keeps track of scores, and determines the final winner. Here’s a brief description:

---

<h3> Global Variables </h3>


- <b>PlayerScore:</b> Tracks the player's score.
- <b>ComputerScore:</b> Tracks the computer's score.
- <b>choices:</b> Dictionary mapping choices to their string representations.
- <b>n:</b> Counter for the number of rounds played.

---

<h3> Functions </h3>

<h3> instruction() </h3>

- Prints the rules of the game.

<h3> choicesAvailable() </h3>

- Prints the available choices (Rock, Paper, Scissors).

<h3> winner(PlayerChoice) </h3>

- Determines the winner of a round.
- Updates and prints the scores.

<h3> game() </h3>

- Main game loop where the player makes a choice and the result is shown.
- Prompts the player to continue or end the game.
- Displays final scores and the overall winner when the player exits.

---

<h3> Execution </h3>

- The program starts by printing the game rules using instruction().
- Then it enters the main game loop in game(), where it repeatedly:
- Displays available choices.
- Prompts the player for their choice.
- Determines the round winner.
- Updates and prints the scores.
- Asks the player if they want to play another round.
- Displays the final result when the player decides to stop.
- The program ensures a fun and interactive experience by continuously updating the player on the game’s progress and final outcome.
