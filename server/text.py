from flask import Flask
import serial
app = Flask(__name__)
ser = serial.Serial('COM3')
print(ser.name)
@app.route('/')
def hello_world():
    return 'Proiect sincretic 2021'
