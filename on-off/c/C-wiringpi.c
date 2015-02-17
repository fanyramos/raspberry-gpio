#include <wiringPi.h>


int main() {
	wiringPiSetupGpio();
	pinMode(26,OUTPUT);
	while(1) {
		delay(1000);
		digitalWrite(26,HIGH);
		delay(1000);
		digitalWrite(26,LOW);
	}
}

