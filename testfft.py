import RealSound as rs

rec = rs.record(3, 5000)

rec.plot()

fft = rec.fft()

fft.plot()