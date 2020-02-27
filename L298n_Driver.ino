//Motor A pins (enableA = enable mtoor, pinA1 = forward, pinA2 = backward)
int enableA = 11;
int pinA1 = 6;
int pinA2 = 5;

//Motor B pins (enabledB = enable motor, pinB1 = forward, pinB2 = backward)
int enableB = 10;
int pinB1 = 4;
int pinB2 = 3;

boolean test = true
boolean production = false

void setup() {
  pinMode(enableA,OUTPUT);
  pinMode(pinA1,OUTPUT);
  pinMode(pinA2,OUTPUT);

  pinMode(enableB,OUTPUT);
  pinMode(pinB1,OUTPUT);
  pinMode(pinB2,OUTPUT);
}

void loop() {
  if (test) {
    test_run();
    test = false;
  }
  else if (production){
    standard_run();
  }
}

void test_run(){
   delay(2000);
   enableMotors();
   forward(200);
   backward(200);
   left(400);
   coast(200);
   right(400);
   coast(200);
}

void standard_run(){
  
}

//Define the high-level H-bridge  commands
void enableMotors(){
  motorAOn();
  motorBOn();  
}

void disableMotors(){
  motorAOff();
  motorBOff();
}

void forward(int time){  

}

void backward(int time){

}

void left(int time){
  
}

void right(int time){
  
}

void coast(int time){
  
}

//Define low-level H-bridge commands
void motorAOn(){
  digitalWrite(enableA,HIGH);  
}
void motorBOn(){
  digitalWrite(enableB,HIGH);  
}

void motorAOff(){
  digitalWrite(enableA,LOW);
}
void motorBOff(){
  digitalWrite(enableB,LOW);  
}

void motorAForward(){
  
}
void motorABackward(){
  
}

void motorBForward(){
  
}
void motorBBackward(){

}
}




