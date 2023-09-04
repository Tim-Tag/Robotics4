#include <Servo.h>
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

String servoPos;
String strServo1Value;
String strServo3Value;
int servo1Value;
int servo3Value;
const int LED = 13;

void setup() {
  Serial.begin(9600);
  digitalWrite(LED, LOW);
  // put your setup code here, to run once:
  servo1.attach(6);
  servo2.attach(11);
  servo3.attach(9);
  servo4.attach(10);


}

void loop() {
  // put your main code here, to run repeatedly:
  servo1.write(120);
  servo2.write(106);
  servo3.write(60);
  servo4.write(128);
  servo1Value = servo1.read();
  servo3Value = servo3.read();
  strServo1Value = String(servo1Value);
  strServo3Value = String(servo3Value);
  
  if (strServo1Value.length() < 100)
  {
    servoPos = "0" + strServo1Value;
    
  }

  else
  {
    servoPos = strServo1Value;
  }

    if (strServo3Value.length() < 100)
  {
    servoPos = servoPos + "0" + strServo3Value;
    
  }

  else
  {
    servoPos = servoPos + strServo3Value;
  }
  
  
  //Serial.print("servo1 position = ");
  //Serial.println(servo1.read());
  //Serial.print("servo3 position = ");
  //Serial.println(servo3.read());
  Serial.println(servoPos);
  delay(1000);
}
