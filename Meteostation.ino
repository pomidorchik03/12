#include <Temperature_LM75_Derived.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP280.h>
#include "DHT.h"

#define BMP_SCK  (13)
#define BMP_MISO (12)
#define BMP_MOSI (11)
#define BMP_CS   (10)
Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);

#define DHTPIN 2 
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

Generic_LM75 temperature;


void setup() {
  Serial.begin(9600);
  Wire.begin();

  bmp.begin();

  dht.begin();
}
  

void loop() {
  
  float t = temperature.readTemperatureC();
  float p = bmp.readPressure() / 133.33;
  float h = dht.readHumidity();
  
  
  Serial.print(t);


  Serial.print(F(" "));
  Serial.print(p);


  Serial.print(F(" "));
  Serial.println(h);


  delay(2000);
}

