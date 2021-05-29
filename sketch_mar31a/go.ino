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

  Serial.println("Полный Вперёд!:)");
  Serial.println(stepperL.getCurrent());
  Serial.println(stepperR.getCurrent());
  stepperL.setTarget(listanse, RELATIVE);
  stepperR.setTarget(ristanse, RELATIVE);
  Serial.println(stepperL.getTarget());
  Serial.println(stepperR.getTarget());
}

void stopping() {
  Serial.print("ПОЛНЫЙ СТОП!!!");
  Serial.println(stepperL.getCurrent());
  Serial.println(stepperR.getCurrent());
  listanse = stepperL.getCurrent() + delta * (listanse / distanse);
  ristanse = stepperR.getCurrent() + delta * (ristanse / distanse);
  stepperL.setTarget(listanse, ABSOLUTE);
  stepperR.setTarget(ristanse, ABSOLUTE);
  Serial.println(stepperL.getTarget());
  Serial.println(stepperR.getTarget());
}
