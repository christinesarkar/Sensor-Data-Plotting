#include <NewPing.h>
 
#define TRIGGER_PIN  8
#define ECHO_PIN     9
#define MAX_DISTANCE 200
int counter=0;
 
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  delay(50);
  //Serial.print("Ping: ");
  counter= counter+1;
  Serial.print(counter);
  Serial.print(",");
  Serial.println(sonar.ping_cm());
  //Serial.println("cm");
}
