void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  //Serial.println("CLEARDATA"); // clears sheet starting at row 2
  Serial.println("CLEARSHEET"); // clears sheet starting at row 1

  // With this command you can set the labels for the top most row of the ActiveSheet
  Serial.println("LABEL,Date Column,Time Column, Seconds Elapsed");
  
  Serial.println("BEEP");
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println( (String) "DATA,TIME," + millis() );
  delay(2000);
}
