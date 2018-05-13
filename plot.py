import matplotlib as mpl

mpl.use('pgf')
mpl.rcParams.update({
    'pgf.preamble': r'\usepackage{siunitx}',
})

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import unumpy

#plot1

data = np.genfromtxt('content/15.txt', unpack=True)


x = 1800*(data[0])/(2*2000000*np.cos(80.06)

y = (-1)*data[1]/np.cos(80.06)

plt.xlabel(r'v$/\si{\meter\per\second}$')
plt.ylabel(r'$\Delta \nu /\cos(\alpha)$')

plt.grid(True, which='both')


# Fitvorschrift
def f(x, A, B):
    return A*x + B


params, covar = curve_fit(f, x, y)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('A') + i), "=" , uparams[i])
print()

lin = np.linspace(x[0], x[-1], 1000)
plt.plot(lin, f(lin, *params), "xkcd:orange", label=r'Röhrendurchmesser=$10\si{\milli\meter}$' )
plt.plot(x, y, ".", color="xkcd:blue", label="Messwerte")



plt.tight_layout()
plt.legend()
plt.savefig('build/15.pdf')
plt.clf()
