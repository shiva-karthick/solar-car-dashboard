int batteryPinNumber = A0;    // select the input pin for the potentiometer
float batteryValue = 75;  // variable to store the value coming from the sensor

void setup() {
  // declare the ledPin as an OUTPUT:
  Serial.begin(9600);
}

void loop() {
  // read the value from the sensor:
  batteryValue = analogRead(batteryPinNumber);
  Serial.print(batteryValue);
  delay(1000); // for stability
}
