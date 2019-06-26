# -*- coding: utf-8 -*-
"""Corridor module

This module provides the game setting. 
"""

from numpy import random


class CorridorGame:
    def __init__(self):
        self.steps = 0
        self.state = 0
        self.trajectory = []
        self.reward = -1
        print("\n##### game started!\n")

    def __del__(self):
        print("\n##### game finished!\n")

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

    def step(self, p):
        """
        Do a single step.
        """
        action = 0
        rand = random.rand()
        temp_state = self.state

        if self.state == 0:
            if rand < p:
                self.state += 1
                action = 1
        elif self.state == 1:
            if rand < p:
                self.state -= 1
                action = 1
            else:
                self.state += 1
        else:
            if rand < p:
                self.state += 1
                action = 1
            else:
                self.state -= 1

        self.trajectory.append([temp_state, action, self.reward])

    def run(self, p):
        """
        Step through the corridor until state 3 is reached.
        """
        while self.state < 3:
            self.step(p)
