# {"delta_t":2.0,"jointArray":[[-1.200426459312439,0.14645712077617645,0.82173556089401245,-0.56252497434616089,-1.3531234264373779],[-0.3607158362865448,-0.084334187209606171,0.13280124962329865,0.038369361311197281,-0.34823125600814819],[0.020244259387254715,0.14357453584671021,0.33371725678443909,0.12079398334026337,0.013147158548235893],[-0.01142410933971405,-0.0810200572013855,-0.13784313201904297,0.054171830415725708,0.012568970210850239],[0.60809046030044556,1.1228148937225342,1.1117130517959595,1.5134974718093872,0.65783661603927612],[0.069326207041740417,0.49166315793991089,0.24828894436359406,0.13809330761432648,-4.41381020621634E-09]],"jointUpperLimits":[2.96705972839036,1.48352986419518,1.22173047639603,5.23598775598299,2.26892802759263,6.28318530717959],
# 
import numpy as np
delta_t = 0.012
jointArray = [[]]

stuff = '"jointLowerLimits":[-2.96705972839036,-1.13446401379631,-3.14159265358979,-5.23598775598299,-2.26892802759263,-6.28318530717959],"axisTranslations":[[0.0,0.0,-0.78],[-0.78,-0.32,-4.77596477990727E-17],[-1.915,-0.32,-4.77596477990727E-17],[-2.115,2.81659461379147E-17,-1.9125],[2.115,1.9125,-1.4526892872218E-16],[2.115,-2.81659461379147E-17,-1.9125],null,null,null]}'

file = open("sarmad_orig.txt")
lines = file.read().split('\n')
lines = list(map(lambda a: a.split(','), lines))

lines = lines[4:-2]

array = map(lambda a: a[0].split(' '),lines)

array = list(map(lambda a: list(filter(lambda p: len(p)>0,a)) ,array))

arraynumbers = list(map(lambda a: list(map(lambda p: float(p),a)), array))


time = list(map(lambda a: a[0], arraynumbers))
positions = list(map(lambda a: a[1:], arraynumbers))
positions_rad = list(map(lambda a: list(map(lambda p: p*np.pi/180,a)),positions))

jointarray = "[" + ''.join( str(list(map(lambda a: a,e))) + "," for e in np.transpose(positions_rad)) +"]"
bigtext = "{\"delta_t\":" +str(delta_t) + ",\"jointArray\":" +jointarray  + "}"

print(bigtext)

with open('sarmad_t0,012_complete.json', 'w') as file:
    file.seek(0)
    file.truncate()
    file.write(bigtext)