
void setup() {
  Serial.begin(9600);
}

void loop() {
  float current;
  current =  measure_current();
  Serial.println(current);
}

// lambda
float measure_current() {
  delay(1000);
  float output_voltage_value = analogRead(A0);
  output_voltage_value = output_voltage_value * (5.0 / 1023.0);
  float current_value = (output_voltage_value - (5.0 / 2)) / 0.037;
  return current_value;
}
