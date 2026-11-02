# Navier Stokes equations

This file gives a brief introduction to Navier Stokes equations, the continuum hypothesis and some basic derivations.
It also slighlty touches the idea of solid mechanichs, since the derivation is similar but this might be moved to a different file.

One important assumption is to treat a fluid as a continuum.
When considering a small fluid element with given density and volume, the continuity equation states that the net flux in and out of the element must equal zero.
In other words, everything that flows in has to flow out again, and vice versa.

$$\frac{\partial}{\partial t}\int_{\Omega} \rho \mathrm{d} \Omega = -\int_{\partial \Omega} \rho \mathbf{u} \cdot \mathrm{d}\mathbf{A}$$

Transforming the rhs. to a volume integral using divergence theorem gives

$$\frac{\partial}{\partial t} \int_{\Omega} \rho \mathrm{d} \Omega = -\int_{\Omega} \nabla \cdot (\rho\mathbf{u}) \mathrm{d}\Omega$$
Since $\Omega$ is fixed in time and chosen arbitrarily the time derivative can be moved inside the integral and the equation must hold pointwise leading to the **continuity equation**
$$\frac{\partial}{\partial t}\rho + \nabla \cdot (\rho \mathbf{u}) = 0$$

The change of momemntum can be described by the net sum of flow of momentum into and out of an arbitrarily chosen element.
Mathematically,
$$\frac{d}{dt}\int_{\Omega}\rho \mathbf{u}  \mathrm{d}\Omega = - \int_{\partial \Omega}\rho \mathbf{uu}\cdot  \mathrm{d}\mathbf{A} - \int_{\partial \Omega} p \mathrm{d}\mathbf{A} + \int_{\Omega} \mathbf{F} \mathrm{d}\Omega$$

Similarily as above the surface integrals can be rewritten to Volume integrals using the divergence theorem.
Additionally taking the time derivative into the integral gives the following
$$\int_{\Omega} \frac{\partial}{\partial t} (\rho \mathbf{u}) \mathrm{d}\Omega = - \int_{\Omega} \nabla \cdot (\rho \mathbf{uu}) + \nabla p - \mathbf{F}\mathrm{d}\Omega$$

This leads to the **Euler equation** which describes the conservation of momentum for ideal fluids without friction

$$\frac{\partial}{\partial t} (\rho \mathbf{u}) = -\nabla \cdot (\rho \mathbf{uu}) - \nabla p + \mathbf{F}$$

A similar derivation can be done with a friction term added resulting in the **Navier Stokes equations**.
This friction term is introduced into the general material dependant stress tensor.
It includes the pressure $p$ from earlier that is applied to the diagonal elements since it is isotropic.

A general stress tensor $\mathbf{\sigma}$ combines the contribution of isotropic pressure with a basic viscous stress tensor
$$\sigma_{\alpha\beta} = \eta \biggl( \frac{\partial u_\alpha}{\partial x_\beta} + \frac{\partial u_\beta}{\partial x_\alpha}\biggr) + \zeta\delta_{\alpha\beta} \frac{\partial u_\gamma}{\partial x_\gamma} - p\delta_{\alpha\beta}$$
where $\eta$ is a shear stress coefficient and $\zeta$ volumetric stress coefficient, $\delta$ the Kronecker-delta corresponding to a unit matrix.

At this point index notation is very useful to distinct the different tensors.
Separation of the stress tensor into viscous shear and normal stress and assuming constant stress coefficients  yields the **Navier Stokes equaitons** when plugging into the momentum equation
$$\rho \biggl( \frac{\partial u_\alpha}{\partial t} + \frac{\partial u_\alpha}{\partial x_ \beta} u_\beta\biggr) = -\frac{\partial p}{\partial x_\alpha} + \eta \frac{\partial^2 u_\alpha}{\partial x_\beta \partial x_\beta} + \biggl( \eta_B + \frac{\eta}{3}\biggr)\frac{\partial^2 u_\beta}{\partial x_\alpha \partial x_\beta} + F_\alpha$$

Assuming **incompressibility** and $\rho=\text{const}$ reduces the continuity and momentum equationsto the following

$$\frac{\partial u_\alpha}{\partial x_\alpha} = 0$$
$$\rho \biggl( \frac{\partial u_\alpha}{\partial t} + \frac{\partial u_\alpha}{\partial x_\beta} u_\beta \biggr) = - \frac{\partial p}{\partial x_\alpha} + \eta \frac{\partial^2 u_\alpha}{\partial x_\beta \partial x_\beta} + F_\alpha$$

As long as the fluid is considered to be a continuum, and the fluid assumed to be compressible those equations govern there behaviour.

An important concept is the Reynoldy similarty.
To flows that have the same Reynolds number $\text{Re} = \frac{ul}{\nu}$ are considered to be equal up to some scaling parameters.
This can be shown by using non-dimensional analysis on the NSE.
The only relevant parameter that remains is the Reynoldy number.

The Reynolds similarity comes in very handy, because we can tweek dimension parameters in order to simulate correct fluid behaviour in a feasible context.




Those equations can be solved numerically to yield very good results for a lot of different problems.

However to solve them numerically for larger problems a few assumptions have to be made for the non linear term in order to not exceed computational limitations.
This is where turbulence modelling comes in.
Different modelling scales exist, from large scale modeling in RANS equations over Large Eddy simulations (LES) where small eddies are modelled, and larger ones are resolved or fully resolved direct numerical simulations (DNS). The needed time and space scales vary strongly among these and so do the computational expenses.

### TODO
- [ ] Add project relevant theory information about which modelling is implemented. Most likely RANS.