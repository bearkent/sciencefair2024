import RealSoundUke as rs
from statistics import mean
from motorclass import Motor 

pinlist = [12, 13, 1, 5, 17, 18, 22, 23]

m = Motor(pinlist)

def turntime(l):
    dif1 = 440-l[0]
    dif2 = 330-l[1] #fix the add it was giving type error
    dif3 = 262-l[2]
    dif4 = 392-l[3]
    
    turn1 = 1000*dif1/40
    turn2 = 1000*dif2/40
    turn3 = 1000*dif3/40
    turn4 = 1000*dif4/40
    
    return [turn1,turn2,turn3,turn4]
    

rec = rs.record(3, 1000)

fft = rec.fft()
ps = rs.PowerSpectrum(fft)

freqs = ps.getukefreqs()

# times = turntime(freqs)
# # print(times)

# times1 = [True, times[0]]
# if times1[1]<0:
#     times1[0]=False
#     times1[1]=-times1[1]
    
# times2 = [True, times[1]]
# if times2[1]<0:
#     times2[0]=False
#     times2[1]=-times1[1]
    
# times3 = [True, times[2]]
# if times3[1]<0:
#     times3[0]=False
#     times3[1]=-times1[1]
    
# times4 = [True, times[3]]
# if times4[1]<0:
#     times4[0]=False
#     times4[1]=-times1[1]
    
# print([times1,times2,times3,times4])



print(freqs)

m.setuppins()
m.motor1(True,100)
m.motor2(True,100)
m.motor3(True,100)
m.motor4(True,100)

# m.motor1(times1[0],int(times1[1]))
# m.motor2(times2[0],int(times2[1]))
# m.motor3(times3[0],int(times3[1]))
# m.motor4(times4[0],int(times4[1]))