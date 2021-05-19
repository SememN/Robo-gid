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
    listanse = 2 * delta * (listanse / distanse);
    ristanse = 2 * delta * (ristanse / distanse);
  }

  Serial.println("Полный Вперёд!:)");
  stepperL.setTarget(listanse, RELATIVE);
  stepperR.setTarget(ristanse, RELATIVE);
  stepperL.getTarget();
  stepperR.getTarget();
  stepperL.getCurrent();
  stepperR.getCurrent();
}
