# Peg Solitaire - AI Solver

This repository contains an AI solver and a playable web version for the classic solo board game **Peg Solitaire**. 

Currently, the project supports three board configurations:
* **English** (Standard 7x7)
* **Fireplace**
* **Diamond**

*More info about the game:* [Peg solitaire on Wikipedia](https://en.wikipedia.org/wiki/Peg_solitaire)  

## Play Online
You can play the game directly in your browser!  
**[Play Peg Solitaire](https://fanisbar.github.io/Peg_Solitaire_solver/)**  

## Run the AI Solver (Locally)
The Python solver uses search algorithms (like DFS) to find a winning sequence of moves and visualizes the solution step-by-step using `matplotlib`.

### Prerequisites
Make sure you have Python installed, along with the required libraries:
```bash
pip install matplotlib numpy
```

## Usage
Run the solver from the root of the repository by providing the board type as an argument:

```bash
python solver.py [english | diamond | fireplace]
```
or
```bash
python3 solver.py [english | diamond | fireplace]
```

*Example:* `python solver.py english`

## Troubleshooting (WSL Users)
If you are using Windows Subsystem for Linux (WSL) and the visualization window doesn't open or throws an error, try exporting the display before running the script:

```bash
export DISPLAY=:0
python solver.py english
```