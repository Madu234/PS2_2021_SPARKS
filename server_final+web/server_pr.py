
from flask import Flask, render_template
from flask import request
from bs4 import BeautifulSoup
import smtplib, ssl
import serial

app = Flask(__name__)
ser = serial.Serial('COM3')
print(ser.name)

def send_leak_mail():
    message = """S-a detectat o inundatie!"""
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.login("proiectproiect7@gmail.com", 'Zxcv123$')
        server.sendmail('proiectproiect7@gmail.com', 'emilcioplea@yahoo.com', message) 

@app.route('/')
def index():
   
    text = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3>Proiect Sincretic 2021</h3></center></div>'
    
    Temp_serial = ser.readline()
    Temp_serial = Temp_serial.decode()
    temp = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3><p>- Temperatura este '+ Temp_serial +'</p></h3></center></div>'
    if Temp_serial.find("Inundatie!") == 0:
        send_leak_mail()

    #string_butoane = '<center><p>LED1: <button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p></center>'
    string_butoane = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><table bgcolor="gray" style="border: 1px solid black"><tr> <td style="border: 1px solid black"><button onclick="document.location=\'home\'">home</button></td>   <td style="border: 1px solid black">LED1 State:<button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></td><td style="border: 1px solid black"> LED2:<form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></td><td style="border: 1px solid black">Display:<form method=\"get\" action=\"mesaj\"><input name=\"msg\" type=\"text\"/> <input type=\"submit\" value=\"send\"></form></td>  <td style="border: 1px solid black"><button onclick="document.location=\'inund\'">Opreste modul de inundatie</button></td>  <td style="border: 1px solid black"><button onclick="document.location=\'yellow\'">LED GALBEN</button><button onclick="document.location=\'purple\'">LED PURPLE</button> </td> </tr></table></center></div>'
    
    return text+ temp+ string_butoane +render_template('index.html')
    #+ color_picker + text_form  + render_template('index.html')
    #with open("index.html") as fp:
     #  soup=BeautifulSoup(fp, 'html.parser')
    #soup = BeautifulSoup(html)#make soup that is parse-able by bs
    #soup.findAll('div')
    #s='print(soup)'
    #return soup

@app.route('/led_on')
def led_on():
    #text = 'Proiect Sincretic 2021'
    #temp = '- Temperatura este '
    ser.write("a".encode())
    #string_butoane = '<p>LED1 State:<button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p>'
    #color_picker = '<p>LED2 RGB Selector: <form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></p>'
    #text_form = '<p>Afiseaza text pe display: <form method=\"get\" action=\"mesaj\"><input name=\"msg\" type=\"text\"/> <input type=\"submit\" value=\"send\"></form></p>'
    #string_butoane_led = '<p><button onclick="document.location=\'purple\'">Opreste modul de inundatie</button> <button onclick="document.location=\'yellow\'">LED GALBEN</button></p>'
    text = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3>Proiect Sincretic 2021</h3></center></div>'
    temp_serial = ser.readline()
    temp_serial = temp_serial.decode()
    temp = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3><p>- Temperatura este '+temp_serial+' </p></h3></center></div>'

    #string_butoane = '<center><p>LED1: <button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p></center>'
    string_butoane = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><table bgcolor="gray" style="border: 1px solid black"><tr> <td style="border: 1px solid black"><button onclick="document.location=\'home\'">home</button></td>   <td style="border: 1px solid black">LED1 State:<button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></td><td style="border: 1px solid black"> LED2:<form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></td><td style="border: 1px solid black">Display:<form method=\"get\" action=\"mesaj\"><input name=\"msg\" type=\"text\"/> <input type=\"submit\" value=\"send\"></form></td>  <td style="border: 1px solid black"><button onclick="document.location=\'inund\'">Opreste modul de inundatie</button></td>  <td style="border: 1px solid black"><button onclick="document.location=\'yellow\'">LED GALBEN</button><button onclick="document.location=\'purple\'">LED PURPLE</button> </td> </tr></table></center></div>'
    return text+ temp + string_butoane + render_template('index_ap.html')

