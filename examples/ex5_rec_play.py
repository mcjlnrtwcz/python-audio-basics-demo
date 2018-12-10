import sounddevice as sd

length = 5
samplerate = 48000
recording = sd.rec(
    int(length * samplerate),
    samplerate=samplerate,
    channels=2,
    blocking=True
)
sd.play(recording, samplerate)
