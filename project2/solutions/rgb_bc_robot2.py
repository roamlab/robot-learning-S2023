from base import RobotPolicy
import numpy as np


class RGBBCRobot2(RobotPolicy):

    """ Implement solution for Part3 below """

    def train(self, data):
        for key, val in data.items():
            print(key, val.shape)
        print("Using dummy solution for RGBBCRobot2")
        pass

    def get_action(self, obs):
    	return 0