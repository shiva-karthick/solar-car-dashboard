

// constants won't change. They're used here to set pin numbers:
const int buttonPin = 24;     // the number of the pushbutton pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  //Serial.println("CLEARDATA"); // clears sheet starting at row 2
  //Serial.println("CLEARSHEET"); // clears sheet starting at row 1

  // With this command you can set the labels for the top most row of the ActiveSheet
  //  Serial.println("LABEL, Time, Temperature(C), Speed(Km/h), Voltage(V), Current(A)");

  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //  Serial.println( (String) "DATA,TIME,25,100,135,0.25"); // Works

  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
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
  } else {
    // do nothing
  }
  delay(2000);
}
