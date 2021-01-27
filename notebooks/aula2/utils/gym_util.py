import warnings
from contextlib import contextmanager

import gym.spaces as spaces
import numpy as np
from gym.wrappers import TimeAwareObservation


@contextmanager
def suppress_box_precision_warning():
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore", message=".*Box bound precision.*", module="gym.logger"
        )
        yield


class TimeAwareWrapper(TimeAwareObservation):
    """Add relative timestep specific to CartPole."""

    @suppress_box_precision_warning()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        high = np.array(
            [
                self.x_threshold * 2,
                np.inf,
                self.theta_threshold_radians * 2,
                np.inf,
                1.0,
            ],
            dtype=np.float32,
        )
        low = -high.copy()
        low[-1] = 0

        self.observation_space = spaces.Box(low, high, dtype=np.float32)

    def observation(self, observation: np.ndarray) -> np.ndarray:
        return np.append(observation, self.t / self.spec.max_episode_steps)
