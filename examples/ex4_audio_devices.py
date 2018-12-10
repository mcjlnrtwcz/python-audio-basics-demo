import sounddevice as sd


print(sd.query_devices())
device_idx = input()
sd.default.device = device_idx  # Or iterable
