import numpy as np
import matplotlib.pyplot as plt
import json
import functions
import text
from plotter import Plotter


def plotter_raw(ax_array,path,col):

    with open(path) as raw_data:
        data = json.load(raw_data)
        truth = data['jointArray']
        #truth = data['theTruth']
        delta_t = data['delta_t']
        # n_axes = len(truth)
        time_samples = list(map(lambda a: len(a), truth))[0] + 2


    axis_zeros = functions.build_zero_array(5,time_samples)
    # truth= [truth[:][0]] + axis_zeros       

    n_axes = 6
    all_axis_poses = list(map(lambda *a: list(a), *truth))
    all_axis_poses = [all_axis_poses[0][:]] + all_axis_poses + [all_axis_poses[-1][:]]
    axis_vels = functions.derive_all(all_axis_poses, delta_t)
    axis_accs = functions.derive_all(axis_vels, delta_t)

    time_array = functions.real_time_array(time_samples, delta_t);

    functions.plot_data(ax_array[0][col], np.transpose(all_axis_poses), text.position, time_array)

    oldvel = str(functions.vel_top(axis_vels,delta_t))
    print('old top velocity:' +oldvel)
    functions.plot_data(ax_array[1][col], np.transpose(axis_vels), text.velocity +oldvel, time_array[:-1])


    oldacc = str(functions.acc_sum(axis_accs,delta_t))
    print('old acc sum: ' +oldacc)
    functions.plot_data(ax_array[2][col], np.transpose(axis_accs), text.acceleration +oldacc, time_array[:-2])

    plotter = Plotter(ax_array)
    if(len(all_axis_poses) > 1):
        plotter.plot_TCP(all_axis_poses,col,time_array)