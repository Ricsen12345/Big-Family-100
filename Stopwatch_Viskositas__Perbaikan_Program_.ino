const int HALLPIN1 = 7;
const int HALLPIN2 = 8;

#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

unsigned long mulai, selesai, dataStopWatch;
int i=0;
int fPaus = 0;
long lastButton = 0;
long delayAntiBouncing = 25;
long dataPaus = 0;

void setup() {
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  digitalWrite(HALLPIN1, 1);
  digitalWrite(HALLPIN2, 1);
  
  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print(" Ujian  Praktek");
  lcd.setCursor(0, 1);
  lcd.print("     Fisika");
  delay(2500);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("   Alat  Ukur");
  lcd.setCursor(0, 1);
  lcd.print("   Viskositas");
}

void loop() {
  if (digitalRead(HALLPIN1)==0)
  {
    if((millis() - lastButton) > delayAntiBouncing)
    {
      if (i==0)
      {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("StopWatch");
        mulai = millis();
        fPaus = 0;
      }
    }
    lastButton = millis();
  }

  else if (digitalRead(HALLPIN2)==0)
  {
    if((millis() - lastButton) > delayAntiBouncing)
    {
      if (i==0)
      {
        dataPaus = dataStopWatch;
        fPaus = 1;
      }
      i =!1;
    }
    lastButton = millis();
  }

  if (i==1)
  {
    selesai = millis();
    float jam, menit, detik, miliDetik;
    unsigned long over;
    dataStopWatch = selesai - mulai;
    dataStopWatch = dataPaus + dataStopWatch;

    jam = int(dataStopWatch / 3600000);
    over = dataStopWatch % 3600000;
    menit = int(over / 60000);
    over = over % 60000;
    detik = int(over / 1000);
    miliDetik = over % 1000;

    lcd.setCursor(0, 1);
    lcd.print(jam, 0);
    lcd.print(":");
    lcd.print(menit, 0);
    lcd.print(":");
    lcd.print(detik, 0);
    lcd.print(".");
    if (jam < 10)
    {
      lcd.print(miliDetik, 0);
      lcd.print(" ");
    }
  }
  
  else if (digitalRead(HALLPIN1)==0 && fPaus==1)
  {
    dataStopWatch = 0;
    dataPaus = 0;
  }
}
