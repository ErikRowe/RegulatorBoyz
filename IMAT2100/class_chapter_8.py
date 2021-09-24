import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class Chapter8(object):
    def __init__(self):
        super(Chapter8, self).__init__
    
    def convert_pol_cart(self, length, angle):
        """
        Angle must be in radians. \n
        Returns carthesian x, y"""
        x = length * math.cos(angle)
        y = length * math.sin(angle)
        return x, y

    def convert_cart_pol(self, x_pos, y_pos):
        """
        Returns polar cord. lenght and angle in radians"""
        length = math.sqrt(x_pos**2 + y_pos**2)
        angle = math.atan(y_pos/x_pos)
        return length, angle
        