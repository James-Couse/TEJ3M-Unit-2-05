/* 
 Create by: James Couse
 Created on: Oct 10 2023
 Turns a servo motor back and forth.
*/

#include <Servo.h>

Servo servoNumber1;

void setup() {
  servoNumber1.attach(7);
  servoNumber1.write(0);
}

void loop() {
  servoNumber1.write(180);
  delay(2000);
  servoNumber1.write(0);
  delay(2000);
}