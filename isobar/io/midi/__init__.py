from .input import MidiIn
from .output import MidiOut

import mido

def get_midi_output_names():
    """
    Query MIDI output device names.

    Returns:
        List[str]: A list of all possible MIDI output device names.
    """
    output_names = mido.get_output_names()
    return output_names

def get_midi_input_names():
    """
    Query MIDI input device names.

    Returns:
        List[str]: A list of all possible MIDI input device names.
    """
    input_names = mido.get_input_names()
    return input_names
