#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;

int servoPin1 = 9;
int servoPin2 = 10;
int servoPin3 = 11;

void setup() {
  servo1.attach(servoPin1);
  servo2.attach(servoPin2);
  servo3.attach(servoPin3);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int pos1, pos2, pos3;
    pos1 = Serial.parseInt();
    pos2 = Serial.parseInt();
    pos3 = Serial.parseInt();

    if (pos1 >= 0 && pos1 <= 180) {
      servo1.write(pos1);
    }

    if (pos2 >= 0 && pos2 <= 180) {
      servo2.write(pos2);
    }

    if (pos3 >= 0 && pos3 <= 180) {
      servo3.write(pos3);
    }
  }
}
