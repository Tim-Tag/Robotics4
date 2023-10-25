#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

//pins
const int LED = 13; // this is the built in LED pin, This is used so we can set the pin to low and therefore the LED will be turned off resulting in less power.
const int relayPin = 7;
const int sensorPin = A0;
const int servo1Pin = 5;
const int servo2Pin = 6;
const int servo3Pin = 10;
const int servo4Pin = 11;

const int messageDelay = 100; // this is the delay between every message that is sent.
String pump = "0";
String arm1 = "180";
String arm2 = "180";
String servoPos;
String strServo1Value;
String strServo3Value;

bool moveArm1 = false;
bool moveArm2 = false;

int relayState = 0;
int servo1Value;
int servo3Value;
int sensor;


void setup() {

  Serial.begin(9600);
  pinMode(LED, OUTPUT);

  pinMode(relayPin, OUTPUT);
  pinMode(sensorPin, INPUT);
  
  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
  servo3.attach(servo3Pin);
  servo4.attach(servo4Pin);
  
  digital.Write(LED, LOW);

  digitalWrite(relayPin, LOW);

  servo1.write(0);
  servo2.write(171);
  servo3.write(38);
  servo4.write(141);
}


void loop() {

  sensor = 0;
  for (int i = 0; i < 10; i ++)
  {
   sensor = sensor + analogRead(sensorPin); // read our sensor pin
   
   if (Serial.available() > 0) // Check if we have a message.
    {
      String data = Serial.readStringUntil('\n'); //read message until "\n"



      if(data.substring(0,1) == "1") // do we have message for first arm?
      {
        arm1 = data.substring(3,6);
        arm1Write(arm1);
      }


      if (data.substring(1,2) == "1") // Do we have message for second arm?
      {
        arm2 = data.substring(6,9);
        arm2Write(arm2);
      }


      if (data.substring(2,3) == "1")// Do we have message for relay?
      {
        relayState = data.substring(9,10);
      } 
    }
    delay((messageDelay/10));
  }


  sensor = sensor/10; // here we are averaging out 10 readings from our sensor taken 0.01 times every second.
  arm1 = String(servo1.read()); // read the position of the first arm and convert it to a string
  arm2 = String(servo3.read()); // read the position of the second arm and convert it to a string
  
  messageFunction(arm1, arm2, flame, relayState); // Here we are feeding our message function with the readings from both our arms, the flame sensor and our pump.
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
  if(strFlame.length() == 4)
  {
    message = message + strFlame;
  }
  else if (strFlame.length() ==3)
  {
    message = message + "0" + strFlame;
  }
  else if (strFlame.length() == 2)
  {
    message = message +"00"+ strFlame;
  }
  else
  {
    message = message + "000" + strFlame;
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
  const int arm1Corrections[] = {  0,   5,  10,  15,  20,  25,  30,  35,  40,  45,  50,  55,  60,  65,  70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140};
  const int arm2Corrections[] = {171, 166, 161, 156, 151, 146, 141, 136, 131, 126, 121, 116, 111, 106, 101, 96, 92, 87, 82, 77,  72,  67, 62,   57,  53,  48,  43,  38,  33};
  servo1.write(arm1Corrections[i]);
  servo2.write(arm2Corrections[i]);
}

void arm2Write(String arm2)
{
  int i = arm2.toInt();
  const int arm3Corrections[] = 
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
