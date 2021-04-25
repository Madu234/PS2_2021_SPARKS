from flask import Flask
import serial
app = Flask(__name__)
ser = serial.Serial('COM3')
print(ser.name)
@app.route('/')
def hello_world():
    text = 'Proiect sincretic 2021'
    temp = '- Temperatura este: '
    Temp_serial = ser.readline()
    return text + temp  + Temp_serial.decode()
