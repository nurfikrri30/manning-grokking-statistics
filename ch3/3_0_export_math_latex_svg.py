# export a math latex expression as an SVG
from sympy import *
x = symbols('x')
expr = x**2 + 2*x + 1
preview(expr, viewer='file', filename='expression.svg', euler=False)