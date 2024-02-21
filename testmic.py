import RealSound as rs

print('recording')
rec = rs.record(3, 44100)

rec.plot()