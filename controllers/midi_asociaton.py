import pyautogui
import pygame.midi
from controllers.load_config import load,save

STATUS_KEYS = 144
STATUS_PADS = 153
STATUS_CC = 176

# Bind keys and connect 
class MIDIbind:
    def load_bind(self):
        save = load()
        if len(save):
            for bind in save:
                bind = bind.split(",")
                try:
                    name,status, note, command = str(bind[0]), int(bind[1]),int(bind[2]), ",".join(bind[3:])
                    bind = [name,status,note,command]
                except Exception as e:
                    print(e)
                    return
                else:
                    self.bind(load=bind)

    def save_bind(self):
        save(MIDIkeys.controlls,MIDIcc.controlls,MIDIPads.controlls)

    def connect(self,status:int,note:int,value:int):
        match status:
            # Keys
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
                    MIDIcc.controlls[control].start_command(value)
                    return True
                else:
                    print("Sin asignar")
                    return False

    def bind(self,load=None):
        command = None
        select = None
        name = None
        if not load:
            status, note, value = self.get_key()
        else:
            name,status,note,command = load
            command = command[:-1]
            value = 50
        if status == STATUS_KEYS:
            select = MIDIkeys(note,value)

        elif status == STATUS_CC:
            select = MIDIcc(note,value)

        elif status == STATUS_PADS:
            select = MIDIPads(note,value)
        if name:
            select.name = name
        self.connect(status,note,value)
        if command and select:
            select.set_command(command)
            return select
        
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
                midi_events = midi_input.read(1)
                for event in midi_events:
                    data = event[0]
                    status = data[0]
                    note = data[1]
                    value = data[2]
                    
                
                check = False
        midi_input.close()
        pygame.midi.quit()
        return status, note, value

# Diferent types of button from the  MIDI Controler standar
class MIDIControllers:
    def __init__(self,number:int,value:int) -> None:
        self.number = number
        self.value = value
        
    def start_command(self):
        pyautogui.hotkey(self.command)
        print(" + ".join(self.command))

    def set_command(self,command):
        self.command = [coman.lower() for coman in command.split(",")]

    def all_midis(self,ui=False):
        pygame.midi.init()
        input_id = pygame.midi.get_default_input_id()
        print(f"ID de entrada MIDI predeterminado: {input_id}")
        midi_input = pygame.midi.Input(1)

        check = True
        status_, note_ = None, None
        while check:
            try:
                if midi_input.poll():
                    midi_events = midi_input.read(10)
                    for event in midi_events:
                        data = event[0]
                        status = data[0]
                        note = data[1]
                        value = data[2]
                        print(f"Status {status} - Nota {note} - Valor {value}")
                        if ui:
                            check = False
                            status_, note_ = status, note
                            break
            except KeyboardInterrupt as e:
                print(f"error: {e}")
                check = False
        pygame.midi.quit()
        return str(status_),str(note_)

# Only Piano Keys
class MIDIkeys(MIDIControllers):

    controlls = {}

    def __init__(self,number:int,value:int) -> None:
        super().__init__(number,value)
        self.status = 144

    def set_command(self, command):
        super().set_command(command)
        self.update_keys()

    def update_keys(self):
        MIDIkeys.controlls[self.number] = self

# Only Control Change/ sliders
class MIDIcc(MIDIControllers):

    controlls = {}

    def __init__(self,number:int,value:int) -> None:
        super().__init__(number,value)
        self.status = 176

    def set_command(self, command):
        super().set_command(command)
        self.update_keys()
    
    def update_keys(self):
        if not self.number in MIDIcc.controlls.keys():
            MIDIcc.controlls[self.number] = self

    def start_command(self,value):
        if self.command and len(self.command) == 1:
            command = self.command[0]
        elif self.command:
            command = self.command
        match command:
            case "scroll":
                if value > self.value:
                    self.value = value
                    pyautogui.scroll(100)
                elif value < self.value:
                    self.value = value
                    pyautogui.scroll(-100)
            case "volumen":
                if value > self.value or value == 127:
                    pyautogui.press("volumeup")
                    self.value = value
                elif value < self.value or value == 0:
                    pyautogui.press("volumedown")
                    self.value = value

            case _:
                self.value = value
                pyautogui.hotkey(self.command)
        return
# Only Pads
class MIDIPads(MIDIControllers):

    controlls = {}

    def __init__(self,number:int,value:int) -> None:
        super().__init__(number,value)
        self.status = 153

    def set_command(self, command):
        super().set_command(command)
        self.update_keys()

    def update_keys(self):
        if not self.number in MIDIPads.controlls.keys():
            MIDIPads.controlls[self.number] = self

