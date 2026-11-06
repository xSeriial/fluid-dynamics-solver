# Lattice Boltzmann Method

This file gives an overview, some derivations, maybe even some proofs and some important informations and restrictions about the lattice boltzmann method.
It starts of by defining the basic mathematics to make an implementation more straight forward.

## Mathematics

Rather then lookin at the fluid as a continuum as done for the Navier Stokes equations, the LBM works on a mesoscopic scale.
Meaning it works with molecular statistics based on kinetic theory.

To start of we introduce the **particle distribution function** $f(\boldsymbol{x},\boldsymbol{\xi},t)$.
It represents the density of particles with velocity $\boldsymbol{\xi} = (\xi_1, \xi_2, \xi_3)$ at position $\boldsymbol{x} = (x_1, x_2, x_3)$ at time $t$.

It relates to the macroscopic fluid variables density, momentum density and energy density through its **moments**.
They are given as
$$\rho(\boldsymbol{x},t) = \int f(\boldsymbol{x},\boldsymbol{\xi},t) \mathrm{d}^3\xi $$
$$\rho(\boldsymbol{x},t)\boldsymbol{u}(\boldsymbol{x},t) = \int \boldsymbol{\xi} f(\boldsymbol{x},\boldsymbol{\xi},t) \mathrm{d}^3\xi$$
$$\rho(\boldsymbol{x},t) E(\boldsymbol{x},t) = \frac{1}{2}\int |\boldsymbol{\xi}|^2 f(\boldsymbol{x},\boldsymbol{\xi},t) \mathrm{d}^3\xi$$

It is assumed that this distribution function relaxes to an equillibrium after being left alone for long enough.
This **equillibrium distribution** $f^{\mathrm{eq}}(\boldsymbol{x},\boldsymbol{\xi},t)$ is isotropic in velocity space around the reference frame velocity $\boldsymbol{\xi}=\boldsymbol{u}$.

This equillibrium distribution is the Maxwell-Boltzmann distribution and looks as follows

$$f^{\mathrm{eq}}(\boldsymbol{x},\boldsymbol{|v|},t) = \rho \biggl( \frac{1}{2 \pi RT} \biggr)^{3/2} e^{-|\boldsymbol{v}|^2/(2RT)}$$

To study the evolution of the distribution function we write its total derivative as
$$\frac{df}{dt} = \biggl( \frac{\partial f}{\partial t} \biggr) \frac{dt}{dt} + \biggl( \frac{\partial f}{\partial x_\beta} \biggr) \frac{dx_\beta}{dt} + \biggl( \frac{\partial f}{\partial \xi_\beta} \biggr) \frac{d\xi_\beta}{dt}$$

Which again can be rewritten using Newtons second law to the **Boltzmann equation** using the notation $\frac{df}{dt} = \Omega(f)$
$$\frac{\partial f}{\partial t} + \frac{\partial f}{\partial x_\beta}\xi_\beta + \frac{\partial f}{\partial \xi_\beta}\frac{F_\beta}{\rho} = \Omega(f)$$

The source term on the rhs is called the **collision operator**.

The simplest possible expression, which still conserves the moments and relaxes to the equillibrium for this operator is the one provided by Bhatnagar, Gross and Krook and has the following form:
$$\Omega(f) = -\frac{1}{\tau}(f - f^{\mathrm{eq}})$$
with **relaxation time** $\tau$ that describes the time needed to reach the equillibrium.

## Macroscopic conservation equations

Integrating the Boltzmann equation over velocity space we get

$$\frac{\partial}{\partial t} \int_{} f \mathrm{d}^3\xi+ \frac{\partial}{\partial x_\beta} \int f \xi_\beta \mathrm{d}^3\xi + \frac{F_\beta}{\rho} \int \frac{\partial f}{\partial \xi_\beta} \mathrm{d}^3 \xi = \int \Omega(f) \mathrm{d}^3 \xi$$

Using the previously defined moments and the fact that the collision operator must conserve mass, we obtain the **continuity equation**
$$\frac{\partial \rho}{\partial t} + \frac{\partial (\rho u_\beta)}{\partial x_\beta} = 0$$

Similarily one can obtain the momentum and energy conservation equations as functions of the stress tensor $\sigma_{\alpha \beta}$ and the heat flux tensor $q_\beta$ which depend on $f$.

To obtain the final Navier Stokes equations one must perform a Chapsman Enskog analysis which is for now not described here.

### TODO
- [ ] Add derivation for Momentum and energy conservation
- [ ] Add Chapsman Enskog analysis and H Therorem.
