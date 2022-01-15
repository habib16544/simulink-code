#include <Servo.h>

Servo gripper,arm,base;

//#define gripper 8
//#define arm 9
void setup(){
  gripper.attach(8);
  arm.attach(9);
  base.attach(10);
  gripper.write(90);
  arm.write(0);
  base.write(0);
  delay(1000);
}

void loop(){
  arm_function();
  delay(1000);  
}

void arm_function(){
//  arm naambe
  for(int i=0;i<=30;i++){
    arm.write(i);
    delay(50);
    }
  delay(500);
//gripper dhorbe
  for (int i=90;i>=0;i--){
    gripper.write(i);
    delay(5);
    }
  delay(500);
//arm uthbe
  for(int i=30;i>=0;i--){
    arm.write(i);
    delay(50);
    }
  delay(500);

//  base ghurbe
  for(int i=0;i<=90;i++){
    base.write(i);
    delay(50);
    }
  delay(500);

//  arm naambe
  for(int i=0;i<=30;i++){
    arm.write(i);
    delay(50);
    }
  delay(500);
  
//gripper charbe
for (int i=0;i<=90;i++){
    gripper.write(i);
    delay(5);
    }
  delay(500);

//arm uthbe
  for(int i=30;i>=0;i--){
    arm.write(i);
    delay(50);
    }
  delay(500);

// base aager jaygay jabe
  for(int i=90;i>=0;i--){
    base.write(i);
    delay(50);
    }
  delay(500);
}
