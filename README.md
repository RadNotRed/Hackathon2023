# 2023 Hackathon

This is just a school wide event that we do every year and I decided to participate this year.  
Projects 5, 6, 8, 9, and 10 were made by me.  
Projects 1, 2, 3, 4, and 7 were made by my teammate.  

# Project 1 - List Manipulation
## Create a python program to complete the following tasks:
```
1.  Write a function to fill a list of 50 elements with random integers from 1 to 100.
2.  Write a funciton to determine the smallest value in the list.
3.  Write a function to remove any duplicate values within the list.
4.  Write a function to put the list in order from greatest to smallest.
```

# Project 2 - Swap Case
## Create a python project that will complete the following tasks:

Your project will ask for a string input, and then the project will swap the case of the letters entered.
```
For Example: 
input: Today is Tomorrow's Yesterday.
output: tODAY IS tOMORROW'S yESTERDAY.
```

# Project 3 - Leap Year Write up

An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:
```
1.  The year can be evenly divided by 4, is a leap year, unless:
2.  The year can be evenly divided by 100, it is NOT a leap year, unless:
3.  The year is also evenly divisible by 400. Then it is a leap year.
```
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
### Task:

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Project 4 - Dictionaries
## Senerio:

Your team was hired by Merriam-Webster, Inc. who are known for publishing dictionaries. They are branching out and want to enter the world of translating english to another language.
## Task:

Your team is tasked to create a dictionary of 25 words in python. The dictionary will have the 'keyword' be in english, and the 'value' will be in a foreign language of your team's choice. After creating the dictionary. The user of the program will enter an english phrase, and the program will display the phrase correctly translated into the other language, using the python dictionairy your team created.

FYI: Dr. Ahmed and the rest of the judges are looking for a dictionary to learn "teenager slang."


# Project 5 - Mad Libs
## Task:

Create a mad libs program. Where the user of the program has to pick from one out of five different madlibs, and follow the instructions for the selected madlibs that the user picks. Once the user has filled in all the appropiate words, the program will then dispaly their creation.

Use the link below for mab lib ideas, or create your own. If you create your own, you have to have a minimum of 5 inputs for the madlib.

https://www.thepaintedturtle.org/sites/main/files/file-attachments/mad_libs.pdf

# Project 6 - GPA Calculator
## Scenario:

The quarter has just ended and you get your report card. There is one major problem. Your report card is missing your final average for the quarter. Create a program that asks a user to input their final quarter grades for a class and returns their final unweighted and weighted grade point averages for the quarter.
Key Requirements:
```
 1. Must ask user for 8 class grades
 2. At least one class must be honors
 3. At least one class must be AP
 4. Must provide user with weighted GPA
 5. Must provide user with unweighted GPA
```
### Notes:

Reminder! Honors Classes get a 5% weight and AP Classes get a 10% weight.

# Project 7 - Nested List

Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
## Example

records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]] The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that score: ["beta", "alpha"]. Ordered alphabetically, the names are printed as:
```
alpha
beta
```
### Input Format
```
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.
```
## Constraints
```
1. There will always be one or more students having the second lowest grade.
2. 2 <= N <= 5
```
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
### Sample Input 0
```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```
### Sample Output 0
```
Berry
Harry
```
### Explanation 0

There are students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

# Project 8 - Hangman
## Tasks:

Your team will create a game of Hangman.
### Requirements:
```
1.  Have a list of 10 phrases for the user to guess from. 
2.  At start up: randomly select one of the phrases, and display the appropiate amount of dashes.
3.  Using text art create a "body" so the user can keep track of how many more guesses they have. 
4.  Display the phrase filled in along with the amount of lives left each round is played. The player will start with 9 lives. 
5.  Reset the game with a new phrase, after the word was correctly entered or the "body" was completly drawn.
```

# Project 9 - Currency Convertor
## Task:

Create a program that allows the user to convert the american dollar into a preprogramed currency.
### Requirements:
```
  1. Create a dictionary with 5 different currencies. 
  2. Create a function that converts to the currencies to the nearest cent. 
  3. Pass at least two variables into the function.
```

# Project 10 - Typing Game
## Senerio:

You and your friends want to see who can type the fastest with out any errors.
Tasks:

Create a program that will do the following:
```
1. Record the users, name and score for each time they play.
2. Time how fast the user enters the phrase.
3. Determine how many errors the user makes when entering the phrase.
4. Have 5 unique phrases the computer uses to test the user's speed and accuracy. 
5. Display a scoreboard with the 3 top times.
```
