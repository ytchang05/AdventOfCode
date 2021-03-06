import os
import requests
import time
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from dotenv import dotenv_values
from pytz import timezone, utc


# Load cookies from .env
cookies: dict = dotenv_values(".env")


# Function to get current time EST
def est_now() -> datetime:
    return datetime.now(tz=utc).astimezone(timezone("US/Eastern"))


# Get current year, day (adding 3 hours for those running it before 12EST)
year, day = est_now().strftime("%Y"), (est_now() + timedelta(hours=3)).strftime("%-d")


# Create new folder for the day
if not os.path.exists(f"{year}/day{day}"):
    os.makedirs(f"{year}/day{day}/")


# Create new Python file for the day
with open(f"{year}/day{day}/day{day}.py", "w") as f, open("template.py") as template:
    f.write(template.read())


# Wait for midnight EST
while (now := est_now()).hour != 0:
    print(now)
    time.sleep(0.5)


# 12:00 AM EST!
print("Advent of Code started!")


# Download input txt file from AoC website
with open(f"{year}/day{day}/day{day}.txt", "w") as f:
    f.write(requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies).content.decode())


# Parse and download example input from AoC website
# Uses content of first <code> inside a <pre> (may be incorrect)
resp: requests.Response = requests.get(f"https://adventofcode.com/2021/day/{day}")
soup: BeautifulSoup = BeautifulSoup(resp.content.decode(), 'html.parser')
if example := soup.find("pre").code.contents[0]:
    with open(f"{year}/day{day}/day{day}_example.txt", "w") as f:
        f.write(example+"\n")
