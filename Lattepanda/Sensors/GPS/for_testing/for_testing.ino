void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("DATA");
  Serial.print(",");
  Serial.print("TIME");
  Serial.print(",");
  Serial.print(25);
  Serial.print(",");
  Serial.print(100);
  Serial.print(",");
  Serial.print(75);
  Serial.print(",");
  Serial.print(0.10);
  Serial.print(",");
  Serial.print(0.20);
  Serial.print(",");
  Serial.print(0.30);
  Serial.print(",");
  Serial.print(0.40);
  Serial.print(",");
  Serial.println(0.50);

  delay(1000);
}
