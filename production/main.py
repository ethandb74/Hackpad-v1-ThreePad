import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# This is the confirmation: KeysScanner is for direct-to-GND wiring
# It tells the brain: "Look at pins 9, 10, and 11. When they touch GND, trigger."
keyboard.matrix = KeysScanner(
    pins=[board.D9, board.D10, board.D11],
    value_when_pressed=False, # Use False because they pull to GND
    pull=True,
)

keyboard.keymap = [
    [KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LCTRL(KC.Z)]
]

if __name__ == '__main__':
    keyboard.go()

    ## need to check not 100 percent read some docs
