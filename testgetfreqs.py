import RealSoundUke as rs

rec = rs.record(3, 1000)

fft = rec.fft()
ps = rs.PowerSpectrum(fft)

xs = ps.getukefreqs()

ps.plot()

