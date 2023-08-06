My files are as follows: 
```Mode1ScoreTest.cpp:
#include "gtest/gtest.h"
#include "gmock/gmock.h"
#include "Mode1Score.h"

// class MockPlayer : public Player {
// public:
//     MockPlayer(GameState* gameState, int player_number) : Player(gameState, player_number) {}
//     MOCK_METHOD(void, setOpponent, (IPlayer* opponent), (override));
//     MOCK_METHOD(IPlayer*, getOpponent, (), (override));
//     MOCK_METHOD(void, setPoints, (int points), (override));
//     MOCK_METHOD(int, getPoints, (), (override));
//     MOCK_METHOD(void, setGames, (int games), (override));
//     MOCK_METHOD(int, getGames, (), (override));
//     MOCK_METHOD(void, setMatches, (int matches), (override));
//     MOCK_METHOD(int, getMatches, (), (override));
//     MOCK_METHOD(void, setMode, (int mode), (override));
//     MOCK_METHOD(int, getMode, (), (override));
//     MOCK_METHOD(void, setSetting, (int setting), (override));
//     MOCK_METHOD(int, getSetting, (), (override)); 
//     MOCK_METHOD(void, setSets, ( IGameState* state, int sets), (override));
//     MOCK_METHOD(int, getSets, (), (override));
//     MOCK_METHOD(void, setSetHistory, (int set, int score), (override));
//     // MOCK_METHOD(std::map<int, int>, getPlayer1SetHistory, (), (override));
//     // MOCK_METHOD(std::map<int, int>, getPlayer2SetHistory, (), (override));
//     MOCK_METHOD(int, incrementSetting, (), (override));
//     MOCK_METHOD(int, number, (), (override));
// };


// class MockPinInterface : public PinInterface {
// public:
//     MockPinInterface(PinState* pinState) : PinInterface(pinState) {
//         // Initialize your mock object here if necessary
//     }

//     // Add your mock methods here...
// };

// class MockGameState : public GameState {
// public:
//     MOCK_METHOD(int, getServeSwitch, (), (override));
//     MOCK_METHOD(void, setServeSwitch, (int), (override));
//     MOCK_METHOD(int, getUpdateDisplayDelay, (), (override));
//     MOCK_METHOD(int, getTieBreak, (), (override));
//     MOCK_METHOD(void, setTieBreak, (int), (override));
//     MOCK_METHOD(int, getSetTieBreak, (), (override));
//     MOCK_METHOD(void, setSetTieBreak, (int), (override));
//     MOCK_METHOD(int, getPointFlash, (), (override));
//     MOCK_METHOD(void, setPointFlash, (int), (override));
//     MOCK_METHOD( unsigned long, getPreviousTime, (), (override));
//     MOCK_METHOD(void, setPreviousTime, ( unsigned long ), (override));
//     MOCK_METHOD(int, getToggle, (), (override));
//     MOCK_METHOD(void, setToggle, (int), (override));
// };

// class MockHistory : public History {
// public:
//     // Mock methods...
// };

class Mode1ScoreTest : public ::testing::Test {
protected:
    // MockGameState gameState;
    // MockPlayer player1{&gameState, 1}, player2{&gameState, 2};
    GameState gameState;
    Player player1{&gameState, 1}, player2{&gameState, 2};
    // MockPlayer player1{&gameState, 1}, player2{&gameState, 2};
    std::map<std::string, int> pinMap; // You may need to populate this map as necessary
    PinState pinState{pinMap};
    PinInterface pinInterface{&pinState};
    // MockHistory history;
    History history;
    Mode1Score* mode1Score;

    Mode1ScoreTest() {
        mode1Score = new Mode1Score( &player1, &player2, &pinInterface, &gameState, &history );
    }

    void TearDown() override {
        delete mode1Score;
    }
};




// TEST_F(Mode1ScoreTest, Mode1P1ScoreTest) {
//     // Now you can use player1, player2, pinInterface, gameState, and history

//     // Set player 1 score to 2
//     player1.setPoints( 2 );

//     // Call the mode1P1Score method
//     mode1Score->mode1P1Score();

//     // Check that the score has been updated correctly
//     ASSERT_EQ(player1.getPoints(), 3 );
// }


// TEST_F(Mode1ScoreTest, TestMode1P1Score_LessThan3Points) {
//     // Arrange
//     EXPECT_CALL(player1, getPoints()).WillOnce(::testing::Return(2));

//     // Act
//     mode1Score->mode1P1Score();

//     // Assert
//     // Assertions are made in the EXPECT_CALL statements
// }

// TEST_F(Mode1ScoreTest, TestMode1P1Score_3Points_LessThan3PointsP2) {
//     // Arrange
//     EXPECT_CALL(player1, getPoints()).WillOnce(::testing::Return(3));
//     EXPECT_CALL(player2, getPoints()).WillOnce(::testing::Return(2));

//     // Act
//     mode1Score->mode1P1Score();

//     // Assert
//     // Assertions are made in the EXPECT_CALL statements
// }

// TEST_F(Mode1ScoreTest, TestMode1P1Score_3Points_EqualPoints) {
//     // Arrange
//     EXPECT_CALL(player1, getPoints()).WillOnce(::testing::Return(3));
//     EXPECT_CALL(player2, getPoints()).WillOnce(::testing::Return(3));
//     EXPECT_CALL(player1, setPoints(3)).Times(1);
//     EXPECT_CALL(player2, setPoints(3)).Times(1);

//     // Act
//     mode1Score->mode1P1Score();

//     // Assert
//     // Assertions are made in the EXPECT_CALL statements
// }

// TEST_F(Mode1ScoreTest, TestMode1P1Score_MoreThan3Points_DifferenceMoreThan1) {
//     // Arrange
//     EXPECT_CALL(player1, getPoints()).WillOnce(::testing::Return(5));
//     EXPECT_CALL(player2, getPoints()).WillOnce(::testing::Return(3));
//     EXPECT_CALL(player1, getGames()).WillOnce(::testing::Return(1));
//     EXPECT_CALL(player1, setGames(2)).Times(1);

//     // Act
//     mode1Score->mode1P1Score();

//     // Assert
//     // Assertions are made in the EXPECT_CALL statements
// }

// TEST_F(Mode1ScoreTest, TestMode1P1Score_4Points) {
//     // Arrange
//     EXPECT_CALL(player1, getPoints()).WillOnce(::testing::Return(4));
//     EXPECT_CALL(gameState, setPointFlash(1)).Times(1);
//     EXPECT_CALL(gameState, setToggle(0)).Times(1);

//     // Act
//     mode1Score->mode1P1Score();

//     // Assert
//     // Assertions are made in the EXPECT_CALL statements
// }

Mode1Score.cpp:
#include "Mode1Score.h"

Mode1Score::Mode1Score( IPlayer* player1, IPlayer* player2,
    PinInterface* pinInterface, GameState* gameState, History* history ) :
    _player1( player1 ),
    _player2( player2 ),
    _gameState( gameState ),
    _history( history ),
    _mode1TieBreaker( player1, player2, pinInterface, gameState, history ),
    _pointLeds( player1, player2, pinInterface ),
    _gameLeds( player1, player2, pinInterface ),
    _setLeds( player1, player2, pinInterface ),
    _mode1WinSequences( player1, player2, pinInterface, gameState ),
    _undo( player1, player2, pinInterface, gameState ) {}
Mode1Score::~Mode1Score() {}

void Mode1Score::setScoreBoard( ScoreBoard* scoreBoard ) { 
    _pointLeds.setScoreBoard(          scoreBoard ); 
    _gameLeds.setScoreBoard(           scoreBoard ); 
    _mode1WinSequences.setScoreBoards( scoreBoard ); 
    _setLeds.setScoreBoard(            scoreBoard ); }

void Mode1Score::_resetGame() {
     GameTimer::gameDelay( UPDATE_DISPLAY_DELAY );
    _player1->setPoints( 0 );
    _player2->setPoints( 0 );
    _gameState->setServeSwitch( 1 );
    _gameState->setServe( 0 );
    _pointLeds.updatePoints(); }

void Mode1Score::updateScore( IPlayer* currentPlayer ) {
    IPlayer* otherPlayer = currentPlayer->getOpponent();
    if ( currentPlayer->getPoints() >= 3 ) {
        if ( currentPlayer->getPoints() == otherPlayer->getPoints()) {
            currentPlayer->setPoints( 3 );
            otherPlayer->setPoints( 3 );
        } else if ( currentPlayer->getPoints() > 3 && ( currentPlayer->getPoints() - otherPlayer->getPoints()) > 1 ) {
            currentPlayer->setGames( currentPlayer->getGames() + 1);
            _undo.memory();
            currentPlayer->number() == 1 ? mode1P1Games() : mode1P2Games(); }
        if ( currentPlayer->getPoints() == 4 ) {
            // std::cout << "inside updateScore().  points == 4.  setting point flash to 1..." << std::endl;
            _gameState->setPointFlash( 1 );
            _gameState->setPreviousTime( GameTimer::gameMillis());
            _gameState->setToggle( 0 ); }}
    // std::cout << "inside updateScore().  updating points..." << std::endl;
    _pointLeds.updatePoints(); }

void Mode1Score::mode1P1Score() { updateScore( _player1 );}
void Mode1Score::mode1P2Score() { updateScore( _player2 );}


/////////////////////////////////////// MODE 1 GAMES //////////////////////////////////////////////
void Mode1Score::mode1P1Games() {
    // _gameLeds.updateGames();
    _gameState->setServeSwitch( _gameState->getServeSwitch() + 1 );
    if ( _player1->getGames() >= GAMES_TO_WIN_SET ) {
        if ( _player1->getGames() == GAMES_TO_WIN_SET && _player2->getGames() == GAMES_TO_WIN_SET ) {
            _gameState->setTieBreak( 1 );
            _mode1TieBreaker.tieBreakEnable(); }
        if ( _gameState->getTieBreak() == 0 ) {
            std::cout << "*** tie break is zero.  checking if p1 games - p2 games > 1... ***" << std::endl;
            if( !_player1 || !_player2 ) { std::cout << "*** ERROR: player1 or player2 is NULL.  exiting... ***" << std::endl; exit( 1 ); }
            std::cout << "*** player1 games: " << _player1->getGames() << " player2 games: " << _player2->getGames() << std::endl;
            if (( _player1->getGames() - _player2->getGames()) > 1 ) {
                std::cout << "*** setting sets for player 1... ***" << std::endl;
                _player1->setSets( _gameState, _player1->getSets() + 1 ); // <-------------<< Increment Player Sets
                _setLeds.updateSets();
                if ( _player1->getSets() == _player2->getSets()) {        // <-------------<< Set Tie Break
                    std::cout << "*** calling p1TBSetWinSequence() ***" << std::endl;
                    _mode1WinSequences.p1TBSetWinSequence();
                    _gameState->setSetTieBreak( 1 );
                    _mode1TieBreaker.setTieBreakEnable();
                } else if ( _player1->getSets() == SETS_TO_WIN_MATCH ) {
                    std::cout << "*** calling p1MatchWinSequence() ***" << std::endl;
                    _mode1WinSequences.p1MatchWinSequence();             // <-------------<< Match Win
                    _gameState->stopGameRunning();
                } else {                                                 // <-------------<< Set Win
                    std::cout << "*** /// calling p1SetWinSequence() point gap is 2 /// ***" << std::endl;
                    _gameState->setPlayer1SetHistory( _player1->getSetHistory());
                    _gameState->setPlayer2SetHistory( _player2->getSetHistory());
                    _gameState->setCurrentSet( _gameState->getCurrentSet() + 1 );
                    _mode1WinSequences.p1SetWinSequence();
                    _setLeds.updateSets();
                    GameTimer::gameDelay( _gameState->getWinDelay());
                    _resetGame(); }
                    std::cout << "*** setting games to 0 ***" << std::endl;
                    _player1->setGames( 0 );
                    _player2->setGames( 0 );
            } else {    // no set win, no match win, no tie break. just a regular game win.
                std::cout << "*** calling p1GameWinSequence() ***" << std::endl;
                _gameLeds.updateGames();
                _gameState->setPlayer1SetHistory( _player1->getSetHistory());
                _gameState->setPlayer2SetHistory( _player2->getSetHistory());
                _mode1WinSequences.p1GameWinSequence();  // sets player points to zero
                _resetGame();
            }}
    } else {
        std::cout << "*** calling p1GameWinSequence() ***" << std::endl;
        _gameLeds.updateGames();
        _gameState->setPlayer1SetHistory( _player1->getSetHistory());
        _gameState->setPlayer2SetHistory( _player2->getSetHistory());
        _mode1WinSequences.p1GameWinSequence();
        _resetGame(); }}

void Mode1Score::mode1P2Games() {
    // std::cout << "inside mode1P2Games().  updtating game leds..." << std::endl;
    // _gameLeds.updateGames();
    // std::cout << "inside mode1P2Games().  setting serve switch..." << std::endl;
    _gameState->setServeSwitch( _gameState->getServeSwitch() + 1 );
    // std::cout << "serve switch set to: " << _gameState->getServeSwitch() << std::endl;
    if ( _player2->getGames()  >= GAMES_TO_WIN_SET ) {
        if ( _player2->getGames()  == GAMES_TO_WIN_SET && _player1->getGames() == GAMES_TO_WIN_SET ) {
            _gameState->setTieBreak( 1 );
            std::cout << "*** calling tieBreakEnable() from inside Mode1Score::mode1P2Games()... ***" << std::endl;
            _mode1TieBreaker.tieBreakEnable();
        }
        if ( _gameState->getTieBreak() == 0 ) {
            if (( _player2->getGames() - _player1->getGames()) > 1 ) {
                _player2->setSets( _gameState, _player2->getSets() + 1 ); // Increment Sets!
                _setLeds.updateSets();
                if ( _player2->getSets() == _player1->getSets()) {
                    _mode1WinSequences.p2TBSetWinSequence();
                    _gameState->setSetTieBreak( 1 );
                    _mode1TieBreaker.setTieBreakEnable();
                }
                else if ( _player2->getSets() == SETS_TO_WIN_MATCH ) {
                    _mode1WinSequences.p2MatchWinSequence();
                    _gameState->stopGameRunning();
                }  else {
                    std::cout << "** inside mode1P2Games().  calling p2SetWinSequence()... ***" << std::endl;
                    _player2->setGames( _player2->getGames() );
                    _gameState->setPlayer1SetHistory( _player1->getSetHistory());
                    _gameState->setPlayer2SetHistory( _player2->getSetHistory());
                    _gameState->setCurrentSet( _gameState->getCurrentSet() + 1 );
                    _mode1WinSequences.p2SetWinSequence();
                    _setLeds.updateSets();
                    GameTimer::gameDelay( _gameState->getWinDelay());
                    _resetGame();
                    std::cout << "*** setting games to 0 ***" << std::endl;
                    _player1->setGames( 0 );
                    _player2->setGames( 0 ); }}

                std::cout << "inside mode1P2Games().  setting games to 0..." << std::endl;
                _player1->setGames( 0 );
                _player2->setGames( 0 );
            } else {
                std::cout << "inside mode1P2Games().  calling p2GameWinSequence()..." << std::endl;
                _gameLeds.updateGames();
                _gameState->setPlayer1SetHistory( _player1->getSetHistory());
                _gameState->setPlayer2SetHistory( _player2->getSetHistory());
                _gameState->setCurrentSet( _gameState->getCurrentSet() + 1 );
                _mode1WinSequences.p2GameWinSequence();
                _resetGame(); }
    } else {
        _gameLeds.updateGames();
        _mode1WinSequences.p2GameWinSequence();  // sets player points to zero
        _gameState->setPlayer1SetHistory( _player1->getSetHistory());
        _gameState->setPlayer2SetHistory( _player2->getSetHistory());
        _resetGame(); }}
////////////////////////////////// END MODE 1 GAMES ///////////////////////////////////////////////

void Mode1Score::mode1TBP1Games() {
    _gameLeds.updateGames();
    _gameState->setServeSwitch( _gameState->getServeSwitch() + 1 );
    GameTimer::gameDelay( UPDATE_DISPLAY_DELAY );
    if ( _player1->getGames() == 15 ) {
        _player1->setSets( _gameState, _player1->getSets() + 1 );

        if ( _player2->getSets() == _player1->getSets()) {
            _mode1TieBreaker.endTieBreak();
            _mode1WinSequences.p1TBSetWinSequence();
            _gameState->setSetTieBreak( 1 );
            _mode1TieBreaker.setTieBreakEnable();
        }
        else {
            _player1->setGames( _player1->getGames() );
            _gameState->setPlayer1SetHistory( _player1->getSetHistory());
            _gameState->setPlayer2SetHistory( _player2->getSetHistory());
            _gameState->setCurrentSet( _gameState->getCurrentSet() + 1 );
            _mode1WinSequences.p1SetWinSequence();
            _mode1TieBreaker.endTieBreak();
        }}
    if ( _player1->getGames() >= 10 &&
        ( _player1->getGames() - _player2->getGames()) > 1 ) {
        _player1->setSets( _gameState, _player1->getSets() + 1 );
        if ( _player2->getSets() == _player1->getSets()) {
            _mode1TieBreaker.endTieBreak();
            _mode1WinSequences.p1TBSetWinSequence();
            _gameState->setSetTieBreak( 1 );
            _mode1TieBreaker.setTieBreakEnable();
        }
        else {
            _player1->setGames( _player1->getGames() );
            _gameState->setPlayer1SetHistory( _player1->getSetHistory());
            _gameState->setPlayer2SetHistory( _player2->getSetHistory());
            _gameState->setCurrentSet( _gameState->getCurrentSet() + 1 );
            _mode1WinSequences.p1SetWinSequence();
            _mode1TieBreaker.endTieBreak();
        }}}

void Mode1Score::mode1SetTBP1Games() {
    _gameLeds.updateGames();
    GameTimer::gameDelay( UPDATE_DISPLAY_DELAY );
    if ( _player1->getGames() == 7 ) {
        _player1->setSets( _gameState, _player1->getSets() + 1 );
        _setLeds.updateSets();
        GameTimer::gameDelay( UPDATE_DISPLAY_DELAY );
        _mode1WinSequences.p1SetTBWinSequence();
        _mode1TieBreaker.tieLEDsOff();
        _mode1WinSequences.p1MatchWinSequence();
        _gameState->stopGameRunning(); }
    _gameState->setServeSwitch( _gameState->getServeSwitch() + 1 ); }

void Mode1Score::mode1TBP2Games() {
    _gameLeds.updateGames();
    _gameState->setServeSwitch( _gameState->getServeSwitch() + 1 );
    GameTimer::gameDelay( UPDATE_DISPLAY_DELAY );
    if ( _player2->getGames() == 15 ) {
        _player2->setSets( _gameState, _player2->getSets() + 1 );
        if ( _player2->getSets() == _player1->getSets()) {
            _mode1TieBreaker.endTieBreak();
            _mode1WinSequences.p2TBSetWinSequence();
            _gameState->setSetTieBreak( 1 );
            _mode1TieBreaker.setTieBreakEnable();
        } else {
            _player1->setGames( _player1->getGames() );
            _gameState->setPlayer1SetHistory( _player1->getSetHistory());
            _gameState->setPlayer2SetHistory( _player2->getSetHistory());
            _gameState->setCurrentSet( _gameState->getCurrentSet() + 1 );
            _mode1WinSequences.p2SetWinSequence();
            _mode1TieBreaker.endTieBreak(); }}
    if ( _player2->getGames() >= 10 &&
        ( _player2->getGames() - _player1->getGames()) > 1 ) {
        _player2->setSets( _gameState, _player2->getSets() + 1 );
        if ( _player2->getSets() == _player1->getSets()) {
            _mode1TieBreaker.endTieBreak();
            _mode1WinSequences.p2TBSetWinSequence();
            _gameState->setSetTieBreak( 1 );
            _mode1TieBreaker.setTieBreakEnable();
        } else {
            _player1->setGames( _player1->getGames() );
            _gameState->setPlayer1SetHistory( _player1->getSetHistory());  // set set history, set++
            _gameState->setPlayer2SetHistory( _player2->getSetHistory());
            _gameState->setCurrentSet( _gameState->getCurrentSet() + 1 );
            _mode1WinSequences.p2SetWinSequence();
            _mode1TieBreaker.endTieBreak(); }}}

void Mode1Score::mode1SetTBP2Games() {
    _gameLeds.updateGames();
    GameTimer::gameDelay( UPDATE_DISPLAY_DELAY );
    if ( _player2->getGames() == 7 ) {
        _player2->setSets( _gameState, _player2->getSets() + 1 );
        _setLeds.updateSets();
        GameTimer::gameDelay( UPDATE_DISPLAY_DELAY );
        _mode1WinSequences.p2SetTBWinSequence();
        _mode1TieBreaker.tieLEDsOff();
        _mode1WinSequences.p2MatchWinSequence(); 
        _gameState->stopGameRunning(); }
    _gameState->setServeSwitch( _gameState->getServeSwitch() + 1 ); }
Makefile:
CXX := g++  # Compiler settings
CXXFLAGS := -std=c++14 -Wall -Wextra -g

SRC_DIR   := /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score  # Directories
TEST_DIR  := /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score
BUILD_DIR := /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score

# Google Test and Google Mock directories
GTEST_DIR := /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/googletest/build/lib
GMOCK_DIR := /home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/googletest/build/lib

# Object files and dependencies
TEST_OBJ := $(BUILD_DIR)/ModeTieBreaker.o $(BUILD_DIR)/Mode1ScoreTest.o $(BUILD_DIR)/PinState.o $(BUILD_DIR)/Mode1Score.o $(BUILD_DIR)/TranslateConstant.o
DEPS := $(GTEST_DIR)/libgtest.a $(GTEST_DIR)/libgtest_main.a $(GMOCK_DIR)/libgmock.a $(GMOCK_DIR)/libgmock_main.a

TARGET := $(BUILD_DIR)/Mode1ScoreTest  # Main target (unit tests)

.PHONY: all clean # Targets

all: $(TARGET)

$(TARGET): $(TEST_OBJ) $(DEPS)  # Build the unit test executable
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -o $@ $^ -lgtest -lgtest_main -lpthread

$(BUILD_DIR)/%.o: %.cpp # Compile the unit test source file
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Compile the Mode1TieBreaker, Mode1Score, and TranslateConstant source files
$(BUILD_DIR)/Mode1TieBreaker.o: ../Mode1TieBreaker/Mode1TieBreaker.cpp
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -c -o $@ $<
	
# Compile the PinState, Mode1Score, and TranslateConstant source files
$(BUILD_DIR)/PinState.o: ../PinState/PinState.cpp
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

$(BUILD_DIR)/Mode1Score.o: Mode1Score.cpp
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

$(BUILD_DIR)/TranslateConstant.o: ../TranslateConstant/TranslateConstant.cpp
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

$(GTEST_DIR)/libgtest_main.a:  # Google Test and Google Mock dependencies
$(GMOCK_DIR)/libgmock_main.a:


clean:                          # Clean build artifacts
	find $(BUILD_DIR) -type f -name '*.o' -delete
	rm -f $(TARGET)
Mode1Score.h:
#ifndef MODE_1_SCORE_H
#define MODE_1_SCORE_H

#include "../Arduino/Arduino.h"
#include "../GameLeds/GameLeds.h"
#include "../GameState/GameState.h"
#include "../GameTimer/GameTimer.h"
#include "../Mode1Tiebreaker/Mode1Tiebreaker.h"
#include "../WinSequences/WinSequences.h"
#include "../PointLeds/PointLeds.h"
#include "../PinInterface/PinInterface.h"
#include "../Player/Player.h"
#include "../SetLeds/SetLeds.h"
#include "../Undo/Undo.h"
#include "../TennisConstants/TennisConstants.h"
#include <iostream>

class Mode1Score {
 public:
    Mode1Score( IPlayer* player1,
                IPlayer* player2,
                PinInterface* pinInterface,
                GameState* gameState,
                History* history );
    ~Mode1Score();
    void mode1P1Score();
    void mode1P1Games();
    void mode1TBP1Games();
    void mode1SetTBP1Games();
    void mode1P2Score();
    void mode1P2Games();
    void mode1TBP2Games();
    void mode1SetTBP2Games();
    void setScoreBoard( ScoreBoard* scoreBoard );
    void updateScore(   IPlayer* currentPlayer  );

 private:
    void _resetGame();
    IPlayer* _player1;
    IPlayer* _player2;
    GameState* _gameState;
    History* _history;
    Mode1TieBreaker _mode1TieBreaker;
    PointLeds _pointLeds;
    GameLeds _gameLeds;
    SetLeds _setLeds;
    WinSequences _mode1WinSequences;
    Undo _undo;
    ScoreBoard* _scoreBoard; };
#endif
```

