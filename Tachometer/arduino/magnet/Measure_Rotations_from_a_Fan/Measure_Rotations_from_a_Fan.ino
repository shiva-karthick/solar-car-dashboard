/* resource link : https://engineersportal.com/blog/2018/10/3/arduino-tachometer-using-a-hall-effect-sensor-to-measure-rotations-from-a-fan
   Arduino Tachometer - Using a Hall Effect Sensor (A3144) to Measure Rotations from a Fan
   Modified and owned by Shankar
*/

// digital pin 2 is the hall pin
int hall_pin = 2;

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  // make the hall pin an input:
  pinMode(hall_pin, INPUT);
  Serial.print("Test!");
}

// the loop routine runs over and over again forever:
void loop() {
  Serial.println(digitalRead(hall_pin));
  delay(1);
}
