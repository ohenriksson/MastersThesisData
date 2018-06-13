import numpy as np
import matplotlib.pyplot as plt
import json
import functions
from plotter import Plotter

def plot_originals(ax_array,path,col):

    with open(path) as axis_data:
        data = json.load(axis_data)
        time_samples = data['N_targets']
        axis_targets = data['ang_pos_targets']
        target_times = data['target_times']
        tcp_vel = data['TCP_vel']
        n_axes = data['n_axis']
        delta_t = data['time_step_orig']
        n_targets = data['N_targets']


    axis_targets = axis_targets[0:n_axes]
    axis_vels = functions.derive_all(axis_targets, delta_t)
    axis_accs = functions.derive_all(axis_vels, delta_t)

    time_array = functions.real_time_array(n_targets,delta_t);
    functions.plot_data(ax_array[0][col], axis_targets, 'Angular Positions', time_array)
    functions.plot_data(ax_array[1][col], axis_vels, 'Angular Velocity', time_array)
    functions.plot_data(ax_array[2][col], axis_accs, 'Angular Acceleration ' +str(functions.acc_sum(axis_accs,delta_t)), time_array)

    plotter = Plotter(ax_array)
    plotter.plot_TCP(axis_targets,col,time_array)