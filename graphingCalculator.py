from tkinter import *
from tkinter import ttk
import math
from math import sqrt  
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from csv import DictWriter

root = Tk()
root.option_add('*Font', 'Times 19')
root.title('graphingCalculator')
root.minsize(450, 650)


class Polynomial:
    
    def __init__(self, a):
        self.coefficients = a
     
    
    def __repr__(self):
        return "Polynomial" + str(tuple(self.coefficients))

    
    def __str__(self):
        
        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^"+str(degree)
            return res

        degree = len(self.coefficients) - 1
        res = ""

        for i in range(0, degree+1):
            coeff = self.coefficients[i]
            if abs(coeff) == 1 and i < degree:
                res += f"{'+' if coeff>0 else '-'}{x_expr(degree-i)}"  
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(degree-i)}" 

        return res.lstrip('+')

    
    def __init__(self, coefficients):
        self.coefficients = (coefficients)
            
    def __call__(self, x):    
        res = 0
        for index, coeff in enumerate(self.coefficients[::-1]):
            res += coeff * x** index
        return res 

class PolynomialPlot:
    
    def __init__(self, coefficients):
       
        self.coefficients = (coefficients) 
            
    def __call__(self, x):    
        res = 0
        for index, coeff in enumerate(self.coefficients[::-1]):
            res += coeff * x** index
        return res 


def reset():
    global equationLabel
    global equation
    
    print('--------------------------------New Equation--------------------------------')
    
    equation = []

    #row 0
    Label(root, text="Enter integer (int):").grid(row=0, column=0, sticky="w")

    Label(root, text="").grid(row=0, column=1, padx=50)

    entry = Entry(root)
    entry.grid(row=0, column=2, sticky=E + W)


    #row 1
    Label(root, text="").grid(row=1, column=0, columnspan=3)


    #row 2
    Button(root, text="Enter", height=3, width=22, bg="Green",
           command=lambda: [b_click(entry.get()), clear_text(entry), updateLabel(equation)]).grid(row=2, column=0, columnspan=3)


    #row 3
    Label(root, text="").grid(row=3, column=0, columnspan=3)


    #row 4
    Button(root, text="Restart", height=3, width=22, bg="Green",
           command=lambda: [root.destroy()]).grid(row=4, column=0, columnspan=3)


    #row 5
    Label(root, text="").grid(row=5, column=0, columnspan=3)


    #row 6
    Button(root, text="Plot from -100 to 100", height=3, width=22, bg="Green",
           command=lambda: plot()).grid(row=6, column=0, columnspan=3)


    #row 7
    Label(root, text="").grid(row=7, column=0, columnspan=3)


    #row 8
    Label(root, text="Current Equation:").grid(row=8, column=0)


    #row 9
    equationLabel = Label(root, text="")
    equationLabel.grid(row=9, column=0, columnspan=3)


def b_click(entry):
    equation.append((int)(entry))
    print(equation)


def clear_text(self):
    self.delete(0, END)
    self.insert(0, "")


def updateLabel(equation):
    
    polys = Polynomial(equation)

    print(str(polys))
    equationLabel.configure(text=str(polys))


def plot():
    xray = []
    yray = []
    
    p = PolynomialPlot(equation)
    print(p)

    for x in range(-3, 3):
        xray.append(x)
        yray.append(p(x))
        print(x, p(x))

    print(xray)
    print(yray)

    plt.plot(xray, yray)
    plt.show()

    #from csv import writer
    List = [equation,xray,yray]
    with open('graphingEquations - Sheet1 (1).csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()


reset()
root.mainloop()




