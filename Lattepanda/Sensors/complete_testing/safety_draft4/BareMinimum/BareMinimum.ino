void setup() {
  // put your setup code here, to run once:
  Serial1.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial1.print("DATA");
  Serial1.print(",");
  Serial1.print("TIME");
  Serial1.print(",");
  Serial1.println(100);
  delay(1000);
}
