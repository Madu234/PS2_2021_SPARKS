const int buttonPin4 = 11;
const int buttonPin3 = 10; 
const int buttonPin2 = 9;
const int buttonPin1 = 8;

enum Buttons {
  EV_OK,
  EV_CANCEL,
  EV_NEXT,
  EV_PREV,
  EV_NONE,
  EV_MAX_NUM
};

enum Menus {
  MENU_MAIN = 0,
  MENU_KP,
  MENU_TEMP,
  MENU_MAX_NUM
};

state_machine_handler_t* sm[MENU_MAX_NUM][EV_MAX_NUM] = 
{ //events: OK , CANCEL , NEXT, PREV
  {enter_menu, go_home, go_next, go_prev},  // MENU_MAIN
  {go_home, go_home, inc_kp, dec_kp},       // MENU_KP
  {go_home, go_home, inc_temp, dec_temp},   // MENU_TEMP
};

void state_machine(enum Menus menu, enum Buttons button)
{
  sm[menu][button]();
}

void print_menu(enum Menus menu)
{
  //lcd.clear();
  switch(menu)
  {
    case MENU_KP:
      //lcd.print("KP = ");
      //lcd.print(kp);
      break;
    case MENU_TEMP:
      //lcd.print("TEMP = ");
      //lcd.print(temp);
      break;
    case MENU_MAIN:
    default:
      //lcd.print("PS 2020");
      break;
  }
  if(current_menu != MENU_MAIN)
  {
    //lcd.setCursor(0,1);
    //lcd.print("modifica");
  }
}

void enter_menu(void)
{
  current_menu = scroll_menu;
}

void go_home(void)
{
  scroll_menu = MENU_MAIN;
  current_menu = scroll_menu;
}

void go_next(void)
{
  scroll_menu = (Menus) ((int)scroll_menu + 1);
  scroll_menu = (Menus) ((int)scroll_menu % MENU_MAX_NUM);
}

void go_prev(void)
{
  scroll_menu = (Menus) ((int)scroll_menu - 1);
  scroll_menu = (Menus) ((int)scroll_menu % MENU_MAX_NUM);
}
Menus scroll_menu = MENU_MAIN;
Menus current_menu =  MENU_MAIN;

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
