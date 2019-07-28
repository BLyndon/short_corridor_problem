# -*- coding: utf-8 -*-
"""IO module

Module for plots, console outputs and export to file.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import matplotlib.animation as animation


def print_staff(staff, p_history, steps):
    """
    Print parameter, initial values and results to console.
    """
    print(25*"o-" + "o\n")
    print("  Initial Probability:\t" + str(staff['ini_probability']))
    print("  Discount Factor:\t" + str(staff['discount_factor']))
    print("  Batch Size:\t\t" + str(staff['batch_size']))
    print("  Number of Episodes:\t" + str(staff['num_episodes']))
    print("  Learning Rate:\t\t" + str(staff['learning_rate']))

    print("  final mean probability:\t" +
          str(np.mean(p_history[-staff['n_mean']:])))
    print("  final mean reward:\t" +
          str(-np.mean(np.array(steps)[-staff['n_mean']:])))
    print("\n" + 25*"o-" + "o")
    print("\n")


def write_staff(staff, p_history, steps):
    """
    Append parameter, initial values and results to 'data/results'.
    """

    f = open("data/results", 'a')

    # print staff
    line = str(staff['ini_probability']) + "\t"
    line += str(staff['discount_factor']) + "\t"
    line += str(staff['batch_size']) + "\t"
    line += str(staff['num_episodes']) + "\t"
    line += str(staff['learning_rate']) + "\t"
    # print mean probability
    line += str(np.mean(p_history[-staff['n_mean']:])) + "\t"
    # print mean reward
    line += str(-np.mean(np.array(steps)[-staff['n_mean']:])) + "\n"

    f.write(line)
    f.close()


def plotter(steps, p_history, export, staff):
    """
    Plot and save learning curves.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1)
    w = savgol_filter(steps, 101, 1)

    ax1.plot(steps)
    ax1.plot(w)
    ax2.plot(p_history)

    ax1.grid(True)
    ax2.grid(True)

    ax1.set_ylabel('total steps')
    ax2.set_ylabel('prob. of right action')
    ax2.set_xlabel('episodes')

    title = "gamma=" + str(staff['discount_factor']) + ",  alpha=" + str(
        staff['learning_rate']) + ",  batch size=" + str(staff['batch_size'])

    fig.suptitle(title,
                 fontsize=16, color='gray')
    fig.suptitle(title)
    if export:
        print("export as pdf not implemented")
    plt.show()
