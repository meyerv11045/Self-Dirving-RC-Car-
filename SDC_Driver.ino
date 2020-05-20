/* Vikram Meyer 4/16/2020
 * Control Code for the L298n motor driver
 */

//Motor A pins (enableA = enable mtoor, pinA1 = forward, pinA2 = backward)
int enableA = 5;
int pinA1 = 6;
int pinA2 = 7;

//Motor B pins (enabledB = enable motor, pinB1 = forward, pinB2 = backward)
int enableB = 10;
int pinB1 = 8;
int pinB2 = 9;

boolean test = true;
boolean production = false;

byte input;

int fps_delay = 33; //33 ms in btw commands to account for 30 FPS 

void setup() {
  pinMode(enableA,OUTPUT);
  pinMode(pinA1,OUTPUT);
  pinMode(pinA2,OUTPUT);

  pinMode(enableB,OUTPUT);
  pinMode(pinB1,OUTPUT);
  pinMode(pinB2,OUTPUT);
   
  if (production or test) {
    Serial.begin(9600);    
  }
}

void loop() {
  if (test){ test_run();}
  else if (production){standard_run();}
  else { Serial.println("Set test or production status");}
}

void test_run(){
   delay(2000);
   
   Serial.println("Forward");
   forward(5000);
   Serial.println("Brake");
   brake(2000);
   Serial.println("Backward");
   backward(5000);
   Serial.println("Brake");
   brake(2000);
   Serial.println("Right");
   left(1000);
   Serial.println("Brake");
   brake(2000);
   Serial.println("Right");
   right(1000);
   Serial.println("Coast");
   coast(5000);
}

//Receives input from serial port during normal run when it is connected to RPI's serial port
void standard_run(){
  enableMotors();  
  input = Serial.read();
  if (input = 'w'){
    forward(fps_delay);
  }
  if (input = 's'){
    backward(fps_delay);
  }
  if (input = 'a'){
    left(fps_delay);
  }
  if (input = 'd'){
    right(fps_delay);
  }
  if (input = 'q'){
    brake(fps_delay);
  }  
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
  motorAForward();
  motorBBackward();
  delay(time);
}

void backward(int time){
  motorABackward();
  motorBBackward();
  delay(time);
}

void left(int time){
  motorABackward();
  motorBForward();
  delay(time);
}

void right(int time){
  motorAForward();
  motorBBackward();
  delay(time);
}

void brake(int time){
  motorABrake();
  motorBBrake();
  delay(time);
}

void coast(int time){
  motorACoast();
  motorBCoast();
  delay(time);
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
  digitalWrite(pinA1,HIGH);
  digitalWrite(pinA2, LOW);
}
void motorABackward(){
  digitalWrite(pinA1,LOW);
  digitalWrite(pinA2,HIGH);
}

void motorBForward(){
  digitalWrite(pinB1,HIGH);
  digitalWrite(pinB2,LOW);
}
void motorBBackward(){
  digitalWrite(pinB1,LOW);
  digitalWrite(pinB2,HIGH);
}

void motorACoast(){
  digitalWrite(pinA1,LOW);
  digitalWrite(pinA2,LOW);  
}
void motorBCoast(){
  digitalWrite(pinB1,LOW);
  digitalWrite(pinB2,LOW);
}

void motorABrake(){
  digitalWrite(pinA1,HIGH);
  digitalWrite(pinA2,HIGH);  
}
void motorBBrake(){
  digitalWrite(pinB1,HIGH);
  digitalWrite(pinB2,HIGH);  
}
