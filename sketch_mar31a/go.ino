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
  listanse = (delta / 2) * (listanse / distanse);
  ristanse = (delta / 2) * (ristanse / distanse);
  }

  Serial.println("Полный Вперёд!:)");
  stepperL.setTarget(listanse, RELATIVE);
  stepperR.setTarget(ristanse, RELATIVE);
}
