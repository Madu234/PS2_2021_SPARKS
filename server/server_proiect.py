from flask import Flask
from flask import request
import serial
app = Flask(__name__)
ser = serial.Serial('COM4')
print(ser.name)
@app.route('/')
def hello_world():
    text = 'Proiect sincretic 2021'
    temp = '  - Temperatura este: '
    Temp_serial = ser.readline()

    string_butoane = '<p><button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p>'
    color_picker = '<p>LED2 RGB Selector: <form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></p>'
    string_butoane_led = '<p><button onclick="document.location=\'purple\'">LED MOV</button> <button onclick="document.location=\'yellow\'">LED GALBEN</button></p>'

    return text + temp  + Temp_serial.decode() + string_butoane + color_picker + string_butoane_led

@app.route('/led_on')
def led_on():
    ser.write("a".encode())
    return "Am aprins ledul!"

@app.route('/yellow')
def yellow():
    ser.write("p505000w".encode())
    return "E galben"

@app.route('/purple')
def purple():
    ser.write("p500050w".encode())
    return "E mov"

@app.route('/led_off')
def led_off():
    ser.write("s".encode())
    return "Am stins ledul!"

@app.route('/color')
def color_picker():
    color=str(request.args['colpicker'])
    red = int("0x" + color[1:3], 16) * 99/255.0
    green = int("0x" + color[3:5], 16) * 99/255.0
    blue = int("0x" + color[5:7], 16) * 99/255.0
    
    color="p" + str(int(red)).zfill(2) + str(int(green)).zfill(2) + str(int(blue)).zfill(2) + "w"
    print(color)
    ser.write(color.encode())
    return "Am modificat culoarea RGB"
