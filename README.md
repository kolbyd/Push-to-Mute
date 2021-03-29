# Push to Mute

Written in [Python](https://www.python.org/), the title says it all. While pushing a button, it mutes your
headphones. When that button is released, it unmutes.

Uses code from [Paradoxis](https://github.com/Paradoxis/Windows-Sound-Manager) (for managing sound) and 
from [LucasG](https://github.com/lucasg) (manages sound inputs). Go check them out.

## Usage

1. Run `pip install -r requirements.txt`
1. Edit `main.py` and set the key_to_mute variable to your desired key
1. Run `main.py`

That's it! Press the key, it will mute. Release the key, it will unmute. NOTE: First time hitting the key
will set your volume to 100%, which could probably be improved by using a different package.

## Contribution Guide

I had no specific goal for this project other than getting the push to mute to work. Although, it can 
be improved.

While I prefer PRs over issues, I will accept either. In the case of a pull request, please comment your
code and what you fixed.

