'''
Created on 2023. 7. 24.

@author: wooyong.shin
'''
import numpy as np

class AFFINE:
    def __init__(self,W,b):
        self.params = [W,b]
        
    def forward(self,x):
        W, b = self.W, self.b
        out = np.matmul(x,W) + b
        
        return out