"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    # negative decay rate must raise an error
    with pytest.raises(ValueError):
        simulate(1000, -0.1)


def test_matches_law():
    # average over many seeds should be close to N0 * exp(-lam * t)
    N0, lam, dt, step = 1000, 0.4, 0.05, 20
    t = step * dt
    avg = np.mean([simulate(N0, lam, dt=dt, steps=step, seed=s)[step]
                   for s in range(200)])
    assert avg == pytest.approx(N0 * np.exp(-lam * t), rel=0.02)