import rtmidi


midi_out = rtmidi.MidiOut()
ports = midi_out.get_ports()

for idx, port in enumerate(ports):
    print(f'{idx}: {port}')
selected_port = input()

midi_out.open_port(int(selected_port))

# Program change (patterns)
pattern = 0  # pattern 1
bank = 0  # bank A
midi_out.send_message([0xC0, pattern + bank * 16])

# Control Change (Continuous Controllers)
midi_out.send_message([0xB0, 82, 127])  # Channel 1, control 82, value 127
