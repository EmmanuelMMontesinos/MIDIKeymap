import pyautogui
import pygame.midi

STATUS_KEYS = 144
STATUS_PADS = 153
STATUS_CC = 176

class MIDIbind:
    def connect(self,status:int,note:int):
        match status:
            # Teclas
            case 144:
                print(f"Tecla presionada: {note}")
                if note in MIDIkeys.controlls.keys():
                    MIDIkeys.controlls[note].start_command()
                    return True
                else:
                    print("Sin asignar")
                    return False
            
            # Pads
            case 153:
                print(f"Pad: {note}")
                if note in MIDIPads.controlls.keys():
                    MIDIPads.controlls[note].start_command()
                    return True
                else:
                    print("Sin asignar")
                    return False

            # Sliders
            case 176:
                control = note
                print(f"Control Change detectado - cc: {control}")
                if control in MIDIcc.controlls.keys():
                    MIDIcc.controlls[control].start_command()
                    return True
                else:
                    print("Sin asignar")
                    return False
                    
    def bind(self):
        status, note = self.get_key()

        if note not in MIDIkeys.controlls.keys() and status == STATUS_KEYS:
            select = MIDIkeys(note)

        elif note not in MIDIcc.controlls.keys() and status == STATUS_CC:
            select = MIDIcc(note)

        elif note not in MIDIPads.controlls.keys() and status == STATUS_PADS:
            select = MIDIPads(note)

        self.connect(status,note)
        if select:
            return select

    def get_key(self):
        pygame.midi.init()
        input_id = pygame.midi.get_default_input_id()
        print(f"ID de entrada MIDI predeterminado: {input_id}")
        midi_input = pygame.midi.Input(1)

        check = True
        while check:
            if midi_input.poll():
                # Leer los mensajes MIDI
                midi_events = midi_input.read(10)
                for event in midi_events:
                    data = event[0]
                    status = data[0]
                    note = data[1]
                    
                
                check = False
        midi_input.close()
        pygame.midi.quit()
        return status, note


class MIDIControllers:
    def __init__(self,number:int) -> None:
        self.number = number
        
    def start_command(self):
        if self.command:
            pyautogui.hotkey(self.command)
            print(" + ".join(self.command))

    def set_command(self,command):
        self.command = [coman.lower() for coman in command.split(",")]

class MIDIkeys(MIDIControllers):

    controlls = {}

    def __init__(self,number:int) -> None:
        super().__init__(number)
        self.status = 144

    def set_command(self, command):
        super().set_command(command)
        self.update_keys()

    def update_keys(self):
        if not self.number in MIDIkeys.controlls.keys():
            MIDIkeys.controlls[self.number] = self
    
class MIDIcc(MIDIControllers):

    controlls = {}

    def __init__(self,number:int) -> None:
        super().__init__(number)
        self.status = 176

    def set_command(self, command):
        super().set_command(command)
        self.update_keys()
    
    def update_keys(self):
        if not self.number in MIDIcc.controlls.keys():
            MIDIcc.controlls[self.number] = self


class MIDIPads(MIDIControllers):

    controlls = {}

    def __init__(self,number:int) -> None:
        super().__init__(number)
        self.status = 153

    def set_command(self, command):
        super().set_command(command)
        self.update_keys()

    def update_keys(self):
        if not self.number in MIDIPads.controlls.keys():
            MIDIPads.controlls[self.number] = self

