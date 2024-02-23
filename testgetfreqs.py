import RealSoundUke as rs

rec = rs.record(3, 1000)

fft = rec.fft()
ps = rs.PowerSpectrum(fft)

xs = ps.getukefreqs()

dict = {}

# for x in xs:
#     if x  dict.keys()
#         for freq in xs:
#             if (x-15)<=freq<=(x+15):
#                 dict[x]=freq


ps.plot()

