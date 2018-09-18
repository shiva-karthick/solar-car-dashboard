#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3); //TX, RX
// Set SET_A and SET_B to ground for Normal Mode (Send and Receive)

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  Serial.println("CLEARDATA");
  Serial.println("LABEL, Random Values");
}

void loop() {
  // Sending code
  if (Serial.available() > 0) { // Read from serial monitor and send over to UM402
    String input = Serial.readString();
    mySerial.println(50);
  }

  // receiving code
  if (mySerial.available() > 1) { // Read from UM402 and send to serial monitor
    String input = mySerial.readString();
    Serial.println(input);
  }

  delay(20); // To stabilise the readings
}
