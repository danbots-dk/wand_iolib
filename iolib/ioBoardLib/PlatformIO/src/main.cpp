#include <Wire.h>
#include <Arduino.h>
#include <Adafruit_NeoPixel.h>

#define PIN        3
#define NUMPIXELS  7
#define DELAYVAL   500

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ400);

void vib_motor(uint8_t on_or_off){
  digitalWrite(2, on_or_off);
}

void neopixel_custom_color(int pixelIndex, uint8_t red, uint8_t green, uint8_t blue, uint8_t on_or_off){
  vib_motor(on_or_off);
  pixels.setPixelColor(pixelIndex, pixels.Color(red, green, blue));
  pixels.show();
}



void receiveEvent(int byteCount) {
  // I2C data received
  while (Wire.available() >= 5) {
    uint8_t funct_id = Wire.read();
    int byte0 = Wire.read();
    uint8_t byte1 = Wire.read();
    uint8_t byte2 = Wire.read();
    uint8_t byte3 = Wire.read();
    uint8_t byte4 = Wire.read();

    neopixel_custom_color(byte0, byte1, byte2, byte3, byte4);


  }

    

    
}


void setup() {

  pinMode(2, OUTPUT);
#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
#endif

  pixels.begin();
  Wire.begin(0x08); // I2C address 8
  Wire.onReceive(receiveEvent);


}

void loop() {
  
}
