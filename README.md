# Advent of Code

This is my repository for the Advent of Code (https://adventofcode.com/), starting from 2021.


## File Structure
Inside each year folder, such as `2021/`, there are folders for each day's puzzles (`dayN`).
These contain 2 files each: `dayN.py` (my solutions w/ Python) and `dayN.txt` (input data).

## Day Initialization
A few minutes before 12:00 AM EST, run `initialize.py`.
The script creates the folder and Python file (from `template.py`) for the day. 
Then, it checks in 0.5s intervals for midnight, upon which it downloads the input file for the day to `dayN.txt` inside the proper folder.

The automatic input file downloading is made possible by the `session` cookie in AoC.
The cookie value can be found in the `Application` tab of Inspect Element, `Storage` > `Cookies` > `session`.
Create a `.env` file in the root project folder with content 
```
session=cookie_value_here
```

## Dependencies
The dependencies for this repository are saved in a `requirements.txt`.
Be sure to create a `venv` (I used Python `3.10.0`), activate it, and run
```
pip install -r requirements.txt
```
