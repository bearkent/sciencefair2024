import RealSound as rs

rec = rs.record(3, 44100)

rec.plot()

fft = rec.fft()

fft.plot()