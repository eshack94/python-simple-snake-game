# Simple Python Snake Game

This project contains no practical purpose, other than for me to learn about
the Pygame library through trial-and-error and personal experimentation.

**NOTE**: This is incomplete, and has some definite rough edges. I plan to
refine it in my free time when I get around to it. This is just a "for-fun"
project, and serves no practical purpose.

## TODO:
* Add score counter (10 points per "dot" collected?)
* Reduce snake speed
* Make the game paused by default, requiring movement key to begin.
* Increase default canvas dimensions
* Fix the "GAME OVER" text overlay.
    * Make text smaller and better aligned; change font.
* Add "R" option to retry to complement the current "Q" option.
    * Currently, you must hit "Q", then restart by launching the program again.
* Pick a better color palette.
* Add borders and more immersive shapes/textures.


## Usage

Make sure your system is running Python 3, then run:

```bash
pip3 install -r requirements.txt
python3 simple_snake_game.py
```

You can move with your keyboard's arrow keys, or with WASD keys. Note that
currently, the snake starts moving immediately, so you'll have to instantly
change directions to avoid hitting a wall. I plan to fix this so that a key
must first be pressed to begin the game.
