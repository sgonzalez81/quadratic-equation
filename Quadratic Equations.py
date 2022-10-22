# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 02:11:30 2022

@author: salva

Write a function roots that computes the roots of a quadratic equation. Check for complex roots and print an
error message saying that the roots are complex.
Hint 1: Your function should take three parameters- what are they?
Hint 2: We know the roots are complex when what condition about the discriminant is met?
Be sure to use a variety of test cases, that include complex roots, real roots, and double roots.
Optional: For an extra challenge, compute and print out the complex roots (Python can natively handle complex
numbers - here’s a good reference: http://infohost.nmt.edu/tcc/help/pubs/python/web/complex-type.html).
"""

import numpy as np
import cmath

def roots(a, b, c):
   
     i = b**2 - 4 * a * c   # this is b**2 - 4ac expression inside the sqrt
     
     if i < 0: 
         res = cmath.sqrt(i)   # cmath.sqrt handles complex numbers
     else:
         res = np.sqrt(i)
     
     p = (-b + res) / (2 * a)
     n = (-b - res) / (2 * a)
     
     if i == 0:
         return p
    
     return [p, n]
     

# x^2 - 25
x = roots(1, 0, -25)
print(f"test[two real roots]    x^2 - 25;      x is {x}")


# x^2 + 25
x = roots(1, 0, 25)
print(f"test[two complex roots] x^2 + 25;      x is {x}")


# x^2 + 2x + 1
x = roots(1, 2, 1)
print(f"test[one real root]     x^2 + 2x + 1;  x is {x}")

# x^2 - 2x + 1
x = roots(1, -2, 1)
print(f"test[one real root]     x^2 - 2x + 1;  x is {x}")
