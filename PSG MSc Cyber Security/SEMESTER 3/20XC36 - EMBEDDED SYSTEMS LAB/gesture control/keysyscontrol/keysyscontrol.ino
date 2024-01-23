uint8_t buf[8] = { 0 }; //Keyboard report buffer
#define CONTROL_CH 1 // Channel change
#define CONTROL_VOL 2 // Volume
#define CONTROL_POW 3 // Power

#define CONTROL_UP 1
#define CONTROL_DOWN -1

#define DIST_MAX 20 // Maximum distance in inches, anything above is ignored.
#define DIST_DOWN 10 // Threshold for up/down commands. If higher, command is "up". If lower, "down".
#define DIST_POW 3 // Threshold for power command, lower than = power on/off


const int pingPin = 8;
const int echoPin = 7;

unsigned long timer;

boolean powerConfirmed = false;

long doPing()
{
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);
  return pulseIn(echoPin, HIGH);
}


long microsecondsToInches(long microseconds)
{
  // According to Parallax's datasheet for the PING))), there are
  // 73.746 microseconds per inch (i.e. sound travels at 1130 feet per
  // second).  This gives the distance travelled by the ping, outbound
  // and return, so we divide by 2 to get the distance of the obstacle.
  // See: http://www.parallax.com/dl/docs/prod/acc/28015-PING-v1.3.pdf
  return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}

void releaseKey() {

buf[0] = 0;

buf[2] = 0;

Serial.write(buf, 8); // Send Release key

}

void setup() {
  // initialize serial communication and set pins
  Serial.begin(9600);
  pinMode(pingPin, OUTPUT);
  pinMode(echoPin, INPUT);
  timer = millis();
}

void loop()
{

//  Serial.println(millis());
  long duration, inches;
  int value;

  // Check for a reading
  duration = doPing();

  // Timer to confirm actions (currently only power)
  if (timer && timer < (millis() - 5000) && (millis() > 5000))
  {
    //Serial.println("timer reset");
    timer = false;
  }

   


  // convert the time into a distance 
  inches = microsecondsToInches(duration);

  // If less than max inches away, act
  if (inches < DIST_MAX)
  {
    // Debug output
    //Serial.print(inches);
    //Serial.println("in");

    // If very close, it is a "power" signal
    if (inches < DIST_POW)
    {
      //Serial.println(timer);
      // on or off
      if (timer)
      {
        doIR(CONTROL_POW, 0);
        timer = false;
        delay(2000); // don't want to be sending this more than once. 2 second delay
      }
      else
      {
        //Serial.println("power flag set");
        timer = millis();
       
        delay(500);
      }
    }
    else // is volume or channel
    {
      // Distance determines control direction
      value = handleDist(inches);
      // wait half a second
      delay(300);
      // check again, has hand disappeared?
      if (microsecondsToInches(doPing()) > DIST_MAX)
      {
        doIR(CONTROL_CH, value); // swipe
      }
      else
      {
        // volume
        int d = 500; // first delay is longer for single volume change
        // repeat until hand is removed
        while (inches < DIST_MAX)
        {
          value = handleDist(inches); // is up or down?
          doIR(CONTROL_VOL, value); // fire off IR signal
          delay(d); // wait
          inches = microsecondsToInches(doPing()); // check for hand again
          d = 100; // delays are shorter for quick multiple volume adjustment
        }
        delay(500); // this stops accidental channel change after volume adjustment
      }
    }
  }
  delay(50); // Short enough to detect all swipes.
}
/*
* If distance is within threshold, mark as 'up' and turn on corresponding LED.
*/
int handleDist(int inches)
{
  if (inches > DIST_DOWN)
  {
    return CONTROL_UP;
  }
  else
  {
    return CONTROL_DOWN;
  }
}


void doIR(int control, int val)
{
  switch(control)
  {
  case CONTROL_POW:
   buf[2] = 4; // W keycode

Serial.write(buf, 8); // Send keypress

releaseKey();
    
    break;
  case CONTROL_CH:
    
    if (val == CONTROL_UP)
    {
      buf[2] = 5; // W keycode

Serial.write(buf, 8); // Send keypress

releaseKey();
    }
    else // down
    {
       buf[2] = 6; // W keycode

Serial.write(buf, 8); // Send keypress

releaseKey();
    }
    break;
  case CONTROL_VOL:
    
    if (val == CONTROL_UP)
    {
      buf[2] = 7; // W keycode

Serial.write(buf, 8); // Send keypress

releaseKey();
      
    }
    else //down
    {
      buf[2] = 8; // W keycode

Serial.write(buf, 8); // Send keypress

releaseKey();
    }
    break;
  }
}


