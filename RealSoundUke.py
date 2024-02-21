from typing import Callable
import sounddevice as sd
import soundfile as sf
import numpy as np
# import pickleu
# from wave import open
import matplotlib.pyplot as plt 
from datetime import datetime
import asyncio
from scipy.interpolate import CubicSpline
# from fix import fix
from scipy.io.wavfile import read, write
# from os.path import dirname, join as pjoin
# from scipy.io.wavfile import write

#TODO: document all code before the fair

def record(duration: float, samplingfreq: int) -> 'Sound':
    print("recording")
    #TODO: record to float or int???
    recording = sd.rec(int(duration * samplingfreq), samplerate=samplingfreq, channels=1, dtype=float)
    sd.wait()
    return Sound(samplingfreq, recording)

def soundread(file) -> 'Sound':
    samplingfreq, ys = read(file)
    return Sound(samplingfreq, ys)


def sine(duration: float, frequency: float, samplingfreq: int, amplitude: float) -> 'Sound':
    n = int(duration*samplingfreq)
    xs = np.arange(0, n+1) / samplingfreq
    ys = amplitude*np.sin(xs*2*np.pi*frequency)
    return Sound(samplingfreq, ys)


class Sound:
    
    def __init__(self, samplingfreq: int, ys: np.array):
        self.samplingfreq = samplingfreq
        self.ys = ys
        self.xs = np.arange(0, len(ys)) / samplingfreq

        if len(self.ys) % 2 == 1:

            self.xs = self.xs[:-1]
            self.ys = self.ys[:-1]
        

    def __len__(self) -> int:
        return len(self.ys)    

    def plot(self) -> None:
        plt.plot(self.xs, self.ys)
        plt.show()  
        
    def play(self) -> None:
        print("playing audio\n")
        
        start_time = datetime.now()
        
        sd.play(self.ys, self.samplingfreq)
        sd.wait()
        
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        
    def write(self, file) -> None:
        write(file, self.samplingfreq, self.ys)

    def fft(self) -> 'FFT':
        ys = np.fft.rfft(self.ys, axis=0)
        return FFT(self.samplingfreq, ys)


class FFT:

    def __init__(self, samplingfreq: int, ys: np.array):
        self.samplingfreq = samplingfreq
        self.ys = ys
        samples = len(ys)
        #TODO: arange??
        self.xs = np.linspace(0, samples/2, samples) * (samplingfreq/samples)
        # self.xs = np.arange(0, samples/2) * (samplingfreq/samples)
        
    # def getukefreqs(self):
    #     self.indecies = []
    #     self.i=0
        
    #     for self.y in self.ys:
    #         if self.y>=3:
    #             self.indecies.append(self.xs[self.i])
    #             print(f"freq: {self.xs[self.i]}")
    #             self.i+=1
    #         else: self.i+=1
            
        # for self.val in self.indecies:
        #     if 250<=self.val<=500==False:
        #         self.indecies.remove(self.val)
        #     else: return
            
        print(self.indecies)
            
        return self.indecies
    
    def __len__(self) -> int:
        return len(self.ys) 
        
    def ifft(self) -> Sound:
        ys = np.fft.irfft(self.ys, axis=0)
        #TODO: what should the types be for sounds?! int or float?

        return Sound(self.samplingfreq, ys)
    
    def plot(self) -> None:
        plt.plot(self.xs, self.ys)
        plt.show()

    def multiply(self, f: Callable[[float],float]) -> 'FFT':
        newys = np.copy(self.ys)

        print('multiplying')

        ff = np.vectorize(f)
        newys = self.ys * ff(self.xs)
            
        return FFT(self.samplingfreq, newys)
    

class PowerSpectrum:
    
    def __init__(self, fft: FFT):
        self.xs = fft.xs
        self.ys = abs(fft.ys/len(self.xs))**2

        # the spectral density of they y values is the fft y values squared over the length of the x values squared.
    def __len__(self) -> int:
        return len(self.ys) 
    
    def plot(self) -> None:
        plt.plot(self.xs, self.ys)
        plt.show()
        
    def getukefreqs(self):
        self.indecies = []
        self.i=0
        
        for self.y in self.ys:
            if self.y>=2:
                self.indecies.append(self.xs[self.i])
                print(f"freq: {self.xs[self.i]}")
                self.i+=1
            else: self.i+=1

    #TODO: what should this be doing?
    def max(self):
        i = np.argmax(self.ys)
        x = self.xs[i]
        y = self.ys[i]
        amp = y**0.5

        return (x, y, amp)


