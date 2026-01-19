# Food Gobbler 🐍🍏

A simple, colorful **Snake Game** built with Python and **Tkinter**.  
Eat the green food, grow longer, and try not to hit the walls or yourself!

This project was created while learning Tkinter basics and object collision detection, heavily inspired by and with huge thanks to **Bro Code**'s excellent YouTube tutorial on building a Snake game.

## Features

- Classic snake gameplay
- Score tracking
- Smooth controls (arrow keys)
- Colorful snake & food
- Game over screen
- Restart button
- Centered window on screen

## Technologies Used

- Python 3
- Tkinter (built-in GUI library)

## How to Run

1. Make sure you have **Python 3** installed
2. Copy the entire code into a file named e.g. `food_gobbler.py`
3. Run the game:

```bash
python food_gobbler.py
# or
python3 food_gobbler.py


↑     - Move Up
↓     - Move Down
←     - Move Left
→     - Move Right
You cannot reverse direction directly into yourself (normal snake rules).

GAME_WIDTH    = 1250
GAME_HEIGHT   = 550
SPEED         = 80          # lower = faster
SPACE_SIZE    = 25
BODY_PARTS    = 3           # starting length
SNAKE_COLOUR  = "#EA13F1"   # bright pink/purple
FOOD_COLOUR   = "#0BEE57"   # neon green
BACKGROUND_COLOUR = "Black"

Special Thanks
Huge credit and thanks to Bro Code (www.youtube.com/brocode) for his clear, beginner-friendly Tkinter + Snake game tutorial that taught me:

How to use Canvas in Tkinter
Basic game loop with window.after()
Simple object collision detection
Creating and managing moving objects on canvas

→ Watch the original inspiration here: Bro Code - Python Snake Game Tutorial (search "bro code snake tkinter" on YouTube)
Have fun & happy snaking! 🐍✨
Feel free to modify colors, speed, size, add features, high scores, sounds, etc. Have fun experimenting!



Good luck and enjoy your snake adventure! 🚀 - Jman
