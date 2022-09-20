import numpy as np

GOAL_WIDTH = 7.32
PITCH_LENGTH = 105
PITCH_WIDTH = 68


# def calculate_goal_angle(x, y):

#     if y < (PITCH_WIDTH - GOAL_WIDTH) / 2:
#         dy1 = (PITCH_WIDTH - GOAL_WIDTH) / 2 - y
#         dy2 = (PITCH_WIDTH + GOAL_WIDTH) / 2 - y
#         theta1 = np.arctan(dy1 / x)
#         theta2 = np.arctan(x / dy2)
#         theta = np.pi / 2 - theta1 - theta2
#     elif y < (PITCH_WIDTH + GOAL_WIDTH) / 2:
#         dy1 = y - (PITCH_WIDTH - GOAL_WIDTH) / 2
#         dy2 = (PITCH_WIDTH + GOAL_WIDTH) / 2 - y
#         theta1 = np.arctan(x / dy1)
#         theta2 = np.arctan(x / dy2)
#         theta = np.pi - theta1 - theta2
#     else:
#         dy1 = y - (PITCH_WIDTH + GOAL_WIDTH) / 2
#         dy2 = y - (PITCH_WIDTH - GOAL_WIDTH) / 2
#         theta1 = np.arctan(dy1 / x)
#         theta2 = np.arctan(x / dy2)
#         theta = np.pi / 2 - theta1 - theta2

#     return theta


def calculate_goal_angle(x, y):
    theta = np.full(x.shape, np.nan)

    bind1 = y < (PITCH_WIDTH - GOAL_WIDTH) / 2
    dy1 = (PITCH_WIDTH - GOAL_WIDTH) / 2 - y[bind1]
    dy2 = (PITCH_WIDTH + GOAL_WIDTH) / 2 - y[bind1]
    theta1 = np.arctan(dy1 / x[bind1])
    theta2 = np.arctan(x[bind1] / dy2)
    theta[bind1] = np.pi / 2 - theta1 - theta2

    bind2 = y > (PITCH_WIDTH + GOAL_WIDTH) / 2
    dy1 = y[bind2] - (PITCH_WIDTH + GOAL_WIDTH) / 2
    dy2 = y[bind2] - (PITCH_WIDTH - GOAL_WIDTH) / 2
    theta1 = np.arctan(dy1 / x[bind2])
    theta2 = np.arctan(x[bind2] / dy2)
    theta[bind2] = np.pi / 2 - theta1 - theta2

    bind3 = ~(bind1 | bind2)
    dy1 = y[bind3] - (PITCH_WIDTH - GOAL_WIDTH) / 2
    dy2 = (PITCH_WIDTH + GOAL_WIDTH) / 2 - y[bind3]
    theta1 = np.arctan(x[bind3] / dy1)
    theta2 = np.arctan(x[bind3] / dy2)
    theta[bind3] = np.pi - theta1 - theta2

    return theta


if __name__ == "__main__":
    calculate_goal_angle(x=15.75, y=35.36)
