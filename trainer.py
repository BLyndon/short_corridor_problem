# -*- coding: utf-8 -*-
"""Trainer module

This module provides the tools for learning the probability. 
"""
import numpy as np
import sys


class Trainer:
    def __init__(self, gamma, alpha):
        self.alpha = alpha
        self.gamma = gamma
        print("\n learning...")

    def __del__(self):
        print("\n...done!\n")

    def estG(self, R, gamma, T):
        """
        Returns a vector of estimated returns for each time step.
        """
        if T < 2:
            print("The trajectory is not valid!")
            sys.exit(1)
        else:
            G = np.zeros(T)
            for t in reversed(range(T-1)):
                G[t] = R[t+1] + gamma * G[t+1]
            return G

    def gradient(self, p, action):
        """
        Returns a vector of gradients for each time step.
        """
        grad = (p - action)/(p**2 - p)
        return grad

    def REINFORCEMENT(self, p, tau):
        """
        Policy update via REINFORCEMENT method.
        """
        tau = np.array(tau)
        T = len(tau)
        A = tau[:, 1]
        R = tau[:, 2]

        # prob = p
        # estG = self.estG(R, self.gamma, T)
        # gradient = self.gradient(p, A)
        # gammas = [self.gamma**i for i in range(T)]

        # prob += self.alpha * np.dot(gammas, gradient*estG)

        prob = p
        estG = self.estG(R, self.gamma, T)

        for t in range(T):
            prob += self.alpha * self.gamma**t * estG[t] * self.gradient(prob, A[t]) 

        return prob
        