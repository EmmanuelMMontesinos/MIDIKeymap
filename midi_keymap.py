"""CLI - MIDIKeymap
"""

import pygame.midi
from controllers.midi_asociaton import *
import os

class MIDIKeymap:
    def activate(self):
        pygame.midi.init()
        input_id = pygame.midi.get_default_input_id()
        midi_input = pygame.midi.Input(1)
        try:
            while check:
                if midi_input.poll():
                    # Leer los mensajes MIDI
                    midi_events = midi_input.read(1)
                    for event in midi_events:
                        data = event[0]
                        status = data[0]
                        note = data[1]
                        value = data[2]
                        MIDIbind.connect(MIDIbind,status,note,value)
        except KeyboardInterrupt:
            print("Desactivando")
        finally:
            midi_input.close()
            pygame.midi.quit()

def clean_window():
    if os.name == "nt":
        clear = "cls"
    else:
        clear = "clear"

    os.system(f"{clear}")

def get_all_midis():
    keys = MIDIkeys.controlls
    cc = MIDIcc.controlls
    pads = MIDIPads.controlls

    if keys:
        print("Asignaciones de Teclas:")
        for note, obj in keys.items():
            print(f"{note} --> {' + '.join(obj.command).upper()}")

    if cc:
        print("Asignaciones de slider:")
        for note, obj in cc.items():
            print(f"{note} --> {' + '.join(obj.command).upper()}")

    if pads:
        print("Asignaciones de Pads:")
        for note, obj in pads.items():
            print(f"{note} --> {' + '.join(obj.command).upper()}")

    print()


if __name__ == "__main__":
    check = True
    clean_window()
    bind = MIDIbind()
    bind.load_bind()
        
    while check:
        clean_window()
        print("Bienvenido a MIDIKeymap por @emmanuelmmontesinos en github")
        get_all_midis()
        print("1 - Asignar tecla/pad/slider a comando")
        print("2 - Activar MIDIKeymap")
        print("3 - Salir")
        selection = input("")
        match selection:
            case "1":
                clean_window()
                get_all_midis()
                obj = bind.bind()
                command = input("Ponga el comando separado por ,\nEj para Ctrl + C sería: ctrl,c\n")
                obj.set_command(command)
                
            case "2":
                clean_window()
                get_all_midis()
                try:
                    print("MIDIKeymap Iniciado")
                    print("Para salir pulse Ctrl + C")
                    MIDIKeymap.activate(MIDIKeymap)

                except KeyboardInterrupt:
                    print("Desactivando MIDIKeymap")
            case "3":
                print("Cerrando Programa")
                bind.save_bind()
                break

        