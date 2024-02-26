# Triathlon Time Calculator**

This Python script calculates the total time taken for a triathlon 
based on the input of swimming, cycling, and running times in minutes. 
It then assigns awards according to the total time achieved.

## Description

This script is designed to help athletes calculate their total time for 
completing a triathlon, which includes swimming, cycling, and running 
events. By inputting the time taken for each event, the script computes
the total time and determines the level of achievement based on 
predefined qualifying criteria. This task is a practical exercise that 
demonstrates how to take user input, perform calculations, and use 
conditional statements to make decisions in Python programming. 
Understanding these concepts is essential for building interactive and 
dynamic applications.

## Table of Contents

1. [Installation](Installation)
2. [Usage](Usage)

## Installation

To use this script, follow these steps:

1. Ensure you have Python installed on your system. If not, download 
and install Python from [python.org](https://www.python.org/).
2. Download the [`award.py`](award.py) file from this repository.
3. Open a terminal or command prompt and navigate to the directory 
where the [`award.py`](award.py) file is located.
4. Run the script by typing `python award.py` and pressing Enter.

## Usage

Once the script is running, it will prompt you to enter the time taken 
for swimming, cycling, and running events, respectively. Input the time 
for each event in minutes when prompted. The script will then calculate 
the total time and determine the award level based on the total time 
achieved. The awards are as follows:

- Provincial Colors: Total time within qualifying time (0-100 minutes).
- Provincial Half Colors: Total time within 5 minutes of the qualifying
time (101-105 minutes).
- Provincial Scroll: Total time within 10 minutes of the qualifying 
time (106-110 minutes).
- No Award: Total time more than 10 minutes of the qualifying time.

The script will display the total time and the corresponding award 
received.
