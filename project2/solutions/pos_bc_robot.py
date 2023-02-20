from base import RobotPolicy
import numpy as np


class POSBCRobot(RobotPolicy):
    
    """ Implement solution for Part1 below """

    def train(self, data):
        for key, val in data.items():
            print(key, val.shape)
        print("Using dummy solution for POSBCRobot")
        pass

    def get_action(self, obs):
        return 0