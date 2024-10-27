# My Code Challenge Submissions

I love doing puzzles and solving problems. I also love coding! I decided to put this repository together to show off my submissions to LeetCode and Advent of Code or any other cool problems solved with code!

### About AI

With tools such as GitHub Copilot and ChatGPT, coding problems and puzzles become trivial. I will not be using any Artificial Intelligent assistants for any of the problems solved here. It is more fun this way :)

### Getting Started (Linux/MacOS)
Clone repository to your machine
```sh
cd /home/projects
git clone git@github.com:streebs/strebe-leet.git
cd strebe-leet
```

Set up Python virtual environment 
```sh
python -m venv .venv
source .venv/bin/activate
```

Once the virtual enviroment is set up, install packages from requirements.txt
```sh
pip install -r requirements.txt
```

remember you can use the following to exit venv
```sh
deactivate
```

If you are using Windows, check this out: https://frankcorso.dev/setting-up-python-environment-venv-requirements.html


# Advent of Code Submissions
If you would like to verify the results of my AoC submissions, check out [aocd-config.md](https://github.com/streebs/strebe-leet/blob/main/aocd-config.md). 
To run the submissions just run a python file in aoc2023/. For example:

```sh
python aoc2023/day4.py
```

optionally there is a '-t' flag for testing submissions

# Project Euler

My solutions for [Project Euler](https://projecteuler.net/about) problems is located in `euler/`. Much Thought goes into these problems and I am making an effort to document my thought process in the comments at the top of each file. I find these problems really fun! I also have started development of a library called `smath`. I have included it in the `euler/` directory as it is a major work in progress. It is there to code highly reusable algorithms related to math. More to come! :) 

