#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:14:20 2020

@author: owner
"""

#%%
def problem2_8(temp_list):
    sum_ = 0
    for i in range(0,len(temp_list)):
        sum_ = sum_ + temp_list[i]
        high = max(temp_list)
        low = min(temp_list)
    print("Average: ", sum_/len(temp_list))
    print("High: ", high)
    print("Low: ", low)   