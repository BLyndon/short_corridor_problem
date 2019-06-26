import corridor as cr
import trainer as tr
import numpy as np
from numpy import random
import inputoutput as io
import sys


########### --- initialisation --- ###########
steps, tau, p_history, staff = [], [], [], {}

staff['ini_probability'] = 0.7
staff['num_episodes'] = int(1e+5)
staff['batch_size'] = 100

staff['discount_factor'] = .99
staff['learning_rate'] = 1e-6
staff['n_mean'] = int(staff['num_episodes']/10)

p = staff['ini_probability']


corridor = cr.CorridorGame()
training = tr.Trainer(staff['discount_factor'], staff['learning_rate'])

########### --- run --- ###########
for i in range(staff['num_episodes']):

    corridor.run(p)
    steps.append(corridor.get_steps())
    tau.append(corridor.trajectory)
    p_history.append(p)

    # REINFORCEMENT method
    if ((i+1) % staff['batch_size']) == 0:
        for k in range(staff['batch_size']):
            p = training.REINFORCEMENT(p, tau[k])

        tau = []

    if p > 1 or p < 0:
        print("p ran out of bounds!")
        print("p = " + str(p))
        sys.exit(1)

    corridor.reset()

del training
del corridor

########### --- plots & prints --- ###########
io.print_staff(staff, p_history, steps)
io.write_staff(staff, p_history, steps)

savePlot = False
io.plotter(steps, p_history, savePlot, staff)
