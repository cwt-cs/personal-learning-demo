# personal-learning-demo
#compile with python php JavaScript  html css and the others (languages) will be update.

from random import choice  
import numpy as np
class Randomwalk():
    def _init_(self):
        self.color='green'
        
    def point_walk(self):
        self.randompoint=5000
        self.x_values= [0]
        self.y_values= [0]
        while len(self.x_values) < self.randompoint:
            
       # while len(self.x_values) < self.randompoint:
            x_dir=choice([1,-1])
            x_dis=choice(np.arange(0,100))
            x_step=x_dir * x_dis
            y_dir=choice([1,-1])
            y_dis=choice(np.arange(0,100))
            y_step=y_dir * y_dis
            if x_step == 0 and y_step == 0:
                continue
            next_xstep=self.x_values[-1]+x_step
            next_ystep=self.y_values[-1]+y_step
            self.x_values.append(next_xstep)
            self.y_values.append(next_ystep)
