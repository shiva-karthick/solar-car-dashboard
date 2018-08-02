void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  // read the input on analog pin 0:
  float batteryValue = analogRead(A0);
  float value = (batteryValue/1023) * 5;
  float realValue = value * 30;
  // print out the value you read:
  Serial.println(realValue);
  delay(1);        // delay in between reads for stability
}
