
void setup() 
{ 
  pinMode(3, OUTPUT);
} 
 
void loop() 
{ 
  int val = analogRead(A0);          
  int brightness = map(val, 0, 1023, 0, 255);
  analogWrite(3, brightness);
  delay(50); 
} 
