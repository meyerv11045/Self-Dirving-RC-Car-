# Self-Driving-RC-Car
### Objective: 
- Self-driving on the track 

- Stop Sign/Traffic Light Detection 

- Front Collision Avoidance 

### System Design: 
1. Input Unit
  - Pi Camera Module
  
  - Ultrasonic Sensor

2. Processing Unit
  - Train Neural Network in OpenCV
  
  - Predict Steering using trained NN
  
  - Object Detection w/ Haar Feature-Based Cascade Classifiers
  
  - Distance Measurment (monocular vision)

3. RC Control Unit
  - Arduino w/ Adafruit Motor Shield
  - Raspberry Pi 4 connects to Arduino to drive car
 
### Materials: 

- Arduino 

- RC Car 

- Short USB Connection Cable (Arduino to raspberry pi) 

- L293D Motor Drive Shield 

- Raspberry Pi 4 

- Pi Camera Module V2  

- Pi Battery Pack 

### Resources: 

- https://zhengludwig.wordpress.com/projects/self-driving-rc-car/ 

- https://github.com/hamuchiwa/AutoRCCar 

- https://blog.davidsingleton.org/nnrccar/ 

- https://arxiv.org/pdf/1910.06734.pdf 

- https://github.com/jsn5/Tensorflow-101 

- https://jpboost.com/2018/03/11/part-1-5-building-a-self-driving-rc-car/ 

- https://pdfs.semanticscholar.org/ae3c/220b8fb8613d5f2424f267018297382d92d3.pdf (monocular vision) 
