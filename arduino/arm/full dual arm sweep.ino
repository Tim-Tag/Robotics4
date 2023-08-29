#include <Servo.h>
Servo servo1;
Servo servo2;
const int t = 40;
const int f = 1000;
void setup() {
  // put your setup code here, to run once:
servo1.attach(9);
servo2.attach(10);
}

void loop() {
  // put your main code here, to run repeatedly:
//110, 100, 90, 80,  70,  60,  50,  40,  30,  20,  10,   0
// 62,  72, 82, 92, 101, 111, 121, 131, 141, 151, 161, 171
//servo1.write(162);
//servo2.write(11);
//delay(1000);
/*
servo1.write(170);
servo2.write(4);
delay(t);
servo1.write(160);
servo2.write(13);
delay(t);
servo1.write(150);
servo2.write(23);
delay(t);
servo1.write(140);
servo2.write(33);
delay(t);
servo1.write(130);
servo2.write(43);
delay(t);
servo1.write(120);
servo2.write(53);
delay(t);
servo1.write(110);
servo2.write(62);
delay(t);
servo1.write(100);
servo2.write(72);
delay(t);
servo1.write(90);
servo2.write(82);
delay(t);
servo1.write(80);
servo2.write(92);
delay(t);
servo1.write(70);
servo2.write(101);
delay(t);
servo1.write(60);
servo2.write(111);
delay(t);
servo1.write(50);
servo2.write(121);
delay(t);
servo1.write(40);
servo2.write(131);
delay(t);
servo1.write(30);
servo2.write(141);
delay(t);
servo1.write(20);
servo2.write(151);
delay(t);
servo1.write(10);
servo2.write(161);
delay(t);
servo1.write(0);
servo2.write(171);
delay(f);
*/
for (int i = 0; i < 174; i++)
{
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
  delay(t);
}
delay(f);
for (int i = 174; i > 0; i--)
{
  if(i> 161)
  {
    servo1.write(i);
    servo2.write(174-i);
  }
  else if(i>117 && i<162)
  {
    servo1.write(i);
    servo2.write(173-i);
  }
  else if(i >118 && i< 77)
  {
    servo1.write(i);
    servo2.write(172-i);
  }
  else if(i>78);
  {
    servo1.write(i);
    servo2.write(171-i);
  }
  delay(t);
}
delay(f);
}
