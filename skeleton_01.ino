
char key = 0;


void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);

  pinMode(0, OUTPUT);
  pinMode(BDPIN_LED_USER_1, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  char key;
  while ((key = test_main_menu()) != 0)
  {
    switch (key)
    {
      case '0':
        Serial.print("No.0\r\n");
        digitalWrite(0, HIGH);
        delay(100);
        digitalWrite(0, LOW);
        break;
      case '1':
        Serial.print("No.1\r\n");
        digitalWrite(BDPIN_LED_USER_1, HIGH);
        delay(100);
        digitalWrite(BDPIN_LED_USER_1, LOW);
        break;
      case '2':
        Serial.print("No.2\r\n");
        digitalWrite(2, HIGH);
        delay(100);
        digitalWrite(2, LOW);
        break;
      case '3':
        Serial.print("No.3\r\n");
        digitalWrite(3, HIGH);
        delay(100);
        digitalWrite(3, LOW);
        break;
      case '4':
        Serial.print("No.4\r\n");
        digitalWrite(4, HIGH);
        delay(100);
        digitalWrite(4, LOW);
        break;

      case '5':
        Serial.print("No.5\r\n");
        digitalWrite(5, HIGH);
        delay(100);
        digitalWrite(5, LOW);
        break;
      case '6':
        Serial.print("No.6\r\n");
        digitalWrite(6, HIGH);
        delay(100);
        digitalWrite(6, LOW);
        break;
      case '7':
        Serial.print("No.7\r\n");
        digitalWrite(7, HIGH);
        delay(100);
        digitalWrite(7, LOW);
        break;
      case '8':
        Serial.print("No.8\r\n");
        digitalWrite(8, HIGH);
        delay(100);
        digitalWrite(8, LOW);
        break;
      case '9':
        Serial.print("No.9\r\n");
        digitalWrite(9, HIGH);
        delay(100);
        digitalWrite(9, LOW);
        break;
      case 'a':
        Serial.print("No.a\r\n");
        digitalWrite(10, HIGH);
        delay(100);
        digitalWrite(10, LOW);
        break;
      case 'b':
        Serial.print("No.b\r\n");
        digitalWrite(11, HIGH);
        delay(100);
        digitalWrite(11, LOW);
        break;
      case 'c':
        Serial.print("No.c\r\n");
        digitalWrite(12, HIGH);
        delay(100);
        digitalWrite(12, LOW);
        break;
      case 'd':
        Serial.print("No.d\r\n");
        digitalWrite(13, HIGH);
        delay(100);
        digitalWrite(13, LOW);
        break;
      default:
        Serial.print("default\r\n");
        break;

    }
  }
}


char test_main_menu(void)
{
  char key;

  Serial.print("\n\r\n");
  Serial.print("-------------------------------------------------\r\n");
  Serial.print("EDUCATION SHIELD TEST MAIN MENU\r\n");
  Serial.print("-------------------------------------------------\r\n");
  Serial.print(" 0.  0 Digital OUT \r\n");
  Serial.print(" 1.  1 Digital OUT \r\n");
  Serial.print(" 2.  2 Digital OUT \r\n");
  Serial.print(" 3.  3 Digital OUT \r\n");
  Serial.print(" 4.  4 Digital OUT \r\n");
  Serial.print(" 5.  5 Digital OUT \r\n");
  Serial.print(" 6.  6 Digital OUT \r\n");
  Serial.print(" 7.  7 Digital OUT \r\n");
  Serial.print(" 8.  8 Digital OUT \r\n");
  Serial.print(" 9.  9 Digital OUT \r\n");
  Serial.print(" a. 10 Digital OUT \r\n");
  Serial.print(" b. 11 Digital OUT \r\n");
  Serial.print(" c. 12 Digital OUT \r\n");
  Serial.print(" d. 13 Digital OUT \r\n");
  Serial.print("-------------------------------------------------\r\n");
  Serial.print(" q. SKELETON IOCTL QUIT\r\n");
  Serial.print("-------------------------------------------------\r\n");
  Serial.print("\n\r\n");
  Serial.print("SELECT THE COMMAND NUMBER : ");

  while (1)
  {
    if (Serial.available())
    {
      key = (char)Serial.read();
      break;
    }
  }

  return key;
}
