import corridor as cr
import trainer as tr
import numpy as np
from numpy import random
import inputoutput as io
import sys


########### --- initialisation --- ###########
steps, tau, p_history, pbase_history, staff = [], [], [], [], {}

staff['agent'] = 'basel'
#staff['agent'] = 'reinf'

staff['ini_probability'] = 0.55 #np.random.rand()
staff['num_episodes'] = int(1e5)
staff['batch_size'] = 1
staff['discount_factor'] = .9
staff['learning_rate'] = 1e-6
staff['n_mean'] = int(staff['num_episodes']/10)
if staff['agent'] == 'basel':
    w = - np.random.rand()
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
            if staff['agent'] == 'reinf':
                p = training.REINFORCEMENT(p, tau[k])
            elif staff['agent'] == 'basel':
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
