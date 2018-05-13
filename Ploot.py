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
data1 = np.genfromtxt('content/30.txt', unpack=True)
data2 = np.genfromtxt('content/60.txt', unpack=True)


x = (-1)*1800*(data[0])/(2*2000000*np.cos(80.06))
y = (-1)*data[0]/np.cos(80.06)

s =(-1)*1800*(data1[1])/(2*2000000*np.cos(70.53))
t =(-1)*data1[1]/np.cos(70.53)

q =1800*(data2[1])/(2*2000000*np.cos(54.74))
r =data2[1]/np.cos(54.74)


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
plt.plot(lin, f(lin, *params), "xkcd:orange", label=r'$\theta = 15\si{\degree}$' )

# Fit 2
def g(s, S, T):
    return S*s + T


params, covar = curve_fit(g, s, t)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('S') + i), "=" , uparams[i])
print()

lin = np.linspace(s[0], s[-1], 1000)
plt.plot(lin, g(lin, *params), "xkcd:red", label=r'$\theta = 30\si{\degree}$' )


# Fit 3
def h(q, Q, R):
    return Q*q + R


params, covar = curve_fit(h, q, r)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('Q') + i), "=" , uparams[i])
print()

lin = np.linspace(q[0], q[-1], 1000)
plt.plot(lin, h(lin, *params), "xkcd:green", label=r'$\theta = 60\si{\degree}$' )

plt.plot(x, y, "x", color="xkcd:blue", label="Messwerte($15\si{\degree}$)")
plt.plot(s, t, "x", color="xkcd:red", label="Messwerte($30\si{\degree}$)")
plt.plot(q, r, "x", color="xkcd:green", label="Messwerte($60\si{\degree}$)")

plt.tight_layout()
plt.legend()
plt.savefig('build/15.pdf')
plt.clf()


#plot2
data = np.genfromtxt('content/15.txt', unpack=True)
data1 = np.genfromtxt('content/30.txt', unpack=True)
data2 = np.genfromtxt('content/60.txt', unpack=True)


x = 1800*(data[3])/(2*2000000*np.cos(80.06))
y = data[3]/np.cos(80.06)

s =(-1)*1800*(data1[3])/(2*2000000*np.cos(70.53))
t =(-1)*data1[3]/np.cos(70.53)

q =1800*(data2[3])/(2*2000000*np.cos(54.74))
r =data2[3]/np.cos(54.74)


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
plt.plot(lin, f(lin, *params), "xkcd:orange", label=r'$\theta = 15\si{\degree}$' )

# Fit 2
def g(s, S, T):
    return S*s + T


params, covar = curve_fit(g, s, t)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('S') + i), "=" , uparams[i])
print()

lin = np.linspace(s[0], s[-1], 1000)
plt.plot(lin, g(lin, *params), "xkcd:red", label=r'$\theta = 30\si{\degree}$' )


# Fit 3
def h(q, Q, R):
    return Q*q + R


params, covar = curve_fit(h, q, r)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('Q') + i), "=" , uparams[i])
print()

lin = np.linspace(q[0], q[-1], 1000)
plt.plot(lin, h(lin, *params), "xkcd:green", label=r'$\theta = 60\si{\degree}$' )

plt.plot(x, y, "x", color="xkcd:blue", label="Messwerte($15\si{\degree}$)")
plt.plot(s, t, "x", color="xkcd:red", label="Messwerte($30\si{\degree}$)")
plt.plot(q, r, "x", color="xkcd:green", label="Messwerte($60\si{\degree}$)")

plt.tight_layout()
plt.legend()
plt.savefig('build/30.pdf')
plt.clf()
#plot3

data = np.genfromtxt('content/15.txt', unpack=True)
data1 = np.genfromtxt('content/30.txt', unpack=True)
data2 = np.genfromtxt('content/60.txt', unpack=True)


x = 1800*(data[5])/(2*2000000*np.cos(80.06))
y = data[5]/np.cos(80.06)

s =(-1)*1800*(data1[5])/(2*2000000*np.cos(70.53))
t =(-1)*data1[5]/np.cos(70.53)

q =1800*(data2[5])/(2*2000000*np.cos(54.74))
r =data2[5]/np.cos(54.74)


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
plt.plot(lin, f(lin, *params), "xkcd:orange", label=r'$\theta = 15\si{\degree}$' )

# Fit 2
def g(s, S, T):
    return S*s + T


params, covar = curve_fit(g, s, t)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('S') + i), "=" , uparams[i])
print()

lin = np.linspace(s[0], s[-1], 1000)
plt.plot(lin, g(lin, *params), "xkcd:red", label=r'$\theta = 30\si{\degree}$' )


# Fit 3
def h(q, Q, R):
    return Q*q + R


params, covar = curve_fit(h, q, r)            #eigene Messwerte hier uebergeben
uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
for i in range(0, len(uparams)):
    print(chr(ord('Q') + i), "=" , uparams[i])
print()

lin = np.linspace(q[0], q[-1], 1000)
plt.plot(lin, h(lin, *params), "xkcd:green", label=r'$\theta = 60\si{\degree}$' )

plt.plot(x, y, "x", color="xkcd:blue", label="Messwerte($15\si{\degree}$)")
plt.plot(s, t, "x", color="xkcd:red", label="Messwerte($30\si{\degree}$)")
plt.plot(q, r, "x", color="xkcd:green", label="Messwerte($60\si{\degree}$)")

plt.tight_layout()
plt.legend()
plt.savefig('build/60.pdf')
plt.clf()
