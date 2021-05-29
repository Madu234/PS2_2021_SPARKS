const int buttonPin4 = 11;
const int buttonPin3 = 10; 
const int buttonPin2 = 9;
const int buttonPin1 = 8;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin1, INPUT);
  digitalWrite(buttonPin4,LOW);
  digitalWrite(buttonPin3,LOW);
  digitalWrite(buttonPin2,LOW);
  digitalWrite(buttonPin1,LOW);
  attachInterrupt(digitalPinToInterrupt(buttonPin4), fbuttonPin4, RISING);
  attachInterrupt(digitalPinToInterrupt(buttonPin3), fbuttonPin3, RISING);
  attachInterrupt(digitalPinToInterrupt(buttonPin2), fbuttonPin2, RISING);
  attachInterrupt(digitalPinToInterrupt(buttonPin1), fbuttonPin1, RISING);
}

void loop() {
  if (digitalRead(buttonPin4))
  Serial.println("Butonul4!");
  delay(100);
}
void fbuttonPin4() {
  Serial.println("Butonul4!");
}
void fbuttonPin3() {
  Serial.println("Butonul3!");
}
void fbuttonPin2() {
  Serial.println("Butonul2!");
}
void fbuttonPin1() {
  Serial.println("Butonul1!");
}