My issue is as follows: I am getting the following error when running:
``` command
    make all
```

``` error
g++   -std=c++14 -Wall -Wextra -g    Mode1ScoreTest.cpp   -o Mode1ScoreTest
In file included from ../GameLeds/../ScoreBoard/../NumberDrawer/../../include/led-matrix.h:31,
                 from ../GameLeds/../ScoreBoard/../NumberDrawer/NumberDrawer.h:4,
                 from ../GameLeds/../ScoreBoard/ScoreBoard.h:7,
                 from ../GameLeds/GameLeds.h:8,
                 from Mode1Score.h:5,
                 from Mode1ScoreTest.cpp:3:
../GameLeds/../ScoreBoard/../NumberDrawer/../../include/pixel-mapper.h: In member function ‘virtual bool rgb_matrix::PixelMapper::SetParameters(int, int, const char*)’:
../GameLeds/../ScoreBoard/../NumberDrawer/../../include/pixel-mapper.h:51:34: warning: unused parameter ‘chain’ [-Wunused-parameter]
   51 |   virtual bool SetParameters(int chain, int parallel,
      |                              ~~~~^~~~~
../GameLeds/../ScoreBoard/../NumberDrawer/../../include/pixel-mapper.h:51:45: warning: unused parameter ‘parallel’ [-Wunused-parameter]
   51 |   virtual bool SetParameters(int chain, int parallel,
      |                                         ~~~~^~~~~~~~
../GameLeds/../ScoreBoard/../NumberDrawer/../../include/pixel-mapper.h:52:42: warning: unused parameter ‘parameter_string’ [-Wunused-parameter]
   52 |                              const char *parameter_string) {
      |                              ~~~~~~~~~~~~^~~~~~~~~~~~~~~~
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/9/../../../x86_64-linux-gnu/Scrt1.o: in function `_start':
(.text+0x24): undefined reference to `main'
collect2: error: ld returned 1 exit status
make: *** [<builtin>: Mode1ScoreTest] Error 1
```

Give me ideas for what could be wrong and what fixes to do in which files.