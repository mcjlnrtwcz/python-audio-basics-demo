from time import sleep

import rtmidi


midi_out = rtmidi.MidiOut()
ports = midi_out.get_ports()

for idx, port in enumerate(ports):
    print(f'{idx}: {port}')
selected_port = input()

midi_out.open_port(int(selected_port))

midi_out.send_message([0x90, 60, 127])  # Channel 1, C4, velocity 127
sleep(1)
midi_out.send_message([0x80, 60, 0])  # Note off
