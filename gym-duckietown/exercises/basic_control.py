#!/usr/bin/env python3

"""
Simple exercise to construct a controller that controls the simulated Duckiebot using pose. 
"""

import time
import sys
import argparse
import math
import numpy as np
import gym
from gym_duckietown.envs import DuckietownEnv

parser = argparse.ArgumentParser()
parser.add_argument('--env-name', default=None)
parser.add_argument('--map-name', default='map1_0')
parser.add_argument('--no-pause', action='store_true', help="don't pause on failure")
args = parser.parse_args()

if args.env_name is None:
    env = DuckietownEnv(
        map_name = args.map_name,
        domain_rand = False,
        draw_bbox = False
    )
else:
    env = gym.make(args.env_name)

obs = env.reset()
env.render()

total_reward = 0

while True:

    lane_pose = env.get_lane_pos2(env.cur_pos, env.cur_angle)
    distance_to_road_center = lane_pose.dist
    angle_from_straight_in_rads = lane_pose.angle_rad

    ######-------> Start changing the code here.
    # TODO: Decide how to calculate the speed and direction.
    ## input: current tile index, next tile index, and above lane_pose?
    ## distance_to_road_center, angle_from_straight_in_rads
    ## output: linear speed (speed) and augular speed (steering)


    ## Methods: 1. DL, need self simulation data
    # 2. RL deep Q-learning, don't need self simulation data
    # https://colab.research.google.com/drive/1alHbTSZ0uYuC6CTpzJZViMFRxzi8VghY?usp=sharing
    # https://colab.research.google.com/drive/1TrPWlRkwtBilt4LReKon9cHly80JDmA4?usp=sharing
    # milestone 1, input high level, output low level

    k_p = 10
    k_d = 1
    
    # The speed is a value between [0, 1] (which corresponds to a real speed between 0m/s and 1.2m/s)
    
    speed = 0.2 # TODO: You should overwrite this value
    
    # angle of the steering wheel, which corresponds to the angular velocity in rad/s
    steering = k_p*distance_to_road_center + k_d*angle_from_straight_in_rads # TODO: You should overwrite this value




    ######<------- end of code change
    
    obs, reward, done, info = env.step([speed, steering])
    total_reward += reward
    
    print('Steps = %s, Timestep Reward=%.3f, Total Reward=%.3f' % (env.step_count, reward, total_reward))

    env.render()

    if done:
        if reward < 0:
            print('*** CRASHED ***')
        print ('Final Reward = %.3f' % total_reward)
        break
