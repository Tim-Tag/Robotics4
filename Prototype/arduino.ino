#include <Servo.h>
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
const int flameSensor = A0;
String pump = "0";
String arm1 = "180";
String arm2 = "180";
bool moveArm1 = false;
bool moveArm2 = false;
String servoPos;
String strServo1Value;
String strServo3Value;
int servo1Value;
int servo3Value;
int flame;
const int LED = 13;

void setup() {
  Serial.begin(9600);

  pinMode(LED, OUTPUT);
  pinMode(flameSensor, INPUT);
  
  digitalWrite(LED, LOW);
  
  servo1.attach(6);
  servo2.attach(11);
  servo3.attach(9);
  servo4.attach(10);
  
  servo1.write(30);
  servo2.write(141);
  servo3.write(70);
  servo4.write(116);
}

void loop() {
  flame = 0;
  for (int i = 0; i < 10; i ++)
  {
   flame = flame + analogRead(flameSensor);
   
   if (Serial.available() > 0)
    {
    String data = Serial.readStringUntil('\n');
    if(data.substring(0,1) == "1")
    {
      arm1 = data.substring(3,6);
      arm1Write(arm1);
    }
    if (data.substring(1,2) == "1")
    {
      arm2 = data.substring(6,9);
      arm2Write(arm2);
      
    }
    if (data.substring(2,3) == "1")
    {
      pump = data.substring(9,10);
    } 
  }
  delay(100);
  }
  
     flame = flame/10;
    arm1 = String(servo1.read());
    arm2 = String(servo3.read());
  messageFunction(arm1, arm2, flame, pump);
}

void messageFunction(String first, String second, int flame, String relay)
{
  String strFirst = first;
  String strSecond = second;
  String strFlame = String(flame);
  String strRelay = relay;
  
  String message;
  if(strFirst.length() == 3)
  {
    message = strFirst;
  }
  else
  {
    message = "0" + strFirst;
  }

  if(strSecond.length() == 3)
  {
    message = message + strSecond;
  }
  else
  {
    message = message + "0" + strSecond;
  }
  if(strFlame.length() >= 3)
  {
    message = message + strFlame;
  }
  else
  {
    message = message + "0" + strFlame;
  }
  message = message + strRelay;
  Serial.println(message);
}
void moveArms(bool moveArm1, String arm1, bool moveArm2, String arm2)
{
  if (moveArm1 == true)
  {
    int arm1New = arm1.toInt();
    arm1Write(arm1New);
  }
}


void arm1Write(String arm1)
{
  int i = arm1.toInt();

  if(i< 78)
  {
    servo1.write(i);
    servo2.write(171-i);
  }
  else if(i>77 && i<118)
  {
    servo1.write(i);
    servo2.write(172-i);
  }
  else if(i >117 && i< 162)
  {
    servo1.write(i);
    servo2.write(173-i);
  }
  else if(i>161);
  {
    servo1.write(i);
    servo2.write(174-i);
  }
}

void arm2Write(String arm2)
{
  int i = arm2.toInt();
  int ffactor;
  if (i == 37)
    {
      ffactor = 191;
    }
    
    if (i > 37 && i < 44)
    {
      ffactor = 190;
    }
    if (i > 43 && i < 46)
    {
      ffactor = 189;
    }

    if (i > 45 && i < 51)
    {
      ffactor = 190;
    }

    if (i > 50 && i < 56)
    {
      ffactor = 189;
    }
    if (i > 55 && i < 61)
    {
      ffactor = 188;
    }
    if (i > 60 && i < 64)
    {
      ffactor = 187;
    }
    if (i > 63 && i < 80)
    {
      ffactor = 186;
    }
    if (i > 79 && i < 86)
    {
      ffactor = 185;
    }
    if (i > 85 && i < 97)
    {
      ffactor = 184;
    }
    if (i > 96 && i < 107)
    {
      ffactor = 183;
    }
    if (i > 106 && i < 145)
    {
      ffactor = 182;
    }
    if (i > 144 && i < 154)
    {
      ffactor = 181;
    }
    if (i > 153)
    {
      ffactor = 180;
    }
    servo3.write(i);
    servo4.write(ffactor-i);
  
}
