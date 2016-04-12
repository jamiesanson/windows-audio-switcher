int button = 2;
boolean pressed = false;

void setup() {  
  pinMode(button, INPUT);
  attachInterrupt(digitalPinToInterrupt(button), pressed, RISING);
  Serial.begin(9600);
}

void loop() {
  if(pressed){
    Serial.println("p");
    pressed = false;
  }
}

void pressed(){
  pressed = true;
}