@app.route('/home')
def home():
    text = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3>Proiect Sincretic 2021</h3></center></div>'
    temp_serial = ser.readline()
    temp_serial = temp_serial.decode()
    temp = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3><p>- Temperatura este '+temp_serial+' </p></h3></center></div>'

    #string_butoane = '<center><p>LED1: <button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p></center>'
    string_butoane = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><table bgcolor="gray" style="border: 1px solid black"><tr> <td style="border: 1px solid black"><button onclick="document.location=\'home\'">home</button></td>   <td style="border: 1px solid black">LED1 State:<button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></td><td style="border: 1px solid black"> LED2:<form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></td><td style="border: 1px solid black">Display:<form method=\"get\" action=\"mesaj\"><input name=\"msg\" type=\"text\"/> <input type=\"submit\" value=\"send\"></form></td>  <td style="border: 1px solid black"><button onclick="document.location=\'inund\'">Opreste modul de inundatie</button></td>  <td style="border: 1px solid black"><button onclick="document.location=\'yellow\'">LED GALBEN</button><button onclick="document.location=\'purple\'">LED PURPLE</button> </td> </tr></table></center></div>'
    return text+ temp + string_butoane + render_template('index.html')

@app.route('/led_off')
def led_off():
    ser.write("s".encode())
    text = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3>Proiect Sincretic 2021</h3></center></div>'
    temp_serial = ser.readline()
    temp_serial = temp_serial.decode()
    temp = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3><p>- Temperatura este '+temp_serial+' </p></h3></center></div>'

    #string_butoane = '<center><p>LED1: <button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p></center>'
    string_butoane = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><table bgcolor="gray" style="border: 1px solid black"><tr> <td style="border: 1px solid black"><button onclick="document.location=\'home\'">home</button></td>   <td style="border: 1px solid black">LED1 State:<button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></td><td style="border: 1px solid black"> LED2:<form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></td><td style="border: 1px solid black">Display:<form method=\"get\" action=\"mesaj\"><input name=\"msg\" type=\"text\"/> <input type=\"submit\" value=\"send\"></form></td>  <td style="border: 1px solid black"><button onclick="document.location=\'inund\'">Opreste modul de inundatie</button></td>  <td style="border: 1px solid black"><button onclick="document.location=\'yellow\'">LED GALBEN</button><button onclick="document.location=\'purple\'">LED PURPLE</button> </td> </tr></table></center></div>'
    return text+ temp + string_butoane + render_template('index_st.html')
    

@app.route('/yellow')
def yellow():
    ser.write("p505000w".encode())
    text = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3>Proiect Sincretic 2021</h3></center></div>'
    temp_serial = ser.readline()
    temp_serial = temp_serial.decode()
    temp = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3><p>- Temperatura este '+temp_serial+' </p></h3></center></div>'

    #string_butoane = '<center><p>LED1: <button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p></center>'
    string_butoane = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><table bgcolor="gray" style="border: 1px solid black"><tr><td style="border: 1px solid black">LED1 State:<button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></td><td style="border: 1px solid black"> LED2:<form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></td><td style="border: 1px solid black">Display:<form method=\"get\" action=\"mesaj\"><input name=\"msg\" type=\"text\"/> <input type=\"submit\" value=\"send\"></form></td>  <td style="border: 1px solid black"><button onclick="document.location=\'inund\'">Opreste modul de inundatie</button></td>  <td style="border: 1px solid black"><button onclick="document.location=\'yellow\'">LED GALBEN</button><button onclick="document.location=\'purple\'">LED PURPLE</button> </td> </tr></table></center></div>'
    return text+ temp + string_butoane + render_template('index_g.html')

@app.route('/purple')
def purple():
    ser.write("p500050w".encode())
    text = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3>Proiect Sincretic 2021</h3></center></div>'
    
    temp_serial = ser.readline()
    temp_serial = temp_serial.decode()
    temp = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3><p>- Temperatura este '+temp_serial+' </p></h3></center></div>'
    #string_butoane = '<center><p>LED1: <button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p></center>'
    string_butoane = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><table bgcolor="gray" style="border: 1px solid black"><tr><td style="border: 1px solid black">LED1 State:<button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></td><td style="border: 1px solid black"> LED2:<form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></td><td style="border: 1px solid black">Display:<form method=\"get\" action=\"mesaj\"><input name=\"msg\" type=\"text\"/> <input type=\"submit\" value=\"send\"></form></td>  <td style="border: 1px solid black"><button onclick="document.location=\'inund\'">Opreste modul de inundatie</button></td>  <td style="border: 1px solid black"><button onclick="document.location=\'yellow\'">LED GALBEN</button><button onclick="document.location=\'purple\'">LED PURPLE</button> </td> </tr></table></center></div>'
    return text+ temp + string_butoane + render_template('index_p.html')

