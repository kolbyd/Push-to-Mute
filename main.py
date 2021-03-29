from Sound.sound import Sound
from pynput import keyboard

global pressed
global key_to_mute

pressed = False

"""
Only thing you need to edit is the key_to_mute variable.
Uncomment the block below to view the available keys.
"""
key_to_mute = keyboard.Key.ctrl_r

# for key in keyboard.Key:
#     print('keyboard.' + str(key))
#
# exit()


def on_press(key):
    if key == globals()['key_to_mute'] and not globals()['pressed']:
        globals()['pressed'] = True
        Sound.mute()


def on_release(key):
    if key == globals()['key_to_mute'] and globals()['pressed']:
        globals()['pressed'] = False
        Sound.mute()


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print(Sound.current_volume())
    listener.join()
