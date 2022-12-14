
import string

import random 
from datetime import datetime

from matplotlib.pyplot import step 


class generator:
    def __init__(self, w,h,step, cw,ch,v,p,x,y):
        self.step = step
        self.w = w 
        self.h = h
        self.cw = cw
        self.ch = ch
        self.v = v
        self.p = p
        self.x = x
        self.y = y
    def generate_file(self):
        a = []


        #Первые 2 строки хуй пойми что
        for i in range (2):
            row = []
            for j in range (self.h):
                row.insert(0,500)
            a.insert(len(a),row)

        
        #Остальные self.h строки

        for i in range (self.w):
            row = []
            for j in range (self.h):
                row.insert(len(row)-1,self.p)
            a.insert(len(a),row)

        #Квадрат

        value = self.v

        for i in range (self.w):
            for j in range (self.h):
                if (i >= (self.y-1) and i <  (self.y-1) + self.ch and i < self.h) and (j >=  (self.x-1) and j <  (self.x-1) + self.cw and j < self.w):
                    a[i][j] = value

        f = open("Data.txt", "w")
        with f:
            f.write(f"{self.w} {self.h}"  + "\n")
            for r in a:
                f.write(' '.join(str(i) for i in r) + "\n")
        f.close()
        pass