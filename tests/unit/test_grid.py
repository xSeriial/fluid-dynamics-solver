import numpy as np
from common.grid import CartesianGrid2D

def test_grid_initialization():
    
    nx, ny = 51, 101
    lx, ly = 2.0, 4.0

    grid = CartesianGrid2D(nx, ny, lx, ly)

    assert grid.nx == nx
    assert grid.ny == ny
    assert grid.X.shape == (nx, ny)
    assert grid.Y.shape == (nx, ny)

    expected_dx = 2.0 / 50.0
    expected_dy = 4.0 / 100.0
    np.testing.assert_allclose(grid.dx, expected_dx)
    np.testing.assert_allclose(grid.dy, expected_dy)

def test_grid_reset():

    grid = CartesianGrid2D(10, 10)
    grid.u.fill(5.0)
    grid.v.fill(3.0)

    grid.reset_fields()

    np.testing.assert_allclose(grid.u, 0.0)
    np.testing.assert_allclose(grid.v, 0.0)
    np.testing.assert_allclose(grid.rho, 1.0)

def test_node_count():
    grid = CartesianGrid2D(9,8)
    expected = 9 * 8
    assert expected == grid.get_node_count()

