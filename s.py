import time
import board
import digitalio

print("press the button!")

button = digitalio.DigitalInOut(board.GPIO_P36)
button.direction = digitalio.Direction.INPUT
# use an external pullup since we don't have internal PU's
#button.pull = digitalio.Pull.UP
while  button == 0 : 
  print("got it")
