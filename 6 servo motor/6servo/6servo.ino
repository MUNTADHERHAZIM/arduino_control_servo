#include <Servo.h>

Servo servo[6];
int servoPins[6] = {9, 10, 11, 6, 5, 3};  // Use any available PWM pins

void setup() {
  for (int i = 0; i < 6; i++) {
    servo[i].attach(servoPins[i]);
  }
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int positions[6];
    
    for (int i = 0; i < 6; i++) {
      positions[i] = Serial.parseInt();
      
      if (positions[i] >= 0 && positions[i] <= 180) {
        servo[i].write(positions[i]);
      }
    }
  }
}
