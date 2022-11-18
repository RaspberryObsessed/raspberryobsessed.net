#LCD

import utime

from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x3F
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

from machine import Pin
import utime

led_aa = Pin(2,Pin.OUT)
led_bb = Pin(3,Pin.OUT)
led_cc = Pin(4,Pin.OUT)
led_dd = Pin(5,Pin.OUT)
led_ee = Pin(6,Pin.OUT)
led_ff = Pin(7,Pin.OUT)
led_gg = Pin(8,Pin.OUT)
led_hh = Pin(9,Pin.OUT)
led_ii = Pin(10,Pin.OUT)
led_jj = Pin(11,Pin.OUT)
led_kk = Pin(12,Pin.OUT)

#Clear
clear = led_aa.low()
led_bb.low()
led_cc.low()
led_dd.low()
led_ee.low()
led_ff.low()
led_gg.low()
led_hh.low()
led_ii.low()
led_jj.low()
led_kk.low()

clear

#Time Delay
delay = 0.25


#Button
button = Pin(14,Pin.IN,Pin.PULL_DOWN)

#Button2
button2 = Pin(15,Pin.IN,Pin.PULL_DOWN)

#Button3
button3 = Pin(13,Pin.IN,Pin.PULL_DOWN)

#Button4
button4 = Pin(12,Pin.IN,Pin.PULL_DOWN)

#Arrow
lcd.custom_char(1, bytearray([0x00,
      0x00,
      0x04,
      0x02,
      0x1F,
      0x02,
      0x04,
      0x00,
      0x00]))

move = 1


lcd.clear()
lcd.move_to(1,0)
lcd.putstr("1")
   
   
lcd.move_to(4,0)
lcd.putstr("2")
    
lcd.move_to(7,0)
lcd.putstr("Password")

lcd.move_to(1,1)
lcd.putstr("Temp")

lcd.move_to(7,1)
lcd.putstr("Help")


while True:    
    if button.value():
        move -=1
        utime.sleep(0.2)
        
    if button2.value():
        move +=1
        utime.sleep(0.2)
    
    if move ==1:
        lcd.move_to(0,0)
        lcd.putchar(chr(1))
        lcd.move_to(3,0)
        lcd.putstr(" ")
        lcd.move_to(6,0)
        lcd.putstr(" ")
        lcd.move_to(0,1)
        lcd.putstr(" ")
        lcd.move_to(6,1)
        lcd.putstr(" ")
        
    if move ==2:
        lcd.move_to(3,0)
        lcd.putchar(chr(1))
        lcd.move_to(0,0)
        lcd.putstr(" ")
        lcd.move_to(6,0)
        lcd.putstr(" ")
        lcd.move_to(0,1)
        lcd.putstr(" ")
        lcd.move_to(6,1)
        lcd.putstr(" ")
        
    if move ==3:
        lcd.move_to(6,0)
        lcd.putchar(chr(1))
        lcd.move_to(0,0)
        lcd.putstr(" ")
        lcd.move_to(3,0)
        lcd.putstr(" ")
        lcd.move_to(0,1)
        lcd.putstr(" ")
        lcd.move_to(6,1)
        lcd.putstr(" ")
        
    if move ==4:
        lcd.move_to(0,1)
        lcd.putchar(chr(1))
        lcd.move_to(0,0)
        lcd.putstr(" ")
        lcd.move_to(3,0)
        lcd.putstr(" ")
        lcd.move_to(6,0)
        lcd.putstr(" ")
        lcd.move_to(6,1)
        lcd.putstr(" ")
        
    if move ==5:
        lcd.move_to(6,1)
        lcd.putchar(chr(1))
        lcd.move_to(0,0)
        lcd.putstr(" ")
        lcd.move_to(3,0)
        lcd.putstr(" ")
        lcd.move_to(6,0)
        lcd.putstr(" ")
        lcd.move_to(0,1)
        lcd.putstr(" ")
        
        
    if button3.value():
        if move ==1:
            utime.sleep(0.2)
            
            lcd.clear()
            lcd.move_to(4,0)
            lcd.putstr("Program 1 is")
            lcd.move_to(6,1)
            lcd.putstr("Running")
                
            led_aa.high()
            utime.sleep(delay)
            led_bb.high()
            utime.sleep(delay)
            led_cc.high()
            utime.sleep(delay)
            led_dd.high()
            utime.sleep(delay)
            led_ee.high()
            utime.sleep(delay)
            led_ff.high()
            utime.sleep(delay)
            led_gg.high()
            utime.sleep(delay)
            led_hh.high()
            utime.sleep(delay)
            led_ii.high()
            utime.sleep(delay)
            led_jj.high()
            utime.sleep(delay)
            led_kk.high()
            utime.sleep(delay)
    
            led_aa.low()
            utime.sleep(delay)
            led_bb.low()
            utime.sleep(delay)
            led_cc.low()
            utime.sleep(delay)
            led_dd.low()
            utime.sleep(delay)    
            led_ee.low()
            utime.sleep(delay)    
            led_ff.low()
            utime.sleep(delay)    
            led_gg.low()
            utime.sleep(delay)    
            led_hh.low()
            utime.sleep(delay)    
            led_ii.low()
            utime.sleep(delay)    
            led_jj.low()
            utime.sleep(delay)    
            led_kk.low()
            machine.reset()
            
        if move ==2:
            utime.sleep(0.2)
            
            lcd.clear()
            lcd.move_to(4,0)
            lcd.putstr("Program 2 is")
            lcd.move_to(6,1)
            lcd.putstr("Running")
            led_aa.high()
            utime.sleep(delay)
            led_aa.low()
            led_bb.high()
            utime.sleep(delay)
            led_bb.low()
            led_cc.high()
            utime.sleep(delay)
            led_cc.low()
            led_dd.high()
            utime.sleep(delay)
            led_dd.low()
            led_ee.high()
            utime.sleep(delay)
            led_ee.low()
            led_ff.high()
            utime.sleep(delay)
            led_ff.low()
            led_gg.high()
            utime.sleep(delay)
            led_gg.low()
            led_hh.high()
            utime.sleep(delay)
            led_hh.low()
            led_ii.high()
            utime.sleep(delay)
            led_ii.low()
            led_jj.high()
            utime.sleep(delay)
            led_jj.low()
            led_kk.high()
            utime.sleep(delay)
            led_kk.low()
            machine.reset()
        
        if move ==3:
            utime.sleep(0.2)
            
            lcd.clear()
            import random

            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSYUVWXYZ1234567890[]{};":,./?-=+\!()'

            length = 10

            password = ''
            for c in range(length):
                password += random.choice(chars)
    
            lcd.move_to(5,0)
            lcd.putstr(f"{password}")
            utime.sleep(0.5)
            while True:
                if button3.value():
                    utime.sleep(0.3)
                    machine.reset()
                    
        if move ==4:
            lcd.clear()
            utime.sleep(0.2)
            TempSensor = machine.ADC(4)
            conversion_factor = 3.3 / 65535
            while True:
                lcd.move_to(0,1)
                lcd.putstr("                    ")
                if button3.value():
                    utime.sleep(0.3)
                    machine.reset()
                data = TempSensor.read_u16() * conversion_factor
                temperature = 27-(data-0.706)/0.001721
                lcd.move_to(0,0)
                lcd.putstr("The temperature is:")
                if button3.value():
                    utime.sleep(0.3)
                    machine.reset()
                lcd.move_to(0,1)
                lcd.putstr(f"{temperature}")
                lcd.move_to(0,2)
                lcd.putstr("*c")
                if button3.value():
                    utime.sleep(0.3)
                    machine.reset()
                utime.sleep(0.5)
                if button3.value():
                    utime.sleep(0.3)
                    machine.reset()
                    
        if move ==5:
            move = 1

            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("Were Just collecting")
            lcd.move_to(4,1)
            lcd.putstr("Some data")
            utime.sleep(.5)
            #...

            lcd.move_to(9,2)
            lcd.putstr(".")
            utime.sleep(.5)

            lcd.move_to(10,2)
            lcd.putstr(".")
            utime.sleep(.5)

            lcd.move_to(11,2)
            lcd.putstr(".")
            utime.sleep(.5)

            #Clear
            lcd.move_to(9,2)
            lcd.putstr(" ")

            lcd.move_to(10,2)
            lcd.putstr(" ")

            lcd.move_to(11,2)
            lcd.putstr(" ")
            utime.sleep(.5)

            #...

            lcd.move_to(9,2)
            lcd.putstr(".")
            utime.sleep(.5)

            lcd.move_to(10,2)
            lcd.putstr(".")
            utime.sleep(.5)

            lcd.move_to(11,2)
            lcd.putstr(".")
            utime.sleep(.5)

            #Clear
            lcd.move_to(9,2)
            lcd.putstr(" ")

            lcd.move_to(10,2)
            lcd.putstr(" ")

            lcd.move_to(11,2)
            lcd.putstr(" ")
            utime.sleep(.5)

            #...

            lcd.move_to(9,2)
            lcd.putstr(".")
            utime.sleep(.5)

            lcd.move_to(10,2)
            lcd.putstr(".")
            utime.sleep(.5)

            lcd.move_to(11,2)
            lcd.putstr(".")
            utime.sleep(.5)

            #Clear
            lcd.move_to(9,2)
            lcd.putstr(" ")

            lcd.move_to(10,2)
            lcd.putstr(" ")

            lcd.move_to(11,2)
            lcd.putstr(" ")
            utime.sleep(.5)

            #...

            lcd.move_to(9,2)
            lcd.putstr(".")
            utime.sleep(.5)

            lcd.move_to(10,2)
            lcd.putstr(".")
            utime.sleep(.5)


            lcd.clear()
            lcd.move_to(1,0)
            lcd.putstr("LED Test")
               
               
            lcd.move_to(11,0)
            lcd.putstr("Temp")
                
            lcd.move_to(1,1)
            lcd.putstr("Tips")

            while True:    
                if button.value():
                    move -=1
                    utime.sleep(0.2)
                    
                if button2.value():
                    move +=1
                    utime.sleep(0.2)
                
                if move ==1:
                    lcd.move_to(0,0)
                    lcd.putchar(chr(1))
                    lcd.move_to(10,0)
                    lcd.putstr(" ")
                    lcd.move_to(0,1)
                    lcd.putstr(" ")
                    
                if move ==2:
                    lcd.move_to(10,0)
                    lcd.putchar(chr(1))
                    lcd.move_to(0,0)
                    lcd.putstr(" ")
                    lcd.move_to(0,1)
                    lcd.putstr(" ")
                    
                if move ==3:
                    lcd.move_to(0,1)
                    lcd.putchar(chr(1))
                    lcd.move_to(10,0)
                    lcd.putstr(" ")
                    lcd.move_to(0,0)
                    lcd.putstr(" ")

                    
                    
                if button3.value():
                    if move ==1:
                        utime.sleep(0.2)
                        
                        lcd.clear()
                        lcd.move_to(4,0)
                        lcd.putstr("Program 1 is")
                        lcd.move_to(6,1)
                        lcd.putstr("Running")
                        
                        while True:
                            led_aa.high()
                            led_bb.high()
                            led_cc.high()
                            led_dd.high()
                            led_ee.high()
                            led_ff.high()
                            led_gg.high()
                            led_hh.high()
                            led_ii.high()
                            led_jj.high()
                            led_kk.high()
                            utime.sleep(2)
                            if button3.value():
                                utime.sleep(0.3)
                                machine.reset()
                            led_aa.low()
                            led_bb.low()
                            led_cc.low()
                            led_dd.low()
                            led_ee.low()
                            led_ff.low()
                            led_gg.low()
                            led_hh.low()
                            led_ii.low()
                            led_jj.low()
                            led_kk.low()
                            utime.sleep(1)
                            if button3.value():
                                utime.sleep(0.3)
                                machine.reset()

                        
                    if move ==2:
                        lcd.clear()
                        utime.sleep(0.2)
                        TempSensor = machine.ADC(4)
                        conversion_factor = 3.3 / 65535
                        while True:
                            lcd.move_to(0,1)
                            lcd.putstr("                    ")
                            if button3.value():
                                utime.sleep(0.3)
                                machine.reset()
                            data = TempSensor.read_u16() * conversion_factor
                            temperature = 27-(data-0.706)/0.001721
                            lcd.move_to(0,0)
                            lcd.putstr("The temperature is:")
                            lcd.move_to(0,1)
                            lcd.putstr(f"{temperature}")
                            lcd.move_to(0,2)
                            lcd.putstr("*c")
                            utime.sleep(0.5)
                            if button3.value():
                                utime.sleep(0.3)
                                machine.reset()
                                
                    if move ==3:
                        utime.sleep(0.2)
                        
                        lcd.clear()
                        lcd.move_to(5,0)
                        lcd.putstr("If you are")
                        lcd.move_to(0,1)
                        lcd.putstr("Experiencing errors")
                        lcd.move_to(7,2)
                        lcd.putstr("Go to:")
                        lcd.move_to(0,3)
                        lcd.putstr("tinyurl.com/mryzwnwz")
                        while True:
                            if button3.value():
                                utime.sleep(0.3)
                                machine.reset()
                
    #Shutdown button3
    
    if button4.value():
        lcd.clear()
        lcd.move_to(3,0)
        lcd.putstr("Shutting Down")
        utime.sleep(.5)
        #...

        lcd.move_to(9,2)
        lcd.putstr(".")
        utime.sleep(.5)
    
        lcd.move_to(10,2)
        lcd.putstr(".")
        utime.sleep(.5)
    
        lcd.move_to(11,2)
        lcd.putstr(".")
        utime.sleep(.5)
    
        #Clear
        lcd.move_to(9,2)
        lcd.putstr(" ")
    
        lcd.move_to(10,2)
        lcd.putstr(" ")
    
        lcd.move_to(11,2)
        lcd.putstr(" ")
        utime.sleep(.5)
    
        #...
    
        lcd.move_to(9,2)
        lcd.putstr(".")
        utime.sleep(.5)
    
        lcd.move_to(10,2)
        lcd.putstr(".")
        utime.sleep(.5)
    
        lcd.move_to(11,2)
        lcd.putstr(".")
        utime.sleep(.5)
    
        #Clear
        lcd.move_to(9,2)
        lcd.putstr(" ")
        
        lcd.move_to(10,2)
        lcd.putstr(" ")
    
        lcd.move_to(11,2)
        lcd.putstr(" ")
        utime.sleep(.5)
    
        #...
    
        lcd.move_to(9,2)
        lcd.putstr(".")
        utime.sleep(.5)
    
        lcd.move_to(10,2)
        lcd.putstr(".")
        utime.sleep(.5)
    
        lcd.move_to(11,2)
        lcd.putstr(".")
        utime.sleep(.5)
    
        #Clear
        lcd.move_to(9,2)
        lcd.putstr(" ")
    
        lcd.move_to(10,2)
        lcd.putstr(" ")
    
        lcd.move_to(11,2)
        lcd.putstr(" ")
        utime.sleep(.5)
    
        #...
    
        lcd.move_to(9,2)
        lcd.putstr(".")
        utime.sleep(.5)
    
        lcd.move_to(10,2)
        lcd.putstr(".")
        utime.sleep(.5)

    
        #Shutdown
        lcd.clear()
        lcd.backlight_off()    
        while True:
            if button4.value():
                lcd.backlight_on()
                
                #lcd
                lcd.move_to(6,0)
                lcd.putstr("Starting")
                
                #lcd ...
                
                #...

                lcd.move_to(9,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                lcd.move_to(10,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                lcd.move_to(11,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                #Clear
                lcd.move_to(9,2)
                lcd.putstr(" ")
                
                lcd.move_to(10,2)
                lcd.putstr(" ")
                
                lcd.move_to(11,2)
                lcd.putstr(" ")
                utime.sleep(.5)
                
                #...
                
                lcd.move_to(9,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                lcd.move_to(10,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                lcd.move_to(11,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                #Clear
                lcd.move_to(9,2)
                lcd.putstr(" ")
                
                lcd.move_to(10,2)
                lcd.putstr(" ")
                
                lcd.move_to(11,2)
                lcd.putstr(" ")
                utime.sleep(.5)
                
                #...
                
                lcd.move_to(9,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                lcd.move_to(10,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                lcd.move_to(11,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                #Clear
                lcd.move_to(9,2)
                lcd.putstr(" ")
                
                lcd.move_to(10,2)
                lcd.putstr(" ")
                
                lcd.move_to(11,2)
                lcd.putstr(" ")
                utime.sleep(.5)
                
                #...
                
                lcd.move_to(9,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                lcd.move_to(10,2)
                lcd.putstr(".")
                utime.sleep(.5)
                
                #restart
                machine.reset()