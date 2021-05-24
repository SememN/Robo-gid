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
  else if (comand == -5) {
    Serial.print("не (:");
    listanse = delta * (listanse / distanse);
    ristanse = delta * (ristanse / distanse);
  }

  Serial.println("Полный Вперёд!:)");
  stepperL.setTarget(listanse, RELATIVE);
  stepperR.setTarget(ristanse, RELATIVE);
  Serial.println(stepperL.getTarget());
  Serial.println(stepperR.getTarget());
  Serial.println(stepperL.getCurrent());
  Serial.println(stepperR.getCurrent());
}
