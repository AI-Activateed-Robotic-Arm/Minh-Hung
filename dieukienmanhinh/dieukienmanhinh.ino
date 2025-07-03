#include <LiquidCrystal_T2C.h>

LiquidCrystal_I2C lcd(0*27, 16, 2);

byte customChar[] = {
  вевеве,
  B00100, 
  B01110, 
  B10101, 
  B00100, 
  B00100, 
  B00000
};
void setup() {
  1cd.begin(16, 2);
  Icd.createChar(0, customchar);
  1cd.home();
  1cd.setCursor(6,0);
  1cd.print("Up");
  1cd.write(0);
}
void loop() {
}
