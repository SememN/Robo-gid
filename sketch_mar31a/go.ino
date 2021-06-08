void doing(int comand)
{
  if (comand == -8) {
    listanse = -distanse;
    ristanse = distanse;
  }
  else if (comand == -2) {
    listanse = distanse;
    ristanse = -distanse;
  }
  else if (comand == -4) {
    listanse = distanse;
    ristanse = distanse;
  }
  else if (comand == -6) {
    listanse = -distanse;
    ristanse = -distanse;
  }

  Serial.println(" Just moving!");
  Serial.println(stepperL.getCurrent());
  Serial.println(stepperR.getCurrent());
  stepperL.setTarget(listanse, RELATIVE); // RELATIVE
  stepperR.setTarget(ristanse, RELATIVE); // ABSOLUTE
  Serial.println(stepperL.getTarget());
  Serial.println(stepperR.getTarget());
}

void stopping() {
  Serial.println(" FULL STOP!!!");
  Serial.println(stepperL.getCurrent());
  Serial.println(stepperR.getCurrent());
  listanse = delta * (listanse / distanse) + stepperL.getCurrent();
  ristanse = delta * (ristanse / distanse) + stepperR.getCurrent();
  stepperL.setTarget(listanse, ABSOLUTE); // RELATIVE
  stepperR.setTarget(ristanse, ABSOLUTE); // ABSOLUTE
  Serial.println(stepperL.getTarget());
  Serial.println(stepperR.getTarget());
}
