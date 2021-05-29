const int inundatiePin = 3;
void setup()
{
  //lcd.init(); // initialize the lcd
  //lcd.backlight();
  Serial.begin(9600);
  
  pinMode(5,OUTPUT); //Red
  pinMode(6,OUTPUT); //Green
  pinMode(7,OUTPUT); //Blue
  pinMode(inundatiePin, INPUT_PULLUP);
  //Clear_EEPROM_Mesaje();
  //Read_EEPROM_Mesaje();
  
  //Afiseaza_Mesaju(0);
  attachInterrupt(digitalPinToInterrupt(inundatiePin), Inundatie, LOW);
  
}
void loop(){}
void Inundatie() {
    //lcd.setCursor(0, 0);
    Serial.println("Inundatie!");
    //lcd.println("modul inundat!");
    //Salveaza_Mesaj("inundatie!",32); // TO DO : adauga ora
}
