# %%

import sympy
import numpy


def ideal(a, b, K):
    x = sympy.Symbol("x")
    print(sympy.solve((x/(1-x))**2*(100-(a*x/2))/(b-(a*x/2))-K**2))
    return x
# C:\Users\io\Anaconda3\python.exe C:\Users\io\anaconda3\cwp.py C:\Users\io\anaconda3 C:\Users\io\anaconda3\python.exe C:\Users\io\anaconda3\Scripts\jupyter-notebook-script.py "%USERPROFILE%/"


a_r = numpy.array([[10.0, 18.0, 583],
                   [10.0, 18.0, 64.9],
                   [10.0, 18.0, 12.5]])

ideal_co = [ideal(_a, _b, _k) for _a, _b, _k in a_r]
# ideal_co = list(ideal(a_r[:, 0], a_r[:, 1], a_r[:, 2]))
# %%
ideal_co
