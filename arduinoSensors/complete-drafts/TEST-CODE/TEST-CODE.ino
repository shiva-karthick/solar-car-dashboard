# include "DHT.h"

# define DHTPIN 2     // what digital pin we're connected to
# define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  // Wait a few seconds between measurements.
  delay(2000);
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();

  // Check if any reads failed and exit early (to try again).
  if (isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Serial.print("Temperature: "); 
  Serial.print(t);
  Serial.print(",");

  // Simulate the speed from the GPS shield
  Serial.print(110);
  Serial.print(",");

  // Simulate the battery level
  Serial.println(50);

}
