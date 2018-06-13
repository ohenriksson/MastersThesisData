import numpy as np

def build_zero_array(n_axes,time):
    return list(map(lambda a: list(map(
        lambda t: 0 ,range(time))) ,range(n_axes) ))


def plot_data(axis, data, title, time):
    axis.set_title(title)
    axis.grid()
    if(len(data) > 1):
        for d in data:
            axis.plot(time, d)
    else:
        axis.plot(time,data[0])

def real_time_array(n_targets, delta_t):
    return list(map(lambda t: np.divide(t,delta_t), range(0, n_targets)))

def vel_top(data,delta_t):
    max1 = 0
    for axis in data:
        a = max(list(map(lambda d: np.abs(d),axis)))
        if a> max1: max1 = a
    return np.round(max1,4)

def acc_sum(data,delta_t):
    sum1 = 0
    for axis in data:
        sum1 += sum(map(lambda d: np.abs(d)*delta_t,axis))
    return np.round(sum1,3)

def compute_derivative(data, delta_t):
    diff = map(lambda a,b: (b-a), data[:-1],data[1:])
    derivative = map(lambda d: np.divide(d,delta_t), diff)
    return list(derivative) 

def derivative_three_point(data, delta_t):
    start = derivative_end_point(data[0], data[1], data[2], delta_t)
    end = derivative_end_point(data[-1], data[-2], data[-3], delta_t)
    midpoints = map(lambda a,b: np.divide(b-a,delta_t*2), data[:-2], data[2:])
    return [start] + list(midpoints) + [end]

def derivative_end_point(y_x1,y_x2, y_x3, h):
    num = -3*y_x1 + 4*y_x2 + -y_x3
    return np.divide(num,2*h)

def derive_all(data,delta_t):
    derivatives = []
    if(len(data) > 1):
        dataT = list(map(lambda *a: list(a), *data))
        for d in dataT:
            derivatives.append(compute_derivative(d,delta_t))
            
        return list(map(lambda *a: list(a), *derivatives))
    else :
        return [compute_derivative(data[0],delta_t)]