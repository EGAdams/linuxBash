My files are as follows:
```
Makefile:
# Compiler settings
CXX := g++
CXXFLAGS := -std=c++14 -Wall -Wextra

# Directories
SRC_DIR   := /home/adamsl/SMOL_AI/tennis_unit_tests/PinInterface
TEST_DIR  := /home/adamsl/SMOL_AI/tennis_unit_tests/PinInterface
BUILD_DIR := /home/adamsl/SMOL_AI/tennis_unit_tests/build/PinInterface

# Google Test and Google Mock directories
GTEST_DIR := /home/adamsl/SMOL_AI/tennis_unit_tests/googletest/build/lib
GMOCK_DIR := /home/adamsl/SMOL_AI/tennis_unit_tests/googletest/build/lib

# Object files and dependencies
TEST_OBJ := $(BUILD_DIR)/MockPinInterface.o
DEPS := $(GTEST_DIR)/libgtest_main.a $(GMOCK_DIR)/libgmock_main.a

# Main target (unit tests)
TARGET := $(BUILD_DIR)/MockPinInterfaceTest

# Targets
.PHONY: all clean

all: $(TARGET)

# Build the unit test executable
$(TARGET): $(TEST_OBJ) $(DEPS)
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Compile the unit test source file
$(BUILD_DIR)/%.o: %.cpp
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Google Test and Google Mock dependencies
$(GTEST_DIR)/libgtest_main.a:
        # Build Google Test if needed

$(GMOCK_DIR)/libgmock_main.a:
        # Build Google Mock if needed

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)

MockPinInterface.cpp:
#include "PinInterface.h"
#include <gmock/gmock.h>

// Create the MOCK class for PinInterface
class MockPinInterface : public PinInterface {
public:
    // Use the constructor of the base class
    using PinInterface::PinInterface;

    // MOCK methods to override the original ones
    MOCK_METHOD(int, pinAnalogRead, (int pin), (override));
    MOCK_METHOD(int, pinDigitalRead, (int pin), (override));
    MOCK_METHOD(void, pinAnalogWrite, (int pin, int value), (override));
    MOCK_METHOD(void, pinDigitalWrite, (int pin, int value), (override));
};

// Define a test fixture (if needed)
class PinInterfaceTest : public ::testing::Test {
protected:
    void SetUp() override {
        // Set up any common data or configuration for your tests
    }

    void TearDown() override {
        // Clean up after your tests (if needed)
    }

    // Add other helper methods or variables specific to your test suite
};

PinInterface.cpp:
#include "PinInterface.h"
#include <string>

PinInterface::PinInterface( PinState* pinState ) : _pinState( pinState ) {}
PinInterface::~PinInterface() {}

std::map<std::string, int> PinInterface::getPinStateMap() { return _pin_map; }

int PinInterface::pinAnalogRead( int pin ) {                         // Analog interface
    std::string pin_string = std::to_string( pin );
    int pin_value = _pinState->getPinState( pin_string );
    return pin_value; }

void PinInterface::pinAnalogWrite( int pin, int value ) { _pinState->setPinState( std::to_string( pin ), value ); }

int PinInterface::pinDigitalRead( int pin ) {                        // Digital interface   
    int pin_value = _pinState->getPinState( std::to_string( pin ));
    return pin_value; }

void PinInterface::pinDigitalWrite( int pin, int value ) { _pinState->setPinState( std::to_string( pin ), value ); }
PinInterface.h:
#ifndef PININTERFACE_H
#define PININTERFACE_H

#include "../PinState/PinState.h"
#include "../Arduino/Arduino.h"
#include <map>

class PinInterface {
  public:
    PinInterface(PinState* pinState);
    ~PinInterface();
    void pinAnalogWrite(int pin, int value);
    void pinDigitalWrite(int pin, int value);
    int pinAnalogRead(int pin);
    int pinDigitalRead(int pin);
    std::map<std::string, int> getPinStateMap();

  private:
    std::map<std::string, int> _pin_map;
    PinState* _pinState;
};

#endif
```

My issue is as follows: I am getting the following error when running:
``` command
    make all
```

``` error
g++ -std=c++14 -Wall -Wextra -c -o /home/adamsl/SMOL_AI/tennis_unit_tests/build/PinInterface/MockPinInterface.o MockPinInterface.cpp
In file included from /usr/local/include/gmock/gmock-actions.h:147,
                 from /usr/local/include/gmock/gmock.h:56,
                 from MockPinInterface.cpp:2:
MockPinInterface.cpp:11:22: error: ‘testing::internal::Function<int(int)>::Result MockPinInterface::pinAnalogRead(testing::internal::ElemFromList<0, int>::type)’ marked ‘override’, but does not override
   11 |     MOCK_METHOD(int, pinAnalogRead, (int pin), (override));
      |                      ^~~~~~~~~~~~~
MockPinInterface.cpp:12:22: error: ‘testing::internal::Function<int(int)>::Result MockPinInterface::pinDigitalRead(testing::internal::ElemFromList<0, int>::type)’ marked ‘override’, but does not override
   12 |     MOCK_METHOD(int, pinDigitalRead, (int pin), (override));
      |                      ^~~~~~~~~~~~~~
MockPinInterface.cpp:13:23: error: ‘testing::internal::Function<void(int, int)>::Result MockPinInterface::pinAnalogWrite(testing::internal::ElemFromList<0, int, int>::type, testing::internal::ElemFromList<1, int, int>::type)’ marked ‘override’, but does not override
   13 |     MOCK_METHOD(void, pinAnalogWrite, (int pin, int value), (override));
      |                       ^~~~~~~~~~~~~~
MockPinInterface.cpp:14:23: error: ‘testing::internal::Function<void(int, int)>::Result MockPinInterface::pinDigitalWrite(testing::internal::ElemFromList<0, int, int>::type, testing::internal::ElemFromList<1, int, int>::type)’ marked ‘override’, but does not override
   14 |     MOCK_METHOD(void, pinDigitalWrite, (int pin, int value), (override));
      |                       ^~~~~~~~~~~~~~~
make: *** [Makefile:34: /home/adamsl/SMOL_AI/tennis_unit_tests/build/PinInterface/MockPinInterface.o] Error 1
```

Act as a world-class, expert C++ project debugger and give me ideas for what could be wrong and what fixes to do in which files.