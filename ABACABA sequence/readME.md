# The ABACABA Sequence

## Table of Content

- [The ABACABA Sequence](#the-abacaba-sequence)
  - [Table of Content](#table-of-content)
  - [Introduction](#introduction)
  - [The Problem](#the-problem)

## Introduction

The [program](abacaba.py) was made with the intent of training string use in python

Programming language used: Python

Program date: August 2021.

Made by: Ana C Maia Atala. :e-mail: @ ana.atala@unemat.br

## The Problem

The ABACABA sequence is defined as follows: the first iteration is the first letter of the alphabet ```a```. To form the second iteration, you take the second letter ```b``` and put the first iteration (just a in this case) before and after it, to get ```aba```. For each subsequent iteration, place a copy of the previous iteration on either side of the next letter of the alphabet.
The first 5 interactions of the sequence:

```txt
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
```

The 26th and final iteration (i.e. the one that adds the ```z```) is 67,108,863 characters long. If you use one byte for each character, this takes up just under 64 megabytes of space.
