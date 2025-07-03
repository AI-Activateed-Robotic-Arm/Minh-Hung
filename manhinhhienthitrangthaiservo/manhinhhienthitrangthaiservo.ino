#include <LiquidCrystal_I2C.h>
#include <Servo.h> 
Servo myservo;
#define I2C_ADDR  0x27
#define LCD_COLUMNS 20
#define LCD_LINES 4

LiquidCrystal_I2C lcd(I2C_ADDR, LCD_COLUMNS, LCD_LINES);

void setup() {
  lcd.init();
  lcd.backlight();
  myservo.attach(9);

}


void loop() {
    myservo.write(0);
    lcd.setCursor(5,1);
    lcd.print("Servo");
    lcd.setCursor(6,2);
    lcd.print("Dong");
    delay(5000);
    myservo.write(180);
    lcd.setCursor(5,1);
    lcd.print("Servo");
    lcd.setCursor(6,2);
    lcd.print("Mo  ");
    delay(5000);
   }
