# Monty Hall Simulator

Challenge resolved with the intent of training python.
[link to the challenge page](https://www.reddit.com/r/dailyprogrammer/comments/n94io8/20210510_challenge_389_easy_the_monty_hall_problem/)

## Table of Contents

- [Monty Hall Simulator](#monty-hall-simulator)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [The Problem](#the-problem)
  - [The players](#the-players)
    - [The user's choices](#the-users-choices)

***

## Introduction

The [program](monty_hall_simulator.py) was made with the intent of simulating the [Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem).

Programming language used: Python

Program date: August 2021.

Made by: Ana C Maia Atala. :e-mail: @ ana.atala@unemat.br

## The Problem

The Monty Hall Problem is a probability puzzle as follows:

```txt
Suppose you're on a game show, and you're giving the choice of three doors: Behind one door is a car, behind the others, goats.
You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat,
he then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
```

The idea of the program is to simulate 1000 rounds of the monty hall problem for different players, each player will have a different strategy. and their result will be shown as their win percentage.

## The players

The program has the following default players, which will all play 1000 rounds each, plus the user's choices, who will also play the game 1000 times:

>**Alice** chooses door #1 in step 2, and always sticks with door #1 in step 4.
**Bob** chooses door #1 in step 2, and always switches to the other closed door in step 4.
**Carol** chooses randomly from the available options in both step 2 and step 4.
**Dave** chooses randomly in step 2, and always sticks with his door in step 4.
**Erin** chooses randomly in step 2, and always switches in step 4.
**Frank** chooses door #1 in step 2, and switches to door #2 if available in step 4. If door #2 is not available because it was opened, then he stays with door #1.
**Gina** always uses either Alice's or Bob's strategy. She remembers whether her previous strategy worked and changes it accordingly. On her first game, she uses Alice's strategy. Thereafter, if she won the previous game, then she sticks with the same strategy as the previous game. If she lost the previous game, then she switches (Alice to Bob or Bob to Alice).
**User** which the choices the user will input.

### The user's choices

the user will have to input *3* datas:

1. Their name, it can be anything.
2. Their **#1** choice, it can be any of the following (without the ''):
    - '1' for door #1.
    - '2' for door #2.
    - '3' for door #3.
    - 'r' for a random door.
3. their **#2** choice, it can be any of the following (without the ''):
    - '1' for door #1 (defaults to the choice #1 if not available).
    - '2' for door #2 (defaults to the choice #1 if not available).
    - '3' for door #3 (defaults to the choice #1 if not available).
    - 'r' for a random door.
    - 'switch' to switch your door from the #1 choice for the other available option.
    - 'stay' to stay with the same door chosen in the #1 choice.
