import numpy as np
import sympy
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr

str = raw_input("f(x) = ")

a = parse_expr(str, evaluate=0)

f = sympy.lambdify(x, a, "numpy")

x = np.linspace(0,1,100)

print f(x)
