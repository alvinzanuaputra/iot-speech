import pyfirmata

comport='COM4'

board=pyfirmata.Arduino(comport)

led1=board.get_pin('d:13:o')

def led(val):
    if val==1:
        led1.write(1)
    elif val==0:
        led1.write(0)

