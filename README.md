# Homework 2 (40 points)
Due Monday, September 20 at 11:59 PM


## Square Footage Calculator (30 points)

In this assignment, you will combine everything we have learned so far to create a square footage calculator for your home.

We will also use the `input()` function, which we did not have time to cover in the lecture. It is briefly described in the lecture slides and discussed in the book. To assist you, the initial `input` call is written for you in the homework template.

### Task
Write a program that calculates the total square footage of a house or apartment. The program must:

1. Ask the user how many rooms are in their house.
2. For each room, prompt the user for the width and length of each room.
3. Once every room has been covered, present the total square footage of the home.

Please write this calculator *twice*: once using iteration with a `for` loop, and once using recursion.

Write your iterative implementation with a `for` loop in `house_iterative.py`, and your recursive implementation in `house_recursive.py`.

Here is what interacting with your program should look like:

```
How many rooms are in your house? 3
Width of room 1: 10
Length of room 1: 10
Width of room 2: 14
Length of room 2: 9
Width of room 3: 22
Length of room 3: 12
Your home is 490 square feet
```

The tests (available in the Actions tab) will verify that `print()` and `input()` are being called the right number of times to produce the output shown above, and that the correct square footage is being calculated.

## Written Questions (10 points)

1. Discuss your implementations of the square footage calculator. In your opinion, which approach (recursion or a `for` loop) is the better method of solving this problem? Why? (4 points)
2. Draw a stack diagram of a hypothetical run of your recursive implementation in a 2-room house. (4 points)
3. In class, we discussed the built-in `math` Python module. Consult the Python documentation and find another module that looks interesting to you. Briefly describe what it is for and what kinds of functionality it provides (2 points).

## Rubric
* Iterative square footage calculator (15 points)
	- Usage of a `for` loop with the `range()` function (5 points)
	- Correct numbering of rooms and output (2 points)
	- Correct accumulation and output of square feet (5 points)
	- Comments (3 points)
* Recursive square footage calculator (15 points)
	- Recursive function structure with base case (5 points)
	- Correct numbering of rooms and output (2 points)
	- Correct accumulation and output of square feet (5 points)
	- Comments (3 points)
* Written questions (10 points)

## Submission

On Blackboard, please submit the following:

* A link to your repository
* Answers to the written questions