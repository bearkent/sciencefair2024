import RealSoundUke as rs
from statistics import mean

rec = rs.record(3, 1000)

fft = rec.fft()
ps = rs.PowerSpectrum(fft)

ps.plot()

freqs = ps.getukefreqs()

print(freqs)

# string1=[]
# string2=[]
# string3=[]
# string4=[]

# for val in xs:
#     if 420<val<460:
#         string1.append(val)
#     elif 310<val<350:
#         string2.append(val)
#     elif 240<val<280:
#         string3.append(val)
#     elif 370<val<410:
#         string4.append(val)
        
# print(string1)
# print(string2)
# print(string3)
# print(string4)

# string1freq=mean(string1)
# string2freq=mean(string2)
# string3freq=mean(string3)
# string4freq=mean(string4)

# print(string1freq)
# print(string2freq)
# print(string3freq)
# print(string4freq)



# dict = {}

# for x in xs:
#     if x  dict.keys()
#         for freq in xs:
#             if (x-15)<=freq<=(x+15):
#                 dict[x]=freq




