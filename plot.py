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


x = np.abs(1800*(data[1])/(2*2000000*np.cos(2*np.pi/360*80.06)))
y = np.abs(data[1]/np.cos(2*np.pi/360*80.06))

s = np.abs(1800*(data1[1])/(2*2000000*np.cos(2*np.pi/360*70.53)))
t = np.abs(data1[1]/np.cos(2*np.pi/360*70.53))

q = np.abs(1800*(data2[1])/(2*2000000*np.cos(2*np.pi/360*54.74)))
r = np.abs(data2[1]/np.cos(2*np.pi/360*54.74))


plt.xlabel(r'v$/\si{\meter\per\second}$')
plt.ylabel(r'$\Delta \nu /\cos(\alpha)$')

plt.grid(True, which='both')

#lin = np.linspace(x[0], x[-1], 100)
#plt.plot(lin, 2*2000000*lin/1800)
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


x = np.abs(1800*(data[3])/(2*2000000*np.cos(2*np.pi/360*80.06)))
y = np.abs(data[3]/np.cos(2*np.pi/360*80.06))

s = np.abs(1800*(data1[3])/(2*2000000*np.cos(2*np.pi/360*70.53)))
t = np.abs(data1[3]/np.cos(2*np.pi/360*70.53))

q = np.abs(1800*(data2[3])/(2*2000000*np.cos(2*np.pi/360*54.74)))
r = np.abs(data2[3]/np.cos(2*np.pi/360*54.74))


plt.xlabel(r'v$/\si{\meter\per\second}$')
plt.ylabel(r'$\Delta \nu /\cos(\alpha)$')

plt.grid(True, which='both')



#lin = np.linspace(x[0], x[-1], 100)
#plt.plot(lin, 2*2000000*lin/1800)
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


x = np.abs(1800*(data[5])/(2*2000000*np.cos(2*np.pi/360*80.06)))
y = np.abs(data[5]/np.cos(2*np.pi/360*80.06))

s = np.abs(1800*(data1[5])/(2*2000000*np.cos(2*np.pi/360*70.53)))
t = np.abs(data1[5]/np.cos(2*np.pi/360*70.53))

q = np.abs(1800*(data2[5])/(2*2000000*np.cos(2*np.pi/360*54.74)))
r = np.abs(data2[5]/np.cos(2*np.pi/360*54.74))


plt.xlabel(r'v$/\si{\meter\per\second}$')
plt.ylabel(r'$\Delta \nu /\cos(\alpha)$')

plt.grid(True, which='both')



#lin = np.linspace(x[0], x[-1], 100)
#plt.plot(lin, 2*2000000*lin/1800)
plt.plot(x, y, "x", color="xkcd:blue", label="Messwerte($15\si{\degree}$)")
plt.plot(s, t, "x", color="xkcd:red", label="Messwerte($30\si{\degree}$)")
plt.plot(q, r, "x", color="xkcd:green", label="Messwerte($60\si{\degree}$)")

plt.tight_layout()
plt.legend()
plt.savefig('build/60.pdf')
plt.clf()

cp = 10/4
cfl = 6/4

def convert(x):
	for i in range(x.size):
		if x[i] <= 30.7/cp:
			x[i] = x[i]*cp
		else:
			x[i] = x[i]*cfl + 30.7*(1-cfl/cp)


strom = np.genfromtxt("content/strömungsprofil.txt", unpack=True)

x = np.abs(strom[0])
convert(x)

y1 = np.abs(1800*(strom[1])/(2*2000000*np.cos(2*np.pi/360*80.06)))

y2 = np.abs(strom[2])

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, y1, 'g.', label="Messwerte für die Geschwindigkeit")
ax2.plot(x, y2, 'b.', label="Messwerte für die Streuintensität")

#plt.legend()
ax1.set_xlabel("Eindringungstiefe/\si{\micro\second}")
ax1.set_ylabel(r"$v/\si{\meter\per\second}$", color='g')
ax2.set_ylabel("\sigma/\si{\percent}", color='b')
plt.tight_layout()
plt.savefig("build/strom1.pdf")
plt.clf()

strom1 = np.genfromtxt("content/strömungsprofil2.txt", unpack=True)

x1 = np.abs(strom1[0])
convert(x1)
y3= np.abs(1800*(strom1[1])/(2*2000000*np.cos(2*np.pi/360*80.06)))

y4 = np.abs(strom1[2])

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x1, y3, 'g.', label="Messwerte für die Geschwindigkeit")
ax2.plot(x1, y4, 'b.', label="Messwerte für die Streuintensität")

#plt.legend()
ax1.set_xlabel("Eindringungstiefe/\si{\milli\meter}")
ax1.set_ylabel(r"$v/\si{\meter\per\second}$", color='g')
ax2.set_ylabel("\sigma/\si{\percent}", color='b')
plt.tight_layout()
plt.savefig("build/strom2.pdf")
plt.clf()
