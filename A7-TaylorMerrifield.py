# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:39:44 2019

@author: Taylor
"""
import regression as r
import matplotlib.pyplot as plt
import numpy as np


def listMaker(file, axs, count):
    x = []
    y =[]
    x.clear()
    y.clear()
    lineList = [line.rstrip('\n') for line in open(file)]
    for item in lineList:
        item = item.rstrip("'")
        splitter = item.split(",")
        x.append(float(splitter[0]))
        y.append(float(splitter[1]))
    print("Data points: " + str(len(x)))
    computer(x,y, axs, count)
   # x = [50,60,75,77,86,96,32,82,53,91]
    #y = [47,41,71,65,88,89,18,79,67,94]

#r.compute_pearson_coefficient(lst)
def computer(x, y, axs, count):

    m,b = r.compute_m_and_b(x, y)
    fx, res = r.compute_fx_residual(x,y,m,b)
    sqrRes = r.compute_sum_of_squared_residuals(res)
    ysqr = r.compute_total_sum_of_squares(y)
    pear = r.compute_pearson_coefficient(x, y)
    mx = m*80 + b
    alt = r.compute_pearson_coefficient_alternate(x,y)
    print("Coefficients:\t" + "M: " + str(m) + "\tB: " + str(b))
    print("Sum of Squared Residuals: " + str(sqrRes))
    print("Total Sum of Squares: " + str(ysqr))
    print("mx: " + str(mx))
    print("Alt Pearson Coeef: " + str(alt))
    print("Pearson Method: " + str(pear))
    
    if count == 0:
        clr = 'grey'
    if count == 1:
        clr= 'blue'
    if count == 2:
        clr = 'green'
    if count == 3: 
        clr = 'black'
    axs[count].scatter(x,y, color=clr)
    #axs[count].title(figure_title, y=1.08)
    axs[count].title.set_text("in" + str(count + 1))
    axs[count].set_ylabel("Y Values")
    axs[count].set_xlabel("X Values")
    axs[count].plot(x, fx, color='red')
    axs[count].legend( ('x vs f(x)', 'x vs y') )
    plt.tight_layout()
    
    #print(mx)
    print("\n\n")

def loop():
    i = 1
    figs, axs = plt.subplots(4)
    while i <= 4:
        name = "in" + str(i)
        print("Input File: " + name)
        listMaker(name, axs, i - 1)
        i+=1
        
loop()