@app.route('/inund')
def inund():
    
    ser.write('c'.encode())
    text = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3>Inundatie</h3></center></div>'
    temp_serial = ser.readline()
    temp_serial = temp_serial.decode()
    temp = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3><p>- Temperatura este '+temp_serial+' </p></h3></center></div>'

    #string_butoane = '<center><p>LED1: <button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p></center>'
    string_butoane = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><table bgcolor="gray" style="border: 1px solid black"><tr><td style="border: 1px solid black">LED1 State:<button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></td><td style="border: 1px solid black"> LED2:<form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></td><td style="border: 1px solid black">Display:<form method=\"get\" action=\"mesaj\"><input name=\"msg\" type=\"text\"/> <input type=\"submit\" value=\"send\"></form></td>  <td style="border: 1px solid black"><button onclick="document.location=\'inund\'">Opreste modul de inundatie</button></td>  <td style="border: 1px solid black"><button onclick="document.location=\'yellow\'">LED GALBEN</button><button onclick="document.location=\'purple\'">LED PURPLE</button> </td> </tr></table></center></div>'
    return text+ temp + string_butoane + render_template('index_ind.html')


@app.route('/color')
def color_picker():
    color=str(request.args['colpicker'])
    red = int("0x" + color[1:3], 16) * 99/255.0
    green = int("0x" + color[3:5], 16) * 99/255.0
    blue = int("0x" + color[5:7], 16) * 99/255.0
    
    color="p" + str(int(red)).zfill(2) + str(int(green)).zfill(2) + str(int(blue)).zfill(2)
    print(color)
    ser.write(color.encode())
    text = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3>Proiect Sincretic 2021</h3></center></div>'
    temp_serial = ser.readline()
    temp_serial = temp_serial.decode()
    temp = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3><p>- Temperatura este '+temp_serial+' </p></h3></center></div>'

    #string_butoane = '<center><p>LED1: <button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p></center>'
    string_butoane = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><table bgcolor="gray" style="border: 1px solid black"><tr> <td  style="border: 1px solid black"><button onclick="document.location=\'home\'">home</button></td>  <td  style="border: 1px solid black">LED1 State:<button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></td><td style="border: 1px solid black"> LED2:<form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></td><td style="border: 1px solid black">Display:<form method=\"get\" action=\"mesaj\"><input name=\"msg\" type=\"text\"/> <input type=\"submit\" value=\"send\"></form></td>  <td style="border: 1px solid black"><button onclick="document.location=\'inund\'">Opreste modul de inundatie</button></td>  <td style="border: 1px solid black"><button onclick="document.location=\'yellow\'">LED GALBEN</button><button onclick="document.location=\'purple\'">LED PURPLE</button> </td> </tr></table></center></div>'
    return text+ temp + string_butoane + render_template('index_led2.html')

@app.route('/mesaj')
def message_parser():
    mesaj = str(request.args['msg'])
    mesaj_serial = "#" + mesaj
    ser.write(mesaj_serial.encode())
    #return "Am transmis mesajul " + mesaj
    text = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3>Mesaj este : '+ mesaj +'</h3></center></div>' 
    temp_serial = ser.readline()
    temp_serial = temp_serial.decode()
    temp = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><h3><p>- Temperatura este '+temp_serial+' </p></h3></center></div>'

    #string_butoane = '<center><p>LED1: <button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></p></center>'
    string_butoane = '<div style="background-color:#d9d9d9; width: 1500px;height: 48px;"><center><table bgcolor="gray" style="border: 1px solid black"><tr><td style="border: 1px solid black">LED1 State:<button onclick="document.location=\'led_off\'">LED OFF</button> <button onclick="document.location=\'led_on\'">LED ON</button></td><td style="border: 1px solid black"> LED2:<form method=\"get\" action=\"color\"><input name=\"colpicker\" type=\"color\"/> <input type=\"submit\" value=\"send\"></form></td><td style="border: 1px solid black">Display:<form method=\"get\" action=\"mesaj\"><input name=\"msg\" type=\"text\"/> <input type=\"submit\" value=\"send\"></form></td>  <td style="border: 1px solid black"><button onclick="document.location=\'inund\'">Opreste modul de inundatie</button></td>  <td style="border: 1px solid black"><button onclick="document.location=\'yellow\'">LED GALBEN</button><button onclick="document.location=\'purple\'">LED PURPLE</button> </td> </tr></table></center></div>'
    return text + temp + string_butoane + render_template('index_disp.html')
