# Primeiro torneio de programação SECOMP 2021

## Table of Content

- [Primeiro torneio de programação SECOMP 2021](#primeiro-torneio-de-programação-secomp-2021)
  - [Table of Content](#table-of-content)
  - [Introdução](#introdução)
  - [Os problemas](#os-problemas)
    - [URI_1247](#uri_1247)
    - [URI_1278](#uri_1278)
    - [URI_1332](#uri_1332)
    - [URI_1429](#uri_1429)

## Introdução

O torneio occoreu na plataforma [URI online Judge](https://www.urionlinejudge.com.br) com os exercicios sendo selecionados do banco de dados deles.

Programming language used: C & Python

Program date: August 2021.

Made by: Ana C Maia Atala. :e-mail: @ ana.atala@unemat.br

## Os problemas

### URI_1247

"Stop thief! Stop thief!" Stole the purse of an innocent lady who was walking on the beach and Nlogonia thief fled toward the sea. His plan seems obvious: he intends to take a boat and escape!

The fugitive, who by now is aboard their vessel leakage, intends to follow the coast perpendicularly toward the limit of international waters, which is 12 nautical miles away, where will be saved from local authorities. Your boat can travel that distance at a constant speed of VF us.

The Coast Guard intends to intercept him, and your boat has a constant speed of VG us. Assuming both boats departing the coast at exactly the same instant, with a distance of D nautical miles between them, can be possible that the Coast Guard reach the thief before the limit of international waters?

Assume the coast of Nlogonia is perfectly straight and the sea calm enough, to allow a trajectory so as retilíınea the coast.

**Input**
The input consists of several test cases. Each test case is described in a line containing three integers, D (1 ≤ D ≤ 100), VF (1 ≤ VF ≤ 100) and VG (1 ≤ VG ≤ 100), indicating the initial distance between the fugitive and the Coast Guard, the runaway boat speed and the Coast Guard boat speed.

**Output**
For each test case print a line containing 'S' if the Coast Guard can reach the fugitive before he exceeds the limit of international waters or 'N' otherwise.

Sample Input | Sample Output
--- | ---
5 1 12 | S
12 10 7 | N
12 9 10 | N
10 5 5 | N

### URI_1278

We have some texts and we want to right justify them, that is, align them to the right. Create a program that reads a text, formats it right justifies all of its lines, printing them in the same order as they appear in the input.

**Input**
The input contains several test cases. The first line of a test case will contain an integer N (1 ≤ N ≤ 100) indicating the number of lines that form the text. Each of the following N lines will contain a text, composed of 1 to 50 uppercase letters (‘A’-‘Z’) or spaces (‘ ’). All text lines will contain at least one letter. There may be more than one space character between words. Also, there may be leading and trailing spaces in the input lines. The end of input is indicated by N = 0.

**Output**
For each test case print the text lines with a single space character between words, and padded on the left with space characters so that all the lines will have the same length as the longest line existing in that text. Print an empty line between all the test cases. There must be no trailing spaces printed out, and you should discard any unnecessary leading spaces, so that at least one line on every text starts with a letter.

Sample Input

```txt
3
     ROMEO      AND
      JULIET WERE  
        IN LOVE    
4
WHO
ELSE
LOVES
STAIRS
3
A TEXT CAN BE JUSTIFIED
ON   BOTH   SIDES    OR
JUST   TO   THE   RIGHT
0
```

Sample Output

```txt
  ROMEO AND
JULIET WERE
    IN LOVE

   WHO
  ELSE
 LOVES
STAIRS

A TEXT CAN BE JUSTIFIED
       ON BOTH SIDES OR
      JUST TO THE RIGHT
```

### URI_1332

Your little brother has just learnt to write one, two and three, in English. He has written a lot of those words in a paper, your task is to recognize them. Note that your little brother is only a child, so he may make small mistakes: for each word, there might be at most one wrong letter. The word length is always correct. It is guaranteed that each letter he wrote is in lower-case, and each word he wrote has a unique interpretation.

**Input**
The first line contains the number of words that your little brother has written. Each of the following lines contains a single word with all letters in lower-case. The words satisfy the constraints above: at most one letter might be wrong, but the word length is always correct. There will be at most 1000 words in the input.

**Output**
For each test case, print the numerical value of the word.

Sample Input | Sample Output
--- | ---
3 | 1
owe | 2
too | 3
theee | |

### URI_1429

Mathew, an engineering freshman, is developing an original positional notation for representing integer numbers. He called it “A Curious Method” (ACM for short). The ACM notation uses the same digits as the decimal notation, i.e., 0 through 9.

To convert a number A from ACM to decimal notation you must add k terms, where k is the number of digits of A (in the ACM notation). The value of the i-th term, corresponding the i-th digit ai, counting from right to left, is ai × i!. For instance 719 ACM is equivalent to 5310, since 7 × 3! + 1 × 2! + 9 × 1! = 53.

Mathew has just begun studying number theory, and probably does not know which properties a numbering system should have, but at the moment he is only interested in converting a number from ACM to decimal. Could you help him?

**Input**
Each test case is given in a single line that contains a non-empty string of at most 5 digits, representing a number in ACM notation. The string does not have leading zeros.

The last test case is followed by a line containing one zero.

**Output**
For each test case output a single line containing the decimal representation of the corresponding ACM number.

Sample Input | Sample Output
--- | ---
719 | 53
1 | 1
15 | 7
110 | 8
102 | 8
0 | |
