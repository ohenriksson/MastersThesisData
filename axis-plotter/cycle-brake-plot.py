
import matplotlib.pyplot as plt

brake_distances = [0.706,0.756,0.804,0.857,0.923]
brake_time = [0.202, 0.218, 0.221, 0.226, 0.242]
cycle_time = [13.8, 9.576, 7.776 , 6.888, 6.12]
velocity_spec = [50, 75, 100,125,150 ]

fig = plt.figure()
plt.xlabel('cycle time [s]')
ax = fig.add_subplot(111)
plt.ylabel(r'$\sum$ brake distance [m]')
ax2 = ax.twinx()
plt.ylabel(r'$\sum$ brake time [s]')

line1, = ax.plot(cycle_time,brake_distances, '--o', ms=4, lw=1, label='brake distance')
for xyz in zip(cycle_time, brake_distances,velocity_spec):           
    ax.annotate('velocity (%s%%)' % xyz[2], xy=xyz[:2], textcoords='data')

line2, = ax2.plot(cycle_time, brake_time, '-x', ms=4, lw=1, label='brake time')
for xyz in zip(cycle_time, brake_time, velocity_spec):           
    ax2.annotate('velocity (%s%%)' % xyz[2], xy=xyz[:2], textcoords='data')

plt.xlim([cycle_time[-1]-1, (cycle_time[0]*1.20)])
ax.grid()
# ax2.grid()


plt.title("Cycle time and stopping behaviour")
plt.legend([line1, line2], ['brake distance','brake time'])
plt.show()