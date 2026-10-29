# fluid-dynamics-solver
In this repository I write fluid dynamics solvers from scratch to solidify knowledge obtained during my studies.
It will start of by implementing standard Euler grid Navier Stokes solvers and LAttice Boltzmann methods and might later on feature AI extensions.

## Plan
1. Create a basic grid class
2. Build a basic LBM solver e.g. D2Q9
3. Introduce immersed boundary method
4. Integrate IBM into LBM solver
5. Build Navier Stokes solver
6. Use shared IBM module in NS solver

## TODO

- [ ] Move basic theory away from README.md
- [ ] Write Outline for NS solver
- [ ] Write Outline for LB method

### Navier Stokes equation

The Navier Stokes Equations are the governing equations of fluid transport and combine mass and momentum equation:
$$\nabla \cdot \mathbf{u} = 0$$
$$\rho \bigl( \frac{\partial \mathbf{u}}{\partial t}  + \mathbf{u} \cdot \nabla \mathbf{u}\bigr) = -\nabla p + \mu \Delta \mathbf{u} + \rho \mathbf{f}$$
The exact derivation can be found [here](theory/NS.md).

### Lattice Boltzmann method

The Lattice Boltzmann methods come from particle physics and approach the fluid transport statistically.
They work in mesoscopic space by working with a particle density equation that recovers the Navier Stokes equations in their hydrodynamic limit.

The formulation using the BGK collision operator is as follows:
$$f_i(\mathbf{x}+ \mathbf{e}_i\Delta t, t + \Delta t) - f_i(\mathbf{x},t) = - \frac{1}{\tau}[f_i(\mathbf{x},t) - f_i^{\mathrm{eq}}(\mathbf{x},t)]$$
where $f_i$ is the discrete particle distribution function with its equillibrium at $f_i^{\mathrm{eq}}$.

