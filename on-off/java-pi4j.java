import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPin;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinDirection;
import com.pi4j.io.gpio.PinMode;
import com.pi4j.io.gpio.PinPullResistance;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;
import com.pi4j.io.gpio.trigger.GpioCallbackTrigger;
import com.pi4j.io.gpio.trigger.GpioPulseStateTrigger;
import com.pi4j.io.gpio.trigger.GpioSetStateTrigger;
import com.pi4j.io.gpio.trigger.GpioSyncStateTrigger;
import com.pi4j.io.gpio.event.GpioPinListener;
import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
import com.pi4j.io.gpio.event.GpioPinEvent;
import com.pi4j.io.gpio.event.GpioPinListenerDigital;
import com.pi4j.io.gpio.event.PinEventType;


class RaspberryLEDs {
	
	public static void main(String[] args) {

		final GpioController gpio = GpioFactory.getInstance();
		
		final GpioPinDigitalOutput pin = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_25, "MyLED", PinState.HIGH);



		Thread.sleep(3000);

		pin.low();

		Thread.sleep(5000);

		pin.toggle();

		Thread.sleep(3000);

		Thread.toggle();

		gpio.shutdown();
	}


	private void blinkWithDelay(GpioPinDigitalOutput pin, int delay) {

		while (true) {
			Thread.sleep(delay);
			pin.toggle();
		}
	}

	private void blinkNoDelay(GpioPinDigitalOutput pin, int delay) {

		while (true) {
			pin.toggle();
		}
	}


}
	