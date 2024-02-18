# Tennis Scoreboard App Development Plan

## Overview
The Tennis Scoreboard App will consist of several files that handle different aspects of the application such as the user interface, game logic, and event handling. Below is the structure of the app and the details of each file that we will generate.

## File Structure

### `index.html`
- **Purpose**: Serves as the entry point of the application and contains the markup for the scoreboard.
- **DOM Element IDs**:
  - `scoreboardCanvas`: The canvas element for the LED Matrix display.
  - `player1Score`: Element to display Player 1's score.
  - `player2Score`: Element to display Player 2's score.
  - `serverIndicator`: Element to show the current server.
  - `setGameInfo`: Element to show the current set and game number.
  - `tieBreakerIndicator`: Element to show if a tie-breaker is in play.

### `styles.css`
- **Purpose**: Provides styling for the HTML elements.
- **CSS Classes**:
  - `.playerScore`: Styles for the player score elements.
  - `.serverIndicator`: Styles for the server indicator element.
  - `.setGameInfo`: Styles for the set and game information element.
  - `.tieBreaker`: Styles for the tie-breaker indicator.

### `app.js`
- **Purpose**: Contains the main application logic for the scoreboard.
- **Exports**:
  - `updateScoreDisplay`: Function to refresh the scoreboard display.
  - `changeServer`: Function to switch the current server.
  - `incrementScore`: Function to increase a player's score.
  - `resetScore`: Function to reset scores for a new game or set.
  - `handleRemoteInput`: Function to process remote control actions.
  - `undoLastAction`: Function to undo the last scoring action.
- **Variables**:
  - `playerScores`: Object holding the current scores of both players.
  - `setScores`: Object holding the scores of the sets.
  - `currentServer`: Variable indicating the current server.
  - `currentSet`: Variable indicating the current set number.
  - `currentGame`: Variable indicating the current game number.
  - `tieBreaker`: Boolean indicating if a tie-breaker is active.
- **Message Names**:
  - `ScoreUpdate`: Broadcasted when the score is updated.
  - `ServerChange`: Broadcasted when the server changes.
  - `GameReset`: Broadcasted when the game or set is reset.
  - `UndoAction`: Broadcasted when an action is undone.

### `remote.js`
- **Purpose**: Handles the remote control inputs and triggers scoreboard updates.
- **Exports**:
  - `remoteControlListener`: Function to listen to remote control inputs.
- **Variables**:
  - `lastAction`: Stores the last action taken for the undo feature.

### `canvas.js`
- **Purpose**: Manages the canvas drawing for the LED Matrix display.
- **Exports**:
  - `drawScoreboard`: Function to draw the scoreboard on the canvas.
- **Variables**:
  - `canvasContext`: The context of the canvas for drawing operations.
  - `scoreBoardMatrix`: Data structure to represent the LED Matrix.

### `data.js`
- **Purpose**: Defines the data schemas and manages the state of the game.
- **Exports**:
  - `ScoreData`: Schema for storing score data.
  - `GameStatus`: Schema for storing current game status.
- **Variables**:
  - `gameData`: Object that holds the current state of the game.

## Summary
The app will be structured into separate files for markup (`index.html`), styling (`styles.css`), application logic (`app.js`), remote input handling (`remote.js`), canvas operations (`canvas.js`), and data management (`data.js`). Each file will have specific responsibilities and export certain variables and functions to maintain a modular and organized codebase.
