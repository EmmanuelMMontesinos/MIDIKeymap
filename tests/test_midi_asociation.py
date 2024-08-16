from controllers.midi_asociaton import *

def test_MIDIkeys():
    test_dispo = MIDIkeys(71,"ctrl,enter")
    assert test_dispo.number == 71
    assert test_dispo.command == ["ctrl","enter"]
    
def test_MIDIcc():
    test_dispo = MIDIkeys(71,"ctrl,enter")
    assert test_dispo.number == 71
    assert test_dispo.command == ["ctrl","enter"]

def test_MIDIPads():
    test_dispo = MIDIkeys(71,"ctrl,enter")
    assert test_dispo.number == 71
    assert test_dispo.command == ["ctrl","enter"]