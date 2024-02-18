#### System Instructions
- Develop a program to generate code based on user intent.
- Provide a comprehensive list of file paths needed for the program.
- Return filepaths as a Python list of strings without additional explanations.

#### User Request
- **Role**: Expert Tennis Scorekeeper with proficiency in JavaScript, HTML, CSS, Canvas, and SVG.

#### Application Description
- **Objective**: Create a JavaScript/HTML/CSS/Canvas app that functions as a tennis game scoreboard.
- **Design**: Scoreboard to resemble HUB75 LED Matrices.

#### Scoreboard Features
- Display current scores for Player 1 (top) and Player 2 (bottom) in large digits.
- Show smaller set scores for Player 1 and Player 2.
- Include an indicator for:
  - History of game and set scores.
  - Current server: A horizontal bar beside the game score.
  - Current set.
  - Current game.
  - Tie-breaker: A horizontal bar in the bottom right corner.
  - Fireworks display and blinking lights for the winner.
- Color Coding:
  - Player 1's score in Green.
  - Player 2's score in Red.

#### Player Remotes
- **Buttons**:
  - `Score`: Increments the scorer's points.
  - `Undo`: Reverts the last score increment.
  - `Reset`: Resets the entire game.

#### Technical Requirements
- Ensure compatibility with the Chrome browser.
- Avoid using `import` and `export` keywords in the code.