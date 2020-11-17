import numpy as np


def modify_obs(obs):
    '''
    [0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
    [0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
    [1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
    [0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
    [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
    [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
    ->
    [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    '''
    obs = obs[:, 0, :] # (envs, agents, 115) -> (envs, 115)
    obs[:, 97:108] = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

    return obs
