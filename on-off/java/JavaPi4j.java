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


class JavaPi4j {
	
	public static void main(String[] args) {

		final GpioController gpio = GpioFactory.getInstance();
		

		final GpioPinDigitalOutput pin = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_25, "MyLED", PinState.HIGH);

		blinkNoDelay(pin);
		gpio.shutdown();
	}

	private static void blinkWithDelay(GpioPinDigitalOutput pin, int delay)  {


		while (true) {

			try	{
				Thread.sleep(delay);
				pin.toggle();
			}

			catch (InterruptedException e) {
				System.out.print("Interrupted Execution Exception ... Cause:\n\n============\n\n" + e.getCause());
				System.out.print("Interrupted Execution Exception ... Cause:\n\n============\n\n" + e.getStackTrace());
			}
		}
	}

	private static void blinkNoDelay(GpioPinDigitalOutput pin) {

		while (true) {
			pin.toggle();
		}
	}	
}
	
