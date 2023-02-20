from base import RobotPolicy
import numpy as np


class RGBBCRobot1(RobotPolicy):

    """ Implement solution for Part2 below """

    def train(self, data):
        for key, val in data.items():
            print(key, val.shape)
        print("Using dummy solution for RGBBCRobot1")
        pass

    def get_action(self, obs):
    	return 0
