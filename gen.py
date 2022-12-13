
import string

import random 
from datetime import datetime

from matplotlib.pyplot import step 


class generator:
    def __init__(self, w,h,step, cw,ch,v):
        self.step = step
        self.w = w 
        self.h = h
        self.cw = cw
        self.ch = ch
        self.v = v
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
                row.insert(len(row)-1,self.step * (i // 4) + self.step)
            a.insert(len(a),row)

        #Квадрат

        random.seed(datetime.now().timestamp() + i)
        x = random.randint(1,self.w - self.cw)
        y = random.randint(1,self.h  - self.ch)
        value = self.v

        for i in range (self.w):
            for j in range (self.h):
                if (i >= y and i < y + self.ch and i < self.h) and (j >= x and j < x + self.cw and j < self.w):
                    a[i+2][j] = value

        f = open("Data.txt", "w")
        with f:
            f.write(f"{self.w} {self.h}"  + "\n")
            for r in a:
                f.write(' '.join(str(i) for i in r) + "\n")
        f.close()
        pass