#include <SoftwareSerial.h>

SoftwareSerial mySerial(8, 7); // -> Works with this code
#define Serial mySerial

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  //Serial.println("CLEARDATA"); // clears sheet starting at row 2
  Serial.println("CLEARSHEET"); // clears sheet starting at row 1

  // With this command you can set the labels for the top most row of the ActiveSheet
  Serial.println("LABEL, Time, Temperature(C), Speed(Km/h), Voltage(V), Current(A)");
}

void loop() {
  // put your main code here, to run repeatedly:
  //  Serial.println( (String) "DATA,TIME,25,100,135,0.25"); // Works
  Serial.print("DATA");
  Serial.print(",");
  Serial.print("TIME");
  Serial.print(",");
  Serial.print(25);
  Serial.print(",");
  Serial.print(100);
  Serial.print(",");
  Serial.print(135);
  Serial.print(",");
  Serial.println(0.25);
  
  delay(2000);
}
