#include <GyverStepper.h>

long command;
uint32_t delta = 1000;
uint32_t distanse = delta;
long listanse;
long ristanse;
uint32_t kit;

GStepper< STEPPER2WIRE> stepperL(1, 2, 3, 4);
GStepper< STEPPER2WIRE> stepperR(1, 5, 6, 7);

void setup() {
  Serial.begin(115200);

  stepperL.setRunMode(FOLLOW_POS);
  stepperL.setMaxSpeed(delta);
  stepperL.setAcceleration(delta / 2);
  stepperL.enable();

  stepperR.setRunMode(FOLLOW_POS);
  stepperR.setMaxSpeed(delta);
  stepperR.setAcceleration(delta / 2);
  stepperR.enable();
}
void loop() {

  seing();

  if (stepperL.tick() && stepperR.tick()) {
    if (Serial.available()) {
      stopping();
    }
  }
  else if (!stepperL.tick() || !stepperR.tick()) {
    if (Serial.available()) {
      command = Serial.readString().toInt();
      Serial.print(" Command - ");
      Serial.println(command);
      kit = millis();
    }

    if (millis() - kit > 1000) {
      Serial.println(" I am staing");
    }
    else if (!stepperL.tick() && !stepperR.tick()) {
      if (command > 0) {
        Serial.println(" There was an amendment to the constitution");
        distanse = command;
      }
    }
    else
      doing(command);
  }
}
