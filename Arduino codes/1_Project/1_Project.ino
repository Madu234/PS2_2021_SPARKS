#include <EEPROM.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
#define MSG_MAX_LEN 32

int val;
int tempPin = 1;
String bufer;

typedef struct mesaje_nvm {
  char mesaj[MSG_MAX_LEN + 1];
  bool stare_citire;
  bool valid = false;  
} mesaje_nvm_t;

mesaje_nvm_t mesaje_ram[10];

void Read_EEPROM_Mesaje ()
{
  EEPROM.get(0, mesaje_ram);
}

void Write_EEPROM_Mesaje()
{
  EEPROM.put(0, mesaje_ram);
}

void Clear_EEPROM_Mesaje()
{
   for (int i = 0 ; i < EEPROM.length() ; i++) {
    EEPROM.write(i, 0);
  }
}

void Salveaza_Mesaj(char* msg, int len)
{
 int i=0;
 for(i = 0; i<10; i++)
 {
  if(mesaje_ram[i].valid != true)
  {
    break; 
  }
 }

 if (i==10)
 {
  i=0;
 }

 //Am gasit un loc pentru salvarea mesajului.
 memcpy(mesaje_ram[i].mesaj, msg, MSG_MAX_LEN + 1);
 //Serial.println("Mesajul a fost salvat");
 mesaje_ram[i].valid = true;
 mesaje_ram[i].stare_citire = false;
 Write_EEPROM_Mesaje();
 //Afiseaza_Mesaje();
}

void Afiseaza_Mesaje()
{
  for ( int j=0; j < 10; j++)
  {
    if (mesaje_ram[j].valid == true)
    {
      Serial.print(j);
      Serial.print(" - ");
      Serial.println(mesaje_ram[j].mesaj);
    }
    else
    {
      Serial.print(j);
      Serial.print(" - \n");
      Serial.println("GOL");
    }
    
  }
}

void Afiseaza_Mesaju(int j){
  if (mesaje_ram[j].valid == true)
    {
      Serial.print(j);
      Serial.print(" - ");
      Serial.println(mesaje_ram[j].mesaj);
    }
    else
    {
      Serial.print(j);
      Serial.print(" - \n");
      Serial.println("GOL");
    }
}

const int inundatiePin = 3;

void setup()
{
  lcd.init(); // initialize the lcd
  lcd.backlight();
  Serial.begin(9600);
  
  pinMode(5,OUTPUT); //Red
  pinMode(6,OUTPUT); //Green
  pinMode(7,OUTPUT); //Blue
  pinMode(inundatiePin, INPUT_PULLUP);
  Clear_EEPROM_Mesaje();
  Read_EEPROM_Mesaje();
  
  //Afiseaza_Mesaju(0);
  attachInterrupt(digitalPinToInterrupt(inundatiePin), Inundatie, LOW);
  
}
void Inundatie() {
    //lcd.setCursor(0, 0);
    Serial.println("Inundatie!");
    //lcd.println("modul inundat!");
    Salveaza_Mesaj("inundatie!",32); // TO DO : adauga ora
}

void loop()
{
  
  val = analogRead(tempPin);
  float mv = ( val/1024.0)*5000;
  float cel = mv/10;
  if(mesaje_ram[0].valid == true){
    Serial.println("Inundatie!");
    lcd.setCursor(0, 6);         // move cursor to   (0, 0)
    lcd.print(mesaje_ram[0].mesaj);
  }
  else{
  Serial.println(cel);
  lcd.setCursor(0, 0);         // move cursor to   (0, 0)
  lcd.print("            ");
  lcd.setCursor(0, 0);
  lcd.print(cel);
  }
  if (Serial.available() > 0)
  {
    bufer = Serial.readStringUntil('\n');
    if (bufer[0] == 'a'){
       analogWrite(7,0);
       analogWrite(6,0);
       analogWrite(5,0);
    }
    else if (bufer[0] == 's'){
      analogWrite(7,260);
      analogWrite(6,255);
      analogWrite(5,255);
    }
    else if (bufer[0] == 'p'){
      int Red,Green,Blue;
      Red = 255-10*(bufer[1]-48)-10*(bufer[2]-48); 
      Green = 255-10*(bufer[3]-48)-10*(bufer[4]-48);
      Blue = 260-10*(bufer[5]-48)-10*(bufer[6]-48);
      analogWrite(7,Blue);
      analogWrite(6,Green);
      analogWrite(5,Red);
    }
    else if (bufer[0] == '#'){
      //Serial.println(bufer = bufer.substring(1, bufer.length()));
      lcd.clear();
      lcd.setCursor(0,1); 
      lcd.print(bufer.substring(1, bufer.length()));
    }
    else if (bufer[0] == 'c'){
      Clear_EEPROM_Mesaje();
      lcd.setCursor(0,1); 
      lcd.print("Memoria golita");
      mesaje_ram[0].valid=false;
    }
  }
  delay(1000);
}
