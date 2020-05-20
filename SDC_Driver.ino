/* Vikram Meyer 5/19/2020
 * Control Code for the L298n motor driver on RC Car
 * Motor A- left side of car
 * Motor B- right side of car 
 * Applying high voltage to pin A1 and B1 make their motors spin CW
 * Applying high voltage to pin A2 and B2 make their motors spin CCW
 */
int BAUD_RATE = 9600;
int FPS_DELAY = 200;

//Motor A pins (enableA = enable mtoor, pinA1 = forward, pinA2 = backward)
int enableA = 5;
int pinA1 = 6;
int pinA2 = 7;

//Motor B pins (enabledB = enable motor, pinB1 = forward, pinB2 = backward)
int enableB = 10;
int pinB1 = 8;
int pinB2 = 9;

byte cmd;

void setup() {
  pinMode(enableA,OUTPUT);
  pinMode(pinA1,OUTPUT);
  pinMode(pinA2,OUTPUT);

  pinMode(enableB,OUTPUT);
  pinMode(pinB1,OUTPUT);
  pinMode(pinB2,OUTPUT);
  enableMotors();
  Serial.begin(BAUD_RATE);
}

void loop() {
  if (Serial.available() > 0){
    cmd = Serial.read();
    if (cmd == 'w'){
      forward(FPS_DELAY);
    } else if (cmd == 'a') {
      left(FPS_DELAY);  
    } else if (cmd == 'd'){
      right(FPS_DELAY);
    } else if (cmd == 'q') {
      coast(FPS_DELAY);
      disableMotors();
    } else if (cmd == 'e'){
      enableMotors();
    } else{
      coast(FPS_DELAY);
    }
  }
}

//Define the high-level H-bridge  commands
void enableMotors(){
  rightSideOn();
  leftSideOn();  
  Serial.println("Motors Enabled");
}

void disableMotors(){
  rightSideOff();
  leftSideOff();
  Serial.println("Motors Disabled");
}

void forward(int time){  
  rightSideForward();
  leftSideForward();
  Serial.println("Forward");
  delay(time);
}

void backward(int time){
  rightSideBackward();
  leftSideBackward();
  Serial.println("Backward");
  delay(time);
}

void left(int time){
  rightSideForward();
  Serial.println("Left");
  delay(time);
}

void right(int time){
  leftSideForward();
  Serial.println("Right");
  delay(time);
}

void coast(int time){
  rightSideCoast();
  leftSideCoast();
  Serial.println("Coasting");
  delay(time);
}

//Define low-level H-bridge commands
void leftSideOn(){
  digitalWrite(enableA,HIGH);  
}
void rightSideOn(){
  digitalWrite(enableB,HIGH);  
}

void leftSideOff(){
  digitalWrite(enableA,LOW);
}
void rightSideOff(){
  digitalWrite(enableB,LOW);  
}

void leftSideBackward(){
  digitalWrite(pinA1,HIGH);
  digitalWrite(pinA2,LOW);
}
void leftSideForward(){
  digitalWrite(pinA1,LOW);
  digitalWrite(pinA2,HIGH);
}

void rightSideBackward(){
  digitalWrite(pinB1,HIGH);
  digitalWrite(pinB2,LOW);
}
void rightSideForward(){
  digitalWrite(pinB1,LOW);
  digitalWrite(pinB2,HIGH);
}

void leftSideCoast(){
  digitalWrite(pinA1,LOW);
  digitalWrite(pinA2,LOW);  
}
void rightSideCoast(){
  digitalWrite(pinB1,LOW);
  digitalWrite(pinB2,LOW);  
}
