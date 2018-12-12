
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial1.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  Serial1.print("DATA");
  Serial1.print(",");
  Serial1.print("TIME");
  Serial1.print(",");
  Serial1.print(25);
  Serial1.print(",");
  Serial1.print(100);
  Serial1.print(",");
  Serial1 .println(75);

  delay(1000);                       // wait for a second
}
