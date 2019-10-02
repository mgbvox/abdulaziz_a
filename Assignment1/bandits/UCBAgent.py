import numpy as np
import sys
import copy
import time
import random
import argparse
from collections import namedtuple
######################################################
Arm = namedtuple("Arm", "count reward")
#Okay what do we need to do. First, create agents. This should use command line args. 
#Also we need to create the game
class UCBAgent:
    def __init__(self):
        #self.currentState.print_board()
        self.name = "Uma the UCB Agent"
    
    def recommendArm(self, bandit, history):
        #Hey, your code goes here!
        arms = {}
        for i in range(bandit.getNumArms()):
            arms[i] = Arm(0, 0.0) 
        return False
