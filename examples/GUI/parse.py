import numpy as np
import sympy
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr

fstr = input("f(x) = ")

a = parse_expr(fstr, evaluate=0)

f = sympy.lambdify(x, a, "numpy")

x = np.linspace(0,1,100)

print(f(x))
