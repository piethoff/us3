import matplotlib as mpl
mpl.use('pgf')
mpl.rcParams.update({
    'pgf.preamble': r'\usepackage{siunitx}',
})

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import unumpy

c_l = 1800
c_p = 2700

def f(x, A, B):
    return A*x + B


##15°##
data1 = np.genfromtxt("content/15.txt", unpack=True)

data2 = np.append(data1[0], data1[2])
data2 = np.append(data2, data1[4])
data = data2

data2 = np.append(data1[1], data1[3])
data2 = np.append(data2, data1[5])
data = np.array([data, data2])
data[1] = np.abs(data[1])


#for i in range(data[0].size):
#	print(data[0][i], data[1][i], sep="\t& ", end="\\\\\n")

data[1] /= np.cos(np.pi/2 - np.arcsin(np.sin(2*np.pi/360 * 15) * c_l/c_p))

print("15°:\n")
for i in range(0,3):
	plt.plot(data[0][5*i:5*(i+1)], data[1][5*i:5*(i+1)], ".", label="Messwerte")
	params, covar = curve_fit(f, data[0][5*i:5*(i+1)], data[1][5*i:5*(i+1)])
	uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
	print(i+1, "-tes Rohr:", sep="")
	for j in range(0, len(uparams)):
		print(chr(ord('A') + j), "=" , uparams[j])
	print()
	lin = np.linspace(data[0][5*i], data[0][5*(i+1)-1], 10)
	plt.plot(lin, f(lin, *params), color="xkcd:orange", label="lin. Fit")

plt.legend()
plt.xlabel("Strömungsgeschwindigkeit/RPM")
plt.ylabel(r"$\frac{\Delta\nu}{\cos\alpha}/\si{\hertz}$")
plt.tight_layout()
plt.savefig("build/15.pdf")
plt.clf()








##30°##
data1 = np.genfromtxt("content/30.txt", unpack=True)

data2 = np.append(data1[0], data1[2])
data2 = np.append(data2, data1[4])
data = data2

data2 = np.append(data1[1], data1[3])
data2 = np.append(data2, data1[5])
data = np.array([data, data2])
data[1] = np.abs(data[1])


#for i in range(data[0].size):
#	print(data[0][i], data[1][i], sep="\t& ", end="\\\\\n")

data[1] /= np.cos(np.pi/2 - np.arcsin(np.sin(2*np.pi/360 * 30) * c_l/c_p))

print("30°:\n")
for i in range(0,3):
	plt.plot(data[0][5*i:5*(i+1)], data[1][5*i:5*(i+1)], ".", label="Messwerte")
	params, covar = curve_fit(f, data[0][5*i:5*(i+1)], data[1][5*i:5*(i+1)])
	uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
	print(i+1, "-tes Rohr:", sep="")
	for j in range(0, len(uparams)):
		print(chr(ord('A') + j), "=" , uparams[j])
	print()
	lin = np.linspace(data[0][5*i], data[0][5*(i+1)-1], 10)
	plt.plot(lin, f(lin, *params), color="xkcd:orange", label="lin. Fit")

plt.legend()
plt.xlabel("Strömungsgeschwindigkeit/RPM")
plt.ylabel(r"$\frac{\Delta\nu}{\cos\alpha}/\si{\hertz}$")
plt.tight_layout()
plt.savefig("build/30.pdf")
plt.clf()






##60°##
data1 = np.genfromtxt("content/60.txt", unpack=True)

data2 = np.append(data1[0], data1[2])
data2 = np.append(data2, data1[4])
data = data2

data2 = np.append(data1[1], data1[3])
data2 = np.append(data2, data1[5])
data = np.array([data, data2])
data[1] = np.abs(data[1])


#for i in range(data[0].size):
#	print(data[0][i], data[1][i], sep="\t& ", end="\\\\\n")

data[1] /= np.cos(np.pi/2 - np.arcsin(np.sin(2*np.pi/360 * 60) * c_l/c_p))

print("60°:\n")
for i in range(0,3):
	plt.plot(data[0][5*i:5*(i+1)], data[1][5*i:5*(i+1)], ".", label="Messwerte")
	params, covar = curve_fit(f, data[0][5*i:5*(i+1)], data[1][5*i:5*(i+1)])
	uparams = unumpy.uarray(params, np.sqrt(np.diag(covar)))
	print(i+1, "-tes Rohr:", sep="")
	for j in range(0, len(uparams)):
		print(chr(ord('A') + j), "=" , uparams[j])
	print()
	lin = np.linspace(data[0][5*i], data[0][5*(i+1)-1], 10)
	plt.plot(lin, f(lin, *params), color="xkcd:orange", label="lin. Fit")

plt.legend()
plt.xlabel("Strömungsgeschwindigkeit/RPM")
plt.ylabel(r"$\frac{\Delta\nu}{\cos\alpha}/\si{\hertz}$")
plt.tight_layout()
plt.savefig("build/60.pdf")
plt.clf()
