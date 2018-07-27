float collect_gps();
float collect_temperature();
float collect_battery();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  float speeed;
  float temperature;
  float battery;

  speeed = collect_gps();
  temperature = collect_temperature();
  battery = collect_battery();
  Serial.print(speeed);
  Serial.print(',');
  Serial.print(temperature);
  Serial.print(',');
  Serial.println(battery);
}

float collect_gps() {
  float speed = 100;
  return speed;
}

float collect_temperature() {
  float temperature = 30;
  return temperature;
}

float collect_battery() {
  float battery = 75;
  return battery;
}

