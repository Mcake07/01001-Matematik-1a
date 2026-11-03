import sympy as sp


i = sp.I

z = 4 + i
print(sp.simplify(z / (sp.Abs(z))**2))