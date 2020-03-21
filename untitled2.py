# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:22:50 2020

@author: User
"""
import random
counter=0
answer=int(input())
while True:
    a = int(input("請從1到10猜一個數字"))
    counter=counter+1
    if counter>=5:
        break
    if answer == a:
        print("恭喜猜對")
        break
    else:
        print("恭喜猜錯")