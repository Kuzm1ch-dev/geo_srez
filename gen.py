
import string

import math 
from datetime import datetime

from matplotlib.pyplot import step 


class generator:
    def __init__(self, s,l,fi,offset):
        self.s = s 
        self.l = l
        self.fi = fi
        self.offset = offset
    def generate_file(self):

        layer_count = len(self.l)
        a = []
        
        #Остальные self.s строки

        for i in range (self.s):
            row = []
            index = i // (int((self.s / layer_count)) + 1)
            for j in range (self.s):
                row.insert(len(row), self.l[index])
            a.insert(len(a),row)

        l = len(a)
        for i in range (l):
            x = (self.s-i) / math.tan((self.fi*(math.pi / 180))) + int((self.s-1) / 3)
            for j in range (self.s):
                if j < x:
                    if(l - i - self.offset < 0 ):
                        a[l - i][j] = a[0][j]
                        continue
                    a[l - i - 1][j] = a[l - i - self.offset][j]

        f = open("Data.txt", "w")
        with f:
            f.write(f"{self.s} {self.s}"  + "\n")
            for r in a:
                f.write('   '.join(str(i) for i in r) + "\n")
        f.close()
        pass