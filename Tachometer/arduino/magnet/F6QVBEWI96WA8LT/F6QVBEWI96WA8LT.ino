#include <LiquidCrystal.h>
LiquidCrystal lcd(13,12,11,10,9,8);

#define reed A0//pin connected to read switch

//storage variables
float radius = 13.5;// tire radius (in inches)- CHANGE THIS FOR YOUR OWN BIKE
int buttonInt=0;
int mode1=1;
int mode2=2;
int mode3=3;
volatile int selectedmode=mode1;
volatile int nselectedmode1=mode2;
volatile int nselectedmode2=mode3;
int reedVal;
long timer = 0;
float mph = 0.00;
float distance=0.00;
float circumference;
boolean backlight;


int maxReedCounter = 100;
int reedCounter;

void setup(){
  
  reedCounter = maxReedCounter;
  circumference = 2*3.14*radius;
  pinMode(1,OUTPUT);
  pinMode(2,INPUT);
  pinMode(reed, INPUT);
  lcd.begin(16,2);
  attachInterrupt(buttonInt,swap,RISING);
  Serial.write(12);

  
  

  cli();


  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1  = 0;
  
  OCR1A = 1999;// = (1/1000) / ((1/(16*10^6))*8) - 1
  
  TCCR1B |= (1 << WGM12);
  
  TCCR1B |= (1 << CS11);   
  
  TIMSK1 |= (1 << OCIE1A);
  
  sei();//allow interrupts
  //END TIMER SETUP

  Serial.begin(9600);
} 

void swap()
{
  if(selectedmode==mode1)
  {
  selectedmode=mode2;
  nselectedmode1=mode3;
  nselectedmode2=mode1;
  }
  else if(selectedmode==mode2)
  {
  selectedmode=mode3;
  nselectedmode1=mode1;
  nselectedmode2=mode2;
  }
  else
  {
  selectedmode=mode1;
  nselectedmode1=mode2;
  nselectedmode2=mode3;
  }    
}  
  
  


ISR(TIMER1_COMPA_vect) {//Interrupt at freq of 1kHz to measure reed switch
  reedVal = digitalRead(reed);//get val of A0
  if (reedVal){//if reed switch is closed
    if (reedCounter == 0){//min time between pulses has passed
      mph = (56.8*float(circumference))/float(timer);//calculate miles per hour
      timer = 0;//reset timer
      reedCounter = maxReedCounter;//reset reedCounter
    }
    else{
      if (reedCounter > 0){//don't let reedCounter go negative
        reedCounter -= 1;//decrement reedCounter
      }
    }
  }
  else{//if reed switch is open
    if (reedCounter > 0){//don't let reedCounter go negative
      reedCounter -= 1;//decrement reedCounter
    }
  }
  if (timer > 2000){
    mph = 0;//if no new pulses from reed switch- tire is still, set mph to 0
  }
  else{
    timer += 1;//increment timer
  } 
 if(digitalRead(2)==LOW)
 {
 distance +=mph;
 }
 else
 {distance=0;
 }
 
}


void displayMPH(){
  Serial.write(12);//clear
  Serial.write("Speed =");
  Serial.write(13);//start a new line
  Serial.println(mph);
  Serial.write(" MPH ");
  //Serial.write("0.00 MPH ");
}

void loop(){
  //print mph once a second
  displayMPH();
 if(selectedmode==mode1)
 { 
  lcd.setCursor(0,0);
  lcd.print("                ");
  lcd.setCursor(0,1);
  lcd.print("                ");
  lcd.setCursor(0,0);
  lcd.print("Speed=");
  lcd.setCursor(6,0);
  lcd.print(mph);
  lcd.setCursor(0,1);
  lcd.print("Distance=");
  lcd.setCursor(10,1);
  lcd.print(distance/3600000);
 }
 else if(selectedmode==mode2)
 {
  float check1=20;
  float distA=distance/3600000;
  float percent=distA/check1;
  float percent1 =percent*100;
  lcd.setCursor(0,0);
  lcd.print("                ");
  lcd.setCursor(0,1);
  lcd.print("                ");
  lcd.setCursor(0,0);
  lcd.print("Cover ");
  lcd.setCursor(6,0);
  lcd.print(check1);
  lcd.setCursor(9,0);
  lcd.print("miles");
  if(distA<check1)
  {
  lcd.setCursor(0,1);
  lcd.print("                ");
  lcd.setCursor(0,1);
  lcd.print("% complete=");
  lcd.setCursor(12,1);
  lcd.print(percent1);
  }
  else
  {
  lcd.setCursor(0,0);
  lcd.print("                ");
  lcd.setCursor(0,1);
  lcd.print("                "); 
  lcd.setCursor(0,0);
  lcd.print("Congratulations");
  lcd.setCursor(0,1);
  lcd.print("You pass");  
  }   
} 
  
     
 else
 {
  lcd.setCursor(0,0);
  lcd.print("                ");
  lcd.setCursor(0,1);
  lcd.print("                ");
  lcd.setCursor(0,0);
  lcd.print("Cover 30mph"); 
  if(mph<30)
  {
  lcd.setCursor(0,1);
  lcd.print("                ");
  lcd.setCursor(0,1);
  lcd.print("speed=");
  lcd.setCursor(6,1);
  lcd.print(mph);
  }
  else
  {
  lcd.setCursor(0,0);
  lcd.print("                ");
  lcd.setCursor(0,1);
  lcd.print("                "); 
  lcd.setCursor(0,0);
  lcd.print("Congratulations");
  lcd.setCursor(0,1);
  lcd.print("Light Rider");  
  } 
 } 
}
