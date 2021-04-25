int val;
int tempPin = 1;
char bufer;
void setup()
{
  Serial.begin(9600);
  pinMode(6,OUTPUT);
  
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
    bufer = Serial.read();
    if (bufer == 'a')
       analogWrite(6,0);
    else if (bufer == 's')
       analogWrite(6,255);
  }
}
