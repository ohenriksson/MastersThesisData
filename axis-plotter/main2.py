from plotter import Plotter
import plotter_before
import plotter_raw
import os.path
import matplotlib.pyplot as plt
from pathlib import Path


def Main():
    rows = 2
    cols = 3
    fig, ax_array = plt.subplots(rows,cols,sharey='row',sharex='col')


    # dataname = 'sarmad_t0,012_complete'
    # dataname = 'axisdata_t0,5_20088_minacc'
    # dataname = 'axisdata_t0,1_7296'
    dataname = 'axisdata_t0,5_14640'
    # dataname = 'axisdata_t0,5_9576'
    rsDataPath = '../../rs-testscenario/trajectories/' +dataname + '.json'
    rsSolvedPath = '../../rs-testscenario/trajectories/' +dataname + '_solved.json'

    plotter_raw.plotter_raw(ax_array,rsDataPath,2)
    Plotter(ax_array).plot_optimized(rsSolvedPath,0)
    plt.show()

Main()