#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:11:39 2020

@author: owner
"""

#%%
def areatriangle(b,h):
    """Computes the area of a triangle of given base and height"""
    area = 0.5*b*h
    print("The area of a triangle of base", b, "and height", h, "is", area)
    
#%%
name = "His name is Conan O'Brien"
cat = 'My cat is named "Butters"'
print(name)
print(cat)
#%%
def fahrenheit_to_celsius(temp):
    """Converts Fahrenheit temperature to Celsius.
    Formula is 5/9 of temp minus 32."""
    # Note that this line is not executed.
    # end = '' keeps print from starting a new line.
    newTemp = 5 * (temp - 32)/9
    print("The Fahrenheit temperature",temp,"is equivalent to",newTemp,end='')
    print("degrees Celsius")
#%%
def celsius_to_fahrenheit(temp):
    """Converts Celsius temperature to Fahrenheit.
    Formula is 9/5 of temp plus 32."""
    newTemp = (9/5) * temp + 32
    print("The Celsius temperature", temp,"is equivalent to", newTemp, end='')
    print(" degrees Fahrenheit")
#%%
# The following will test the above function
celsius_to_fahrenheit(100)
celsius_to_fahrenheit(0)
celsius_to_fahrenheit(50)
#%%
def name():
    """ Input your name and where you live, combine to strings and print."""
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    town = input("Enter the town/city you live in: ")
    county = input("Enter the county you live in: ")
    fullname = fname + " " + lname
    address = town + ", " + county
    
    print("Your name is: ", fullname)
    print("You live in: ", address)
#%%
"""
The following function uses an 'if' statement. Note that the indentation marks
scope of the 'if', 'elif','else' actions.
"""
def area(type_,x):
    """Computes the area of a square or circle. 
    type_ must be the string "circle" or the string "square".
    We use type_ here, because type is a Python keyword."""
    if type_ == "circle":
        area = 3.14 * x**2
        print(area)
    elif type_ == "square":
        area = x**2
        print(area)
    else:
        print("I don't know that one")
#%%
def absolutevalue(num):
    """ Computes the absolute value of a number."""
    if num > 0:
        print("The absolute value of", num,"is", num)
    elif num < 0 :
        numpos = -1 * num
        print("The absolute value of", num, "is", numpos)
    else:
        print("The absolute value of", num, "is 0")
#%%
def inches_to_feet(inches):
    """converts inches to feet and inches"""
    feet = inches // 12
    extra_inches = inches % 12
    print(inches,"inches is", feet,"feet and", extra_inches,"inches")
#%%
def cheer():
    """Prints 2 4 6 8, who do we appreciate .... Note that everything in 
    the while loop is indented. The first line not indented is the first 
    line following the while loop."""
    ct = 2
    while ct <= 8:
        print(ct, end=' ') #end=' ' keeps from starting a new line.
        ct = ct + 2
    print()                # now we'll start a new line.
    print("Who do we appreciate?")
    print("COURSERA")
#%%
def count_down():
    """Starts a countdown from 10 to rocket launch."""
    ct = 10
    while ct > 0:
        print(ct, end=' ') #end=' ' keeps from starting a new line.
        ct = ct - 1
    print()                #starts a new line
    print("BLASTOFF!")
#%%    
def cheer2():
    """Same as cheer, but uses a for loop and range()
    range uses a start number, a stop number and a step size"""
    for ct in range(2,9,2):
        print(ct, end=' ')
    print()
    print("Who do we appreciate?")
    print("COURSERA!")
#%%
def countdown1():
    """Starts a countdown from 10 to rocket launch using 'for' loop."""
    for ct in range(10,0,-1):
        print(ct, end=' ')
    print()
    print("BLASTOFF!")
#%%
""" Find and correct all the errors in the following Python functions.
    To run one, click in the cell (between two lines) and type Ctrl-Enter for
    Windows or Command-Return for a Mac.  Then enter the name of the function
    into the IPython console.  For example, to run the first one enter
    print_phrase() and press return.
"""
""" 
Exercise 1 
"""
#%%
def print_phrase():
    phrase = "Now is the time"
    print(phrase)
#%%
""" 
Exercise 2
"""
#%%
def favorite_sport():
    favorite = input("Your favorite sport is: ")
    print("Your favorite sport is",favorite)
#%%
""" 
Exercise 3 
"""
#%%
def username():
    yourname = input("Enter your first name: ")
    print("Your name is",yourname)
#%%
"""
Exercise 4
"""
#%%
def compare_numbers(x,y):
    if x == y:
        print("they are equal")
    else:
        print(x, "and", y, "are not equal")
#%%
        """
Exercise 5
"""
#%%
def count_by_5():
    """ Count from 5 to 100 in steps of 5 """
    """ 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 """
    print('Counting from 5 through 100 in steps of 5')
    ct = 5
    while ct <= 100:
        print(ct, end = " ")
        ct = ct + 5
#%%    