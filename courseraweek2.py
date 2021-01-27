#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:19:49 2020

@author: owner
"""

"""Let's define a list, I'll call it lis and we'll do things with it to 
illustrate accessing items in a list."""
#%%
lis = ["a","b","c","d","e","f"]
#%%
"""
lis[0] is the first element of the list. (index is 0)
lis[1] is the second element of the list and so on. (index is 1)
The length of the list is len(lis) and is the number of items in the list.
lis[-1] is the last item in the list.
lis[2:4] will list items 2 and 3 (but not 4).
lis[:4] will list items 0,1,2,3 (but not 4); that is all items up to 4.
lis[3:] will list all items starting with item 3.
lis.append["g"] will append "g" onto the end of the list.
"a" in lis    #running this statement will return True.
"r" in lis    #running this statement will return False.
Everything in Python is an object, whether it is a variable like x or a list
like lis. Objects have methods indicated by the dot. So .append() is a method 
of the list object. Will see more of this.
"""

"""
Here is an example function using a list. We pass in a list of items and it
checks for certain animals or flowers in the list.
"""
#%%
def who_is_there(lis):
    if "bear" in lis:
        print("There's a bear.")
    if "lion" in lis:
        print("There's a lion.")
    if "daisy" in lis or "iris" in lis:
        print("There are flowers.")
    if "donkey" in lis:
        print("There's a donkey.")
    if "horse" not in lis:
        print("There is no horse in the list.")
    print("The list has", len(lis),"items.")
#%%
"""
The following function illustrates using lists in 'for' loops. Note that the
loop variable 'let' steps through the list, alist, taking the value of each
of its items in turn.
"""
#%%
lis = ["a","b","c","d","e","f"]
lis1 = ["a","b","a","r","c","a","a"]
#%%
def count_a(alist):
    ct = 0
    for let in alist:
        if let == 'a':
            ct = ct + 1
    print("There are", ct, "letter a's in the list.")
#%%
def average(numlis):
    """ Function to compute the average of the numbers in a list."""
    my_sum = 0    #initiate the sum of the values in the list
    for num in numlis:
        my_sum = my_sum + num
        print(num)
    av = my_sum/len(numlis)
    print("The average is", av, "and its count is", len(numlis))
#%%
nlis = [2,4,8,105,210,-3,47,8,33,1] #average should be 41.5
rlis = [3.14, 7.26, -4.76, 0, 8.24, 9.1, -100.7, 4] #average is -9.215
#%%
newEngland = ["Maine", "New Hampshire", "Vermont", "Rhode Island", 
              "Massachusetts", "Connecticut"]
def for_state(slis):
    for state in slis:
        print(state)
#%%
letter_list = ['a', 'b', 'c']
cap_list = ['A','B','C','D']
misc_list = ['ball', 3.14, -50, 'university', 'course']

def print_list(lis):
    """This function prints the items of a list."""
    for item in lis:
        print(item)
#%%
"""
Let's print a small report. Here is a list of New England states and their
populations. We'll print this as a table or report. Essentially, this is
like the previous function, except that we need to handle the variables in a
more sophisticated way."""
#%%
newEngland = [["Massachusetts", 6692824], ["Connecticut", 3596080], 
              ["Maine", 1328302], ["New Hampshire", 1323459], 
              ["Rhode Island", 1051511], ["Vermont", 626630]]
#%%
"""
Before writing this function, let's understand this list of lists better.
What is the first item of newEngland?
What is the second item?
What is the name of the state in the second element?
What is the population of this state?
"""
#%%
def report1(state_data):
    """ prints population report"""
    print("Population          State")
    for state_item in state_data:
        print(state_item[1],"          ", state_item[0])
#%%
""" The following function does the same thing as report1 """
def report2(state_data):
    """ print population report """
    print("Population          State")
    for i in range(0, len(state_data)):
        print(state_data[i][1], "          ", state_data[i][0])
#%%
""" Can now find the sum of the populations of the New England states."""
def population(state_data):
    """ sums state populations """
    sum_ = 0
    num_states = len(state_data)
    for i in range(0, num_states):
        one_state = state_data[i]
        pop = one_state[1]
        sum_ = sum_ + pop
    print("The total poulation of this list of states is", sum_)
    print("There are", num_states, "states in this list")
#%%
def average(nlis):
    sum_ = 0
    for i in range(0, len(nlis)):
        sum_ = sum_ + nlis[i]
        print(nlis[i], end=' ')
    print() 
    print("The average is", sum_/len(nlis))
#%%
numlis = [65, 44, 3, 56, 48, 74, 7, 97, 95, 42]
numlis2 = [4, 6, 8, 12, 2, 7, 19]
#%%
"""
Libraries. Python is a 'small' language in the sense that many tools that are
available are not automatically included when you run it. Many of these
tools are in modules called libraries and can be loaded into your program
only when you need them.
A typical way of doing this is

import random

which will load the library named random.
"""
#%%
import random
#%%
# Each run of the following gives a different random number between 0 and 1.
print(random.random())
#%%
# Each run of the following gives a different random integer between 3 and 8.
print(random.randint(3,8))
#%%
import random

verbs = ["goes", "cooks", "shouts", "faints", "chews", "screams"]
nouns = ["bear", "lion", "mother", "baby", "sister", "car", "bicycle", "book"]
adverbs = ["handily", "sweetly", "sourly", "gingerly", "forcefully", "meekly"]
articles = ["a", "the", "that", "this"]

def sentence():
    article = random.choice(articles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    
    our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
    our_sentence = our_sentence.capitalize()
    
    print(our_sentence)
#%%
""" Want to adapt the above function to write a four line poem. """
import random
verbs = ["goes", "cooks", "shouts", "faints", "chews", "screams"]
nouns = ["bear", "lion", "mother", "baby", "sister", "car", "bicycle", "book"]
adverbs = ["handily", "sweetly", "sourly", "gingerly", "forcefully", "meekly"]
articles = ["a", "the", "that", "this"]

def simple_poem():
    "writes a randomly assembled 4 line poem."
    ct = 0
    while ct < 4:
        article = random.choice(articles)
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        adverb = random.choice(adverbs)
    
        our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
        our_sentence = our_sentence.capitalize()
    
        print(our_sentence)    
        ct = ct + 1
#%%
def add_up():
    sum_ = 0
    while True:             # will loop forever
        num = int(input("Enter a number, input 0 to quit: "))
        if num == 0:
            break           # breaks out of while loop
        sum_ = sum_ + num
    print(sum_)
#%%
baseball = []
baseball.append("ball")
baseball.append("bat")
baseball.append("mitt")
baseball
#%%
def store_up():
    num_lis = []
    while True:
        nextnum = int(input("Enter a number, 0 to quit: "))
        if nextnum == 0:
            break
        num_lis.append(nextnum)
    print(num_lis)
#%%
def diner_waitress():
    """ asks for your order and prints it out."""
    order = []
    print("Hello, I'll be your waitress. What would you like to order?")
    while True:
        food = input("Menu item: ")
        if food == "that's all":
            break
        else:
            order.append(food)
    print("You've ordered")
    print(order)
#%%