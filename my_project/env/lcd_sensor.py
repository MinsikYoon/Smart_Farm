from RPLCD.i2c import CharLCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x26)
lcd.clear()

    
lcd.cursor_pos=(1,0)
lcd.write_string('Hello, World!')