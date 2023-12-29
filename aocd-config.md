# How to Configure advent-of-code-data

This is a small tutorial to get the module set up for this repository. If you want more customization or options in setting it up, [here is a link to the docs](https://pypi.org/project/advent-of-code-data/) that goes more in depth on the module.

advent-of-code-data is a python module that allows you to recieve **your** Advent of Code data without the hassle of recieving it yourself. However there are a few steps involved for it to work correctly. This document should help you get advent-of-code-data working properly for you!

For the module to work, you must capture the session cookie from the [Advent of Code](https://adventofcode.com/) website and store the cookie on your local machine

#### Step 1
Sign in to [Advent of Code](https://adventofcode.com/)

#### Step 2
Inspect the page in your browser and go to the *network* tab (you may need to refresh if nothing is there)

#### Step 3
click on the adventofcode.com request. Under the headers tab locate the *Headers* tab.

#### Step 4
In the Headers tab find the *Request Headers* and open it if closed

#### Step 5
Look for cookie, and your cookie will look like this: session=\<this is your cookie\>;
Copy and paste the cookie somewhere for later or keep the browser open.

#### Step 6
On your machine, in the terminal enter the following commands

```sh
cd ~
mkdir .config/
cd .config
mkdir aocd
cd aocd
nano token
```

You will now be in a text editor where you will paste your cookie. save and exit the file.

#### Step 7
Once your cookie is saved on your machine you need to add a path variable to access it. 

In your terminal, enter the follwing

```sh
export AOCD_DIR=~/.config/aocd/token
```

You should be set up to retrieve your puzzle input and submit your solutions. 