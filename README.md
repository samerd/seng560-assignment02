# SENG-560 - Programming Assignment #2

Course: [*SENG-560 Software Reuse*](https://www.coursicle.com/wvu/courses/SENG/560/)  
Instructor: [*Mr. Gregory Mundy*](https://www.statler.wvu.edu/faculty-staff/faculty/gregory-mundy)  
Student: *Samir Deeb*  
Date: *Nov 08, 2019*  

This project package has been developed as part of the assignment #2 of the course "SENG-560"

The objective of this assignment is to show how can we reuse components.
In this assignment I reused the python project [*seng560Calc*](https://github.com/jdc0051/seng560Calc)

The developed project is a simple calculator application that provides the following functionalities:

1. calculate binary operations such as 2 * 5.1
2. calculate unary operations such as V2 (square root of 2)
3. convert integers from/to the following formats: Binary, Octal, Decimal and Hexadecimal

## How to use this application
To run this application:

1. clone this repository.
1. clone the reused repository: [seng560Calc](https://github.com/jdc0051/seng560Calc)
1. make sure the reused repository is in your PYTHONPATH
1. run python [calcapp.py](./src/pycalc/calcapp.py)

## Usage

when running the application the following menu is displayed:

```
1: Calculate
2: Convert
q: Quit
Choice:
```

### Calculate sub-menu

The user will be prompted to enter a binary or unary operation question

```
Please enter a question in one of the following formats:
    1- op1 operator op2
    2- operator op
Where operator can be: +,-,*,/,^,V
   ^ denotes power and V denotes square root
Question: 
```

the application will parse the question and print the result or an error

### Convert sub-menu

The user will be prompted to enter input format:

```
Please enter input format:
b: Binary
o: Octal
d: Decimal
h: Hexadecimal
Choice:
```

Then the output format.

```
Please enter output format:
b: Binary
o: Octal
d: Decimal
h: Hexadecimal
Choice:
```

And the number to be converted:

```
Please enter number to convert:
```

the application will convert the given number from the input format to the output format.

# Reuse experience

In this project, we used black-box reuse, as the reused library has been used as is with out any modification.

## Limitation

Although the reuse was very simple and straight-forward, the resued library does not handle the following cases:

1. division by zero
2. squareroot or fractional powers of negative numbers

The error displayed in these two cases does not reflect the real error.

to overcome these issues we can do the following:

1. modify the reused library (whitebox reuse)
2. let our application catch these errors before calling the reused library, which will add ore complexity to the application. we can also use some decorator of these functions.

neither one of these two options was used, and it was left as is.