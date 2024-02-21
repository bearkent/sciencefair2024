import RealSoundUke as rs

rec = rs.record(3, 1000)

fft = rec.fft()

xs = fft.getukefreqs()

fft.plot()
