# -*- coding: utf-8 -*-
"""Corridor module

This module provides the game setting. 
"""
from numpy import random

class CorridorGame:
    def __init__(self):
        self.reset()
        print("\n##### game started!\n")

    def __del__(self):
        print("\n##### game finished!\n")

    def __action(self, p):
        return 1 if random.rand() < p else 0

    def __reward(self, state):
        return -1 if state < 4 else 0

    def get_steps(self):
        """
        Returns number of steps.
        """
        return len(self.trajectory)

    def reset(self):
        """
        Reset state of the game.
        """
        self.steps = 0
        self.state = 0
        self.trajectory = []

    def __step(self, p):
        """
        Do a single step and save history.
        """
        action = self.__action(p)
        temp_state = self.state

        if self.state == 0:
            if action == 1:
                self.state += 1
        elif self.state == 1:
            if action == 1:
                self.state -= 1
            else:
                self.state += 1
        else:
            if action == 1:
                self.state += 1
            else:
                self.state -= 1
        
        self.trajectory.append([temp_state, action, self.__reward(self.state)])

    def run(self, p):
        """
        Step through the corridor until state 3 is reached.
        """
        while self.state < 3:
            self.__step(p)
