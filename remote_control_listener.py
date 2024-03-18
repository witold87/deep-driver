from bluetooth import *
import time
import serial
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(17, False)
GPIO.output(27, False) 
GPIO.output(22, False) 
while True:

        server_sock=BluetoothSocket( RFCOMM )
        server_sock.bind(("",PORT_ANY))
        server_sock.listen(1)
        print (' listening ')
        try:
                client_sock,address = server_sock.accept()
                print ("Accepted connection from ",address)

                while 1:
                        try:
                                data = client_sock.recv(1024)
#                               if len(data) == 0: break
                                print (type(data))
                                lr = data[:4]
                                fb = data[4:]
                                lr=int(lr.replace('\x02',''))
                                fb=int(fb.replace('\x03',''))
                                print(type(fb))
                                print(type(lr))
                                print (fb)
                                print (lr)
                                if fb > 210 and (lr < 250 and lr > 150): 
                                    print("PROSTO")
                                    GPIO.output(17, False)
                                    GPIO.output(27, False) 
                                    GPIO.output(22, True)
                                elif fb > 210 and lr >250:
                                    print("PRAWO")
                                    GPIO.output(17, False)
                                    GPIO.output(27, True) 
                                    GPIO.output(22, True)
                                elif fb > 210 and lr <150:
                                    print("LEWO")
                                    GPIO.output(17, True)
                                    GPIO.output(27, True) 
                                    GPIO.output(22, True)
                                elif fb < 150 and (lr <250 and lr >150):
                                    print("TYL")
                                    GPIO.output(17, True)
                                    GPIO.output(27, True) 
                                    GPIO.output(22, False)
                                elif fb < 190 and lr >250:
                                    print("TPRAWO")
                                    GPIO.output(17, True)
                                    GPIO.output(27, False) 
                                    GPIO.output(22, False)
                                elif fb < 190 and lr <150:
                                    print("TLEWO")
                                    GPIO.output(17, False)
                                    GPIO.output(27, True) 
                                    GPIO.output(22, False)
                                elif (fb > 150 and fb < 250):
                                    print("STOP")
                                    GPIO.output(17, False)
                                    GPIO.output(27, False) 
                                    GPIO.output(22, False)
                                #print (b'%s' % data)
                        except IOError:
                                print ("connection disconnected")
                                break
                        except KeyboardInterrupt:
                                client_sock.close()
                                sys.exit()
        except KeyboardInterrupt:
                server_sock.close()
                sys.exit()