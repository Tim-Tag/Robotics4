#include <Servo.h>
Servo turn;
Servo esc;

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;


const int LED = 13;
const int pump = 7;
const int servo1Pin = 5;
const int servo2Pin = 6;
const int servo3Pin = 10;
const int servo4Pin = 11;

const int arm1Corrections[] = {  0,   5,  10,  15,  20,  25,  30,  35,  40,  45,  50,  55,  60,  65,  70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140};
const int arm2Corrections[] = {171, 166, 161, 156, 151, 146, 141, 136, 131, 126, 121, 116, 111, 106, 101, 96, 92, 87, 82, 77,  72,  67, 62,   57,  53,  48,  43,  38,  33};

const int arm3Corrections[] = { 38,  45,  50,  55,  60,  65, 70,  75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165};
const int arm4Corrections[] = {141, 134, 128, 122, 117, 109, 104, 99, 93, 88, 82, 78,  72,  66,  61,  57,  52,  47,  42,  35,  29,  24,  19,  12,   6,   1};

String message;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);

  pinMode(pump, OUTPUT);
  digitalWrite(pump, LOW);

  esc.attach(3);
  turn.attach(9);

  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
  servo3.attach(servo3Pin);
  servo4.attach(servo4Pin);

  servo1.write(0);
  servo2.write(171);
  servo3.write(38);
  servo4.write(141);
  
  turn.write(90);
  esc.write(90);

  
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    String data = Serial.readStringUntil('\n');
    if (data.substring(0,1) == "T")
    {
      message = data.substring(1,4);
      int i = message.toInt();
      turn.write(i);
    }
    else if( data.substring(0,1) == "M")
    {
      message = data.substring(1,4);
      int i = message.toInt();
      esc.write(i);
      delay(75);

      while (Serial.available() > 0)
      {
        String drivingMessage = Serial.readStringUntil('\n');
        if (drivingMessage.substring(0,1) == "M")
        {
          int i = drivingMessage.substring(1,4).toInt();
          esc.write(i);
          delay(100);
        }
        else if ( drivingMessage.substring(0,1) == "T")
        {
          int t = drivingMessage.substring(1,4).toInt();
          turn.write(i);
        }
        else{
          esc.write(90);
        }
      }
      
      

      if (Serial.available() == 0)
      {
        esc.write(90);
 
      }
      
    }
    
    else if (data.substring(0,1) == "A")
    {
      digitalWrite(13, HIGH);

     int servo1move = data.substring(1,3).toInt();
     int servo2move = data.substring(3,5).toInt();
     int pumpchange = data.substring(5,6).toInt();
     servo1.write(arm1Corrections[servo1move]);
     servo2.write(arm2Corrections[servo1move]);
     servo3.write(arm3Corrections[servo2move]);
     servo4.write(arm4Corrections[servo2move]);
     digitalWrite(pump, pumpchange);
     
    }
    
  message = "";
  }
}
