import RealSoundUke as rs

rec = rs.record(3, 2000)

rec.plot()

fft = rec.fft()

fft.plot()

xs = fft.getukefreqs()
print(xs)