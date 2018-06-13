	# CONST jointtarget JointTarget_1:=[[170.000007007,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	# CONST jointtarget JointTarget_2:=[[143.024262269,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	# CONST jointtarget JointTarget_3:=[[113.3049809,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	# CONST jointtarget JointTarget_4:=[[87.274335878,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	# CONST jointtarget JointTarget_5:=[[48.429291781,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	# CONST jointtarget JointTarget_6:=[[15.425917994,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	# CONST jointtarget JointTarget_7:=[[-5.037431675,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	# CONST jointtarget JointTarget_8:=[[-30.266766578,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	# CONST jointtarget JointTarget_9:=[[-58.818282132,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	# CONST jointtarget JointTarget_10:=[[-77.492415908,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	# CONST jointtarget JointTarget_11:=[[-105.198837588,85,-98.742260129,0.112841515,40.027258121,-22.258237543],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];

	# PROC Path_10()
	# 	MoveAbsJ JointTarget_1,vmax,z200,tool0\WObj:=wobj0;
	# 	MoveAbsJ JointTarget_2,vmax,z200,tool0\WObj:=wobj0;
	# 	MoveAbsJ JointTarget_3,vmax,z200,tool0\WObj:=wobj0;
	# 	MoveAbsJ JointTarget_4,vmax,z200,tool0\WObj:=wobj0;
	# 	MoveAbsJ JointTarget_5,vmax,z200,tool0\WObj:=wobj0;
	# 	MoveAbsJ JointTarget_6,vmax,z200,tool0\WObj:=wobj0;
	# 	MoveAbsJ JointTarget_7,vmax,z200,tool0\WObj:=wobj0;
	# 	MoveAbsJ JointTarget_8,vmax,z200,tool0\WObj:=wobj0;
	# 	MoveAbsJ JointTarget_9,vmax,z200,tool0\WObj:=wobj0;
	# 	MoveAbsJ JointTarget_10,vmax,z200,tool0\WObj:=wobj0;
	# 	MoveAbsJ JointTarget_11,vmax,z200,tool0\WObj:=wobj0;
	# ENDPROC

# joint discretization: 6,6,6
import matplotlib.pyplot as plt
import numpy

def calcLength(angles):
    # return list(map(lambda a: numpy.sin(a/2.0)*3.05*2, angles))
    return list(map(lambda a: a, angles))
    


#scenario 1 has big movements on axis 1
#scenario 2 is the algo, using linear trajectories
brake_time1_t0 = [0.032, 0.058, 0.081, 0.105,0.137, 0.137, 0.137, ]
brake_angles1_t0 = [0.007, 0.021, 0.043, 0.072, 0.124, 0.124, 0.124]
brake_time1_t175 = [0.065, 0.113, 0.168,  0.215, 0.290, 0.290, 0.290]
brake_angles1_t175 = [0.010, 0.039, 0.082, 0.145,0.255, 0.255, 0.256]
brake_distances1_t0 = calcLength(brake_angles1_t0)
brake_distances1_t175 = calcLength(brake_angles1_t175)

brake_time2_t0 = [0.04, 0.07,0.106 ,0.129,0.136,0.140 , 0.140 ]
brake_distances2_t0 = calcLength([0.010, 0.03,0.071, 0.108,0.124, 0.124, 0.124])
# brake_distances2_t0 = [0.140, 0.283,0.306,0.306]
brake_time2_t175 = [0.08, 0.155 ,0.213,0.265 ,0.290,0.290, 0.290 ]
brake_distances2_t175 = calcLength([0.02,0.067,0.146,0.220,0.255, 0.255, 0.255])
# brake_distances2_t175 = [0.288,0.582,0.629,0.630]
velocity_spec = [1000,2000,3000, 4000, 5000,6000, 7000]
legend = ['scenario 1, t0', 'scenario 1, t175', 'scenario 2, t0', 'scenario 2, t175']
lines = ['-x','-o','--x','--o']


def plotTime(xaxis,ygroup):
    for y in zip(ygroup,lines):
        line2 = plt.plot(xaxis, y[0], y[1], ms=4, lw=1 )


plt.subplot(2,1,1)
plt.title("Axis 1 brake scenarios")
plt.ylabel(r'max brake time [s]')
plotTime(velocity_spec, [brake_time1_t0, brake_time1_t175, brake_time2_t0, brake_time2_t175])
plt.xlabel('velocity specification [mm/s]')
plt.grid()

plt.subplot(2,1,2)
plt.ylabel(r'max angular brake distance [rad]')
plotTime(velocity_spec, [brake_distances1_t0, brake_distances1_t175, brake_distances2_t0, brake_distances2_t175] )
plt.xlabel('velocity specification [mm/s]')
plt.grid()

plt.legend(legend)
plt.show()
