int val;
int tempPin = 1;
String bufer;
void setup()
{
  Serial.begin(9600);
  pinMode(5,OUTPUT); //Red
  pinMode(6,OUTPUT); //Green
  pinMode(7,OUTPUT); //Blue
}
void loop()
{
  
  val = analogRead(tempPin);
  float mv = ( val/1024.0)*5000;
  float cel = mv/90;
  float farh = (cel*9)/5 + 32;
  Serial.println(cel);
  delay(1000);
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
      analogWrite(6,270);
      analogWrite(5,255);
    }
    else if (bufer[0] == 'p'){
      int Red,Green,Blue;
      Red = 255-10*(bufer[1]-48)-10*(bufer[2]-48); 
      Green = 270-10*(bufer[3]-48)-10*(bufer[4]-48);
      Blue = 260-10*(bufer[5]-48)-10*(bufer[6]-48);
      analogWrite(7,Blue);
      analogWrite(6,Green);
      analogWrite(5,Red);
    }
  }
}
