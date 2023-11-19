# Tennis Scoreboard Product Requirements Document (PRD)

## Introduction

This document outlines the requirements for a digital tennis scoreboard system. It defines the system's functionality, including score tracking, tie-break handling, server indication, and remote control operation.

## Product Overview

The scoreboard is designed to provide a clear and interactive display of scores, game, set, and set histories during a tennis match. It should be controllable by players using a remote.

## Product Features

- **Score Display**: Use SVG for displaying scores in a visually clear manner.
- **Tie-Breaker Display**: Include a visual indicator for tie-breaks.
- **Server Indicator**: Display which player is serving.
- **Remote Control**: Allow score adjustments and match resets through a remote.

## Component Specifications

### ScoreKeeper

Responsible for managing the scores of the match.

- **Attributes:**
  - `scores`: A dictionary with player IDs as keys and scores as values.
- **Methods:**
  - `incrementScore(playerId)`: Increase the score for a player.
  - `decrementScore(playerId)`: Decrease the score for a player.

### TieBreakHandler

Inherits from ScoreKeeper, specialized for tie-break scenarios.

- **Attributes:**
  - Inherits `scores` from ScoreKeeper.
- **Methods:**
  - Overrides `incrementScore(playerId)`: Additionally checks for tie-break conditions.

### RemoteReceiver

Processes input from the remote control devices.

- **Methods:**
  - `receiveInput(input)`: Acts upon the signal from the remote control.

### DisplayManager

Manages the visual output of the scoreboard.

- **Methods:**
  - `updateScoreDisplay(scores)`: Updates the score display.
  - `updateServerIndicator(currentServerId)`: Updates the server indicator.
  - `showTieBreakIndicator(isActive)`: Displays or hides the tie-break indicator.

### MatchState

Keeps track of the overall state of the match, including who is serving and the history of scores.

- **Attributes:**
  - `currentServerId`: Stores the ID of the player currently serving.
  - `matchHistory`: A stack to keep the match snapshots for undoing scores.
- **Methods:**
  - `changeServer()`: Switch the current server.
  - `storeMatchState()`: Save the current state of the match.
  - `restorePreviousState()`: Revert to the previous state.

## User Interface

- **Remote Control**: Design the remote with three buttons: 'Score', 'Undo', and 'Reset Game'. Each button press sends a signal to the RemoteReceiver.
