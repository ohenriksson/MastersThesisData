import numpy as np
import json
import functions
import text

import sys
path = "../../python-robot-kinematics"
sys.path.append(path)
from kinematics import Kinematics
import dh_parameters_abb_irb6700 as dh_param

class Plotter:
    def __init__(self,ax_array):
        self.ax_array = ax_array
        return
        
    def plot_TCP(self, axis_poses, column, time_array):
        if(len(axis_poses[0]) < 6): return
        delta_t = np.divide((time_array[-1] - time_array[0]),len(time_array))
        tcp_pos_array = []
        for pose in axis_poses:
            b = Kinematics.TCPFrame(dh_param.a_array, dh_param.alfa_array,
                dh_param.d_array,
                [pose[0],pose[1],pose[2],0,pose[3],pose[4],pose[5]])
            tcp_pos = map(lambda p: p[0],np.matrix.tolist(b[0:3,3]))
            tcp_pos_array.append(list(tcp_pos))
        
        x_array = functions.compute_derivative(self.getColumn(tcp_pos_array,0),delta_t)
        y_array = functions.compute_derivative(self.getColumn(tcp_pos_array,1),delta_t)
        z_array = functions.compute_derivative(self.getColumn(tcp_pos_array,2),delta_t)
        tcp_vel_magnitude = list(map(lambda x,y,z: np.sqrt(np.power(x,2) + np.power(y,2) + np.power(z,2)), x_array, y_array, z_array))

        self.ax_array[3][column].plot(time_array[:-1], tcp_vel_magnitude)
        self.ax_array[3][column].set_title(text.tcpVelocity)
        self.ax_array[3][column].grid()
    
    @staticmethod
    def getColumn(array_2d, col):
        return list(map(lambda row: row[col],array_2d))


    def plot_optimized(self, path, colNumber):
        with open(path) as axis_data:
            data = json.load(axis_data)
            resolution = data['resolution']
            time_samples = data['N']
            n_targets = data['N_targets']
            axis_poses_original = data['optimal_poses']
            axis_vels_original= data['optimal_velocity']
            axis_accs_original= data['optimal_acceleration']
            axis_poses = data['optimal_poses_decimated']
            axis_vels = data['optimal_velocity_decimated']
            axis_accs = data['optimal_acceleration_decimated']
            axis_targets = data['ang_pos_targets']
            target_times = data['target_times']
            tcp_vel = data['TCP_vel']
            tcp_vel_original = data['TCP_vel_original']
            n_axes = data['n_axis']
            delta_t= data['time_step_orig']
            time_end = data['time_end']



        n_targets = n_targets +2
        axis_poses_original = list(map(lambda a: list(map(lambda b: b-np.pi*10,a)),axis_poses_original))

        n_axes = 6
        # axis_poses = list(map(lambda a: list(map(lambda b: b-np.pi*2,a)),axis_poses_original))
        axis_poses = axis_poses_original

        axis_zeros = functions.build_zero_array(5,time_samples)
        # axis_poses_original = [axis_poses_original[:][0]] + axis_zeros       

        if(len(axis_poses)>1):
            axis_poses = list(map(lambda *a: list(a), *axis_poses))

        axis_vels = functions.derive_all(axis_poses, delta_t)
        axis_accs = functions.derive_all(axis_vels, delta_t)

        if(len(axis_poses)>1):
            axis_vels = np.transpose(axis_vels)
            axis_accs= np.transpose(axis_accs)

        time_array = functions.real_time_array(time_samples,delta_t)
        time_array_upsampled = functions.real_time_array(time_samples,delta_t*resolution)

        # functions.plot_data(self.ax_array[0][colNumber], axis_poses, 'Ang Pos Decimated', time_array)

        functions.plot_data(self.ax_array[0][colNumber], axis_poses_original, text.position, time_array_upsampled)

        # functions.plot_data(self.ax_array[1][colNumber], axis_vels, 'Angular Velocities Decimated ' +str(functions.vel_top(axis_vels,delta_t)), time_array[:-1])

        newvel = str(functions.vel_top(axis_vels,delta_t))
        print('new top velocity: ' +newvel)
        functions.plot_data(self.ax_array[1][colNumber], axis_vels_original, text.velocity +newvel, time_array_upsampled[:-1])

        newacc = str(functions.acc_sum(axis_accs,delta_t));
        print('new acc sum: ' +newacc)
        # functions.plot_data(self.ax_array[2][colNumber], axis_accs, 'Angular Acceleration ' +newacc, time_array[:-2])
        functions.plot_data(self.ax_array[2][colNumber], axis_accs_original, text.acceleration +str(functions.acc_sum(axis_accs_original,delta_t/resolution)), time_array_upsampled[:-2])

        # for k,t in enumerate(target_times):
        #     self.ax_array[0][colNumber].scatter(t/(delta_t*resolution), axis_targets[0][k])

        # for k,t in enumerate(target_times):
        #    self.ax_array[0][colNumber+1].scatter(t/(delta_t*resolution), axis_targets[0][k])

        if(len(axis_poses_original) > 1):
            # self.plot_TCP(axis_poses, colNumber, time_array)
            self.plot_TCP(np.transpose(axis_poses_original), colNumber,time_array_upsampled)

