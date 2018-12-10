import rtmidi


midi_out = rtmidi.MidiOut()
ports = midi_out.get_ports()

for idx, port in enumerate(ports):
    print(f'{idx}: {port}')
selected_port = input()

midi_out.open_port(int(selected_port))
print(midi_out.is_port_open())
