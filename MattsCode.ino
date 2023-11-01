#include<Servo.h>
 
Servo esc;
Servo turn;
 
void setup()
{
esc.attach(9);
turn.attach(10);
delay(5000);
}
 
void loop()
{
//motor();
//steer();
Left();
Right();
}
 
void motor()
{
esc.write(90);
delay(2000);
esc.write(80);
delay(2000);
esc.write(90);
delay(2000);
esc.write(100);
delay(2000);
}
 
void steer()
{
turn.write(90);
delay(1000);
turn.write(0); //left
delay(1000);
turn.write(90);
delay(1000);
turn.write(180); //right
delay(1000);
turn.write(90);
delay(1000);
}
 
void Left()
{
turn.write(90);
delay(1000);
turn.write(0);
delay(1000);
esc.write(90);
delay(2000);
esc.write(150);
delay(2000);
esc.write(90);
delay(2000);
turn.write(90);
delay(1000);
}
 
void Right()
{
turn.write(90);
delay(1000);
turn.write(180);
delay(1000);
esc.write(90);
delay(2000);
esc.write(150);
delay(2000);
esc.write(90);
delay(2000);
turn.write(90);
delay(1000);
}
