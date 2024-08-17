from config.files import Files


def load():
    with open(Files.MIDI_BLINDS_SAVE.value,"r") as file:
        shorcuts = [short for short in file.readlines()]
    return shorcuts
        
def save(keys,cc,pads):
    shortcuts = load()
    
    with open(Files.MIDI_BLINDS_SAVE.value,"w") as file:
        for key in keys.values():
            status, note, command = key.status, key.number, ",".join(key.command)
            file.write(f"{status},{note},{command}\n")
        for pad in pads.values():
            status, note, command = pad.status, pad.number, ",".join(pad.command)
            
            file.write(f"{status},{note},{command}\n")
        for c in cc.values():
            status, note, command = c.status, c.number, ",".join(c.command)
            
            file.write(f"{status},{note},{command}\n")
            