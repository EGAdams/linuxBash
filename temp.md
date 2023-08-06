My files are as follows:
```
PinInterfaceTest.cpp:
#include "PinInterface.h"
#include <gtest/gtest.h>

class PinInterfaceTest : public ::testing::Test {  // Define a test fixture
protected:
    PinState*                   pinState;
    std::map<std::string, int>  pinMap;
    PinInterface*               pinInterface;

    void SetUp() override {
        pinState         = new PinState( pinMap );
        pinInterface     = new PinInterface( pinState ); }

    void TearDown() override {
        delete pinInterface;
        delete pinState; }};

TEST_F( PinInterfaceTest, TestAnalogRead ) {  // Define tests
    int pin = 5;
    int value = 1;
    pinInterface->pinAnalogWrite( pin, value );
    EXPECT_EQ( pinInterface->pinAnalogRead( pin ), value );}

TEST_F( PinInterfaceTest, TestDigitalRead ) {
    int pin = 5;
    int value = 1; // Digital pins can only be HIGH ( 1 ) or LOW (0)
    pinInterface->pinDigitalWrite( pin, value );

    EXPECT_EQ( pinInterface->pinDigitalRead( pin ), value );}

TEST_F( PinInterfaceTest, TestAnalogWrite ) {
    int pin = 5;
    int value = 1;
    pinInterface->pinAnalogWrite( pin, value );
    EXPECT_EQ( pinState->getPinState(std::to_string( pin )), value );}

TEST_F( PinInterfaceTest, TestDigitalWrite ) {
    int pin = 5;
    int value = 1; // Digital pins can only be HIGH ( 1 ) or LOW (0)
    pinInterface->pinDigitalWrite( pin, value );
    EXPECT_EQ( pinState->getPinState(std::to_string( pin )), value );}

PinInterface.cpp:
#include "PinInterface.h"
#include <string>

PinInterface::PinInterface( PinState* pinState ) : _pinState( pinState ) {}
PinInterface::~PinInterface() {}

int PinInterface::pinAnalogRead( int pin ) {
    // std::string pin_string = std::to_string( pin );
    int pin_value = _pinState->getPinState( std::to_string( pin ));
    return pin_value; }

int PinInterface::pinDigitalRead( int pin ) {
    int pin_value = _pinState->getPinState( std::to_string( pin ));
    return pin_value; }

void PinInterface::pinAnalogWrite( int pin, int value ) { 
    _pinState->setPinState( std::to_string( pin ), value ); }

void PinInterface::pinDigitalWrite( int pin, int value ) { 
    _pinState->setPinState( std::to_string( pin ), value ); }

std::map<std::string, int> PinInterface::getPinStateMap() { return _pin_map; }

PinInterface.h:
#ifndef PININTERFACE_H
#define PININTERFACE_H

#include "../PinState/PinState.h"
#include "../Arduino/Arduino.h"
#include <map>

class PinInterface {
  public:
    PinInterface(PinState* pinState);
    virtual ~PinInterface();
    virtual void pinAnalogWrite(int pin, int value);
    virtual void pinDigitalWrite(int pin, int value);
    virtual int pinAnalogRead(int pin);
    virtual int pinDigitalRead(int pin);
    std::map<std::string, int> getPinStateMap();

  private:
    std::map<std::string, int> _pin_map;
    PinState* _pinState; };
#endif```

My issue is as follows: I am getting the following error when running:
``` command
    make all
```

``` error
g++   -std=c++14 -Wall -Wextra -g -o /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/Mode1ScoreTest /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/WinSequences.o /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/Mode1ScoreTest.o /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/Player.o /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/GameState.o /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/Mode1TieBreaker.o /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/PinState.o /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/Mode1Score.o /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/TranslateConstant.o /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/googletest/build/lib/libgtest.a /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/googletest/build/lib/libgtest_main.a /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/googletest/build/lib/libgmock.a /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/googletest/build/lib/libgmock_main.a -lgtest -lgtest_main -lgmock -lpthread
/usr/bin/ld: /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/WinSequences.o: in function `WinSequences::~WinSequences()':
/home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/../WinSequences/WinSequences.cpp:4: undefined reference to `SetWin::~SetWin()'
...
make: *** [Makefile:24: /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/Mode1ScoreTest] Error 1
```

Act as a world-class, expert C++ project debugger and give me ideas for what could be wrong and what fixes to do in which files.