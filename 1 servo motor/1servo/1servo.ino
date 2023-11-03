#include <Servo.h>

Servo servo;
int servoPin = 9; // Use any available PWM pin

void setup() {
  servo.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int pos = Serial.parseInt();
    if (pos >= 0 && pos <= 180) {
      servo.write(pos);
    }
  }
}
