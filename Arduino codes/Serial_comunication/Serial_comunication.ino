void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(6,OUTPUT);
}

void loop() {
  char bufer;
  if (Serial.available() > 0)
  {
    bufer = Serial.read();
    if (bufer == 'a'){
       analogWrite(6,0);
       
       }
    else if (bufer == 's')
       analogWrite(6,255);
  }
  
}
