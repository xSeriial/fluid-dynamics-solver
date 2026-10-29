import numpy as np

class CartesianGrid2D:
    """
    A 2D structured Cartesian grid for CFD and LBM simulations.
    """
    def __init__(self, nx: int, ny: int, lx: float = 1.0, ly: float = 1.0):
        self.nx = nx
        self.ny = ny
        self.lx = lx
        self.ly = ly

        self.dx = lx / (nx - 1)
        self.dy = ly / (ny - 1)

        # Coordinate map with indexing='ij'
        self.x = np.linspace(0.0, lx, nx)
        self.y = np.linspace(0.0, ly, ny)
        self.X, self.Y = np.meshgrid(self.x, self.y, indexing='ij')

        # Initialize macroscopic variables
        self.u = np.zeros(shape= (nx, ny), dtype=np.float64)
        self.v = np.zeros(shape= (nx, ny), dtype=np.float64)
        self.rho = np.ones(shape= (nx, ny), dtype=np.float64)
        self.p = np.zeros(shape= (nx, ny), dtype=np.float64)

    def reset_fields(self):
        """
        Resets all fields.
        """
        self.u.fill(0.0)
        self.v.fill(0.0)
        self.rho.fill(1.0)
        self.p.fill(0.0)

    def get_node_count(self):
        """
        Returns number of gridpoints.
        """
        return self.nx * self.ny
