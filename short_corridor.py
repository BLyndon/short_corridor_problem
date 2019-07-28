import corridor as cr
import trainer as tr
import numpy as np
from numpy import random
import inputoutput as io
import sys


########### --- initialisation --- ###########
steps, tau, p_history, pbase_history, staff = [], [], [], [], {}

agents = ['reinforcement', 'baseline']

staff['agent'] = agents[1]

staff['ini_probability'] = np.random.rand()
staff['num_episodes'] = int(5e3)
staff['batch_size'] = 1
staff['discount_factor'] = .99
staff['learning_rate'] = 1e-5
staff['n_mean'] = int(staff['num_episodes']/10)
if staff['agent'] == 'baseline':
    w = -4.9
    staff['alpha_base'] = 1e-6

p = staff['ini_probability']

corridor = cr.CorridorGame()
training = tr.Trainer(staff)

########### --- run --- ###########
for i in range(staff['num_episodes']):
    corridor.run(p)
    steps.append(corridor.get_steps())
    tau.append(corridor.trajectory)
    p_history.append(p)

    if ((i+1) % staff['batch_size']) == 0:
        for k in range(staff['batch_size']):
            if staff['agent'] == 'reinforcement':
                p = training.REINFORCEMENT(p, tau[k])
            elif staff['agent'] == 'baseline':
                p, w = training.PG_baseline(p, w, tau[k])
        tau = []
    if p > 1 or p < 0:
        print("p ran out of bounds!")
        print("p = " + str(p))
        io.plotter(steps, p_history, False, staff)
        sys.exit(1)

    corridor.reset()

del training
del corridor

########### --- plots & prints --- ###########
io.print_staff(staff, p_history, steps)
io.write_staff(staff, p_history, steps)

savePlot = False
io.plotter(steps, p_history, savePlot, staff)
