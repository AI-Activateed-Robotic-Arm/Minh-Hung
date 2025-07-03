#include <WiFi.h>

#define SSID "BKSTAR_T2_01"
#define PASS "stemstar"

void setup() {
  Serial.begin(115200);
  pinMode(8, OUTPUT);
  digitalWrite(8, HIGH);
  WiFi.begin(SSID, PASS);
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.println(".");
  }
  Serial.println("Connected!");
  digitalWrite(8, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:

}

