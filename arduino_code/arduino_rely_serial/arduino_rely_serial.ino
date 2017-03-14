int out = 8; // pin connected to VCC of 5v rely
String cmd = "on";

void setup() {
  Serial.begin(9600); // Starts the serial communication
  Serial.flush();
  pinMode(out, OUTPUT);
}

void loop() {
  String input = ""; 
   // Read any serial input
   while (Serial.available() > 0) {
       input += (char) Serial.read(); // Read in one char at a time
       delay(5); // Delay for 5 ms so the next char has time to be received
   }
   if (input == "on") {
     cmd = "on";
     digitalWrite(out, HIGH); // on
     Serial.println("ON");
   }
   else if (input == "off") {
     cmd = "off";
     digitalWrite(out, LOW); // off
     Serial.println("OFF");
   }

}
