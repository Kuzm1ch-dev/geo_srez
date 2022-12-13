
import string

import random 
from datetime import datetime 


class generator:
    def __init__(self, w,h,step, cube_count):
        self.step = step
        self.w = w 
        self.h = h
        self.cube_count = cube_count
    def generate_file(self):
        a = []


        #Первые 2 строки хуй пойми что
        for i in range (2):
            row = []
            for j in range (self.h):
                row.insert(0,self.step)
            a.insert(len(a),row)

        
        #Остальные self.h строки

        for i in range (self.w):
            row = []
            for j in range (self.h):
                row.insert(len(row)-1,self.step * i + self.step)
            a.insert(len(a),row)

        #Квадраты

        for i in range (self.cube_count):
            random.seed(datetime.now().timestamp() + i)
            x = random.randint(1,self.w)
            y = random.randint(1,self.h)
            cw = random.randint(1,self.w - x)
            ch = random.randint(1,self.h - y)
            value = random.randint(1,10) * self.step

            print(x,y)

            for i in range (self.w):
                for j in range (self.h):
                    if (i >= y and i < y+ch) and (j >= x and j < x+cw):
                        a[i+2][j] = value

        #print(a)

        f = open("Data.txt", "w")
        with f:
            f.write(f"{self.w} {self.h}"  + "\n")
            for r in a:
                f.write(' '.join(str(i) for i in r) + "\n")
        f.close()
        pass