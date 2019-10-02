
import numpy as np
import sys
import copy
import time
import random
import argparse
from collections import namedtuple
######################################################

#Okay what do we need to do. First, create agents. This should use command line args. 
#Also we need to create the game
Arm = namedtuple("Arm", "count reward")

class epsGreedyAgent:
    def __init__(self):
        #self.currentState.print_board()
        self.eps = .4
        self.name = "Eric the Epsilon Greedy Agent"
        
    def recommendArm(self, bandit, history):
        #Hey, your code goes here!
        if np.random.random() < self.eps or not history:
            return np.random.randint(0,bandit.getNumArms())
        else:
            # we need to count how many times an arm has been pulled
            # we need to calculate the comulative reward
            arms = {}
            for i in range(bandit.getNumArms()):
                arms[i] = Arm(0, 0.0)            

            for armNum, reward in history:
                arms[armNum] = Arm(arms[armNum].count + 1, arms[armNum].reward + reward)
            
            max_rate = -1.0
            best_arm = None
            for arm_key in arms.keys():
                if arms[arm_key].count == 0:
                    continue         
                reward_rate = arms[arm_key].reward / arms[arm_key].count
                if reward_rate > max_rate:
                    max_rate = reward_rate
                    best_arm = arm_key
            return best_arm
