import numpy as np
from mmof.wyscout_tools import calculate_goal_angle

# import pytest

# def test_calculate_goal_angle():
#     assert calculate_goal_angle(x=12.6, y=27.88) == pytest.approx(0.467241, 1e-6)
#     assert calculate_goal_angle(x=29.40, y=30.60) == pytest.approx(0.244517, 1e-6)
#     assert calculate_goal_angle(x=14.70, y=39.44) == pytest.approx(0.433806, 1e-6)


def test_calculate_goal_angle():
    x = np.array([12.6, 29.40, 14.70])
    y = np.array([27.88, 30.60, 39.44])
    angle = np.array([0.467241, 0.244517, 0.433806])
    assert np.allclose(calculate_goal_angle(x=x, y=y), angle, rtol=1e-6)
