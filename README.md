# Simulation of repressilator
Simulation of repressilator from Liebler and Elowitz, Nature, 2000 (https://doi.org/10.1038/35002125)

## Minimal model of repressilator
$$
\begin{align}
\frac{d}{dt}tetR = \alpha_0 * \frac{1}{1 + lacI^n} - tetR \\
\frac{d}{dt}LacI = \alpha_0 * \frac{1}{1 + \lambda cI^n} - LacI \\
\frac{d}{dt}\lambda cI = \alpha_0 * \frac{1}{1 + tetR^n} - \lambda cI
\end{align}
$$