#TODO: better name?
async def recordamps(testfreq, step, endfreq, samplingfreq, samplingtime):
    
    amps =[]
    freqs = []

    while testfreq <= endfreq:
        
        sinewave = sine(samplingtime, testfreq, samplingfreq, 1)
        
        returnvals = await asyncio.gather(
            asyncio.to_thread(Sound.play, sinewave),
            asyncio.to_thread(record, samplingtime, samplingfreq)
        )
        
        sound = returnvals[1]
        fftys = np.fft.rfft(sound.ys)
        fft = FFT(samplingfreq, fftys)
        
        powerspecturm = PowerSpectrum(fft)

        vals = powerspecturm.max()
        amps.append(vals[2][0])
        
        freqs.append(testfreq)
        
        testfreq += step
        
    amps = np.array(amps)
    freqs = np.array(freqs)
    vals = [freqs, amps]

    #TODO: save is better as a different function that takes in a filename, so that you can easily run and save multiple tests
    np.save('CallibrationValues4.npy', vals)
    
    return [freqs, amps]
async def recordampsagain(testfreq, step, endfreq, samplingfreq, samplingtime, callibrationfile):
    amps = []
    freqs = []

    vals = np.load(callibrationfile)
    xs = np.array(vals[0])
    ys = np.array(vals[1])
    ys = meaninverse(ys)
    f = cubicspline(xs, ys)
    f2 = lambda x: 0.0 if x > 20000 else f(x)

    while testfreq <= endfreq:

        amp = f2(testfreq)

        sinewave = sine(samplingtime, testfreq, samplingfreq, amp)

        returnvals = await asyncio.gather(
            asyncio.to_thread(Sound.play, sinewave),
            asyncio.to_thread(record, samplingtime, samplingfreq)
        )

        sound = returnvals[1]
        fftys = np.fft.rfft(sound.ys)
        fft = FFT(samplingfreq, fftys)

        powerspecturm = PowerSpectrum(fft)

        vals = powerspecturm.max()
        amps.append(vals[2][0])

        freqs.append(testfreq)

        testfreq += step

    amps = np.array(amps)
    freqs = np.array(freqs)
    vals = [freqs, amps]

    # TODO: save is better as a different function that takes in a filename, so that you can easily run and save multiple tests
    np.save('FixedValues1.npy', vals)

    return [freqs, amps]

async def recordampsagain2(testfreq, step, endfreq, samplingfreq, samplingtime, callibrationfile1, callibrationfile2):
    amps = []
    freqs = []

    vals1 = np.load(callibrationfile1)
    xs1 = np.array(vals1[0])
    ys1 = np.array(vals1[1])
    ys1 = meaninverse(ys1)
    f = cubicspline(xs1, ys1)
    f2 = lambda x: 0.0 if x > 20000 else f(x)

    vals2 = np.load(callibrationfile2)
    xs2 = np.array(vals2[0])
    ys2 = np.array(vals2[1])
    ys2 = meaninverse(ys2)
    f3 = cubicspline(xs2, ys2)
    f4 = lambda x: 0.0 if x > 20000 else f3(x)

    while testfreq <= endfreq:

        amp = f2(testfreq)*f3(testfreq)

        sinewave = sine(samplingtime, testfreq, samplingfreq, amp)

        returnvals = await asyncio.gather(
            asyncio.to_thread(Sound.play, sinewave),
            asyncio.to_thread(record, samplingtime, samplingfreq)
        )

        sound = returnvals[1]
        fftys = np.fft.rfft(sound.ys)
        fft = FFT(samplingfreq, fftys)

        powerspecturm = PowerSpectrum(fft)

        vals = powerspecturm.max()
        amps.append(vals[2][0])

        freqs.append(testfreq)

        testfreq += step

    amps = np.array(amps)
    freqs = np.array(freqs)
    vals = [freqs, amps]

    # TODO: save is better as a different function that takes in a filename, so that you can easily run and save multiple tests
    np.save('DoubleFixedValues1.npy', vals)

    return [freqs, amps]


def meaninverse(ys):
    #TODO: I think there is an avg func
    sums = sum(ys)
    lengths = len(ys)
    mean = sums/lengths
    #makes sure the amps are averaged to 1
    
    ys = mean/ys
    
    return ys


def cubicspline(x, y):
    return CubicSpline(x, y, bc_type='natural')

def plotspline(f):
    
    x_new = np.linspace(1, 20001, 100000)
    y_new = f(x_new)
    
    plt.plot(x_new, y_new)
    
