"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""


def stupidPassword(n: int, l: int):
    result = []

    # first l lowercase letters
    letters = [chr(ord('a') + i) for i in range(l)]

    for d1 in range(1, n + 1):
        for d2 in range(1, n + 1):
            for c1 in letters:
                for c2 in letters:
                    for d3 in range(1, n + 1):
                        if d3 > d1 and d3 > d2:
                            result.append(f"{d1}{d2}{c1}{c2}{d3}")

    return result

