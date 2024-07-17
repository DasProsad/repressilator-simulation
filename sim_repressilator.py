#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def repressilator(t, y):
	"""
	Minimal model of the three-component repressilator.
	It is constructed as a regulatory circuit of three
	genes: tetR, LacI, and lambda CI.
	
	Parameters:
	- t (numpy array): Vector of time
	- y (list[int]): A list of initial conc. of tetR, LacI and Lambda cI respectively
	
	Returns:
	- A list of rates of the three genes
	"""
	
	# Maximum transcription rate (mRNAs/unit time)
	alpha_0 = 50
	
	# Hill coefficient
	n = 2
	
	# Vector of concentrations
	tetR, LacI, Lci = y
	
	# Rate equations
	dtetR_dt = alpha_0 / (1 + LacI**n) - tetR
	dLacI_dt = alpha_0 / (1 + Lci**n) - LacI
	dLci_dt = alpha_0 / (1 + tetR**n) - Lci
	
	return [dtetR_dt, dLacI_dt, dLci_dt]

def simulate_repressilator(odes):
	"""
	Solves the repressilator.
	
	Parameters:
	- odes: System of ODEs
	
	Returns:
	- Tuple of time vector and concentraion vector of tetR, LacI and Lambda cI mRNAs
	"""
	# Initial conc. of tetR, LacI, Lambda cI mRNAs (copies/uL)
	y_0 = [0, 2, 0]
	
	# Time span
	t_span = [0,50]
	t_eval = np.linspace(0, 50, 1000)

	# Solve ODEs
	solution = solve_ivp(odes, t_span, y_0, t_eval = t_eval)

	# Results
	t = solution.t
	conc = solution.y
	
	return t, conc

if __name__ == "__main__":
	
	t_vector, conc_vector = simulate_repressilator(odes = repressilator)

	tetR = conc_vector[0]
	LacI = conc_vector[1]
	Lci = conc_vector[2]
	
	# use tex font, sudo apt install cm-super dvipng
	plt.rcParams['text.usetex'] = True
	plt.rc("font", family="serif", size=12)
	
	# Plot the results
	plt.figure(figsize=(3.5,3))
	plt.plot(t_vector, tetR, label=r'$\mathrm{tetR}$')
	plt.plot(t_vector, LacI, label=r'$\mathrm{LacI}$')
	plt.plot(t_vector, Lci, label=r'$\lambda \mathrm{cI}$')
	plt.xlabel('Time (Minutes)')
	plt.ylabel(r'Concentration (Transcripts / $\mu$L)')
	plt.title('Repressilator Dynamics')
	plt.legend()
	plt.grid()
	plt.tight_layout()
	plt.savefig("repressilator.pdf")
	plt.show()
