int val;
int tempPin = 1;

void setup()
{
  Serial.begin(9600);
}
void loop()
{
  val = analogRead(tempPin);
  float mv = ( val/1024.0)*5000;
  float cel = mv/90;
  float farh = (cel*9)/5 + 32;
  Serial.println(cel);
  delay(1000);
}
