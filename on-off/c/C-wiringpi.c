#include <wiringPi.h>


int main() {
	wiringPiSetupGpio();
	pinMode(26,OUTPUT);
	while(1) {
		digitalWrite(26,HIGH);
		digitalWrite(26,LOW);
	}
}

