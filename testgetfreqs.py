import RealSoundUke as rs

rec = rs.record(3, 44100)

fft = rec.fft()
ps = rs.PowerSpectrum(fft)

xs = ps.getukefreqs()

ps.plot()

