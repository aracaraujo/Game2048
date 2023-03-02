//
// Created by Arã Araújo on 12/15/22.
//

#ifndef C_BOARD_H
#define C_BOARD_H
#pragma once
#include <vector>
#include <tuple>

using namespace std;

class Board{

private:
    vector<vector<int>> board;
public:
    // Default constructor
    Board();
    // Display the board on the terminal
    void display_board();
    // Check for empty spots at the board
    bool empty_checker();
//    tuple<int,int> empty_checker();
    // Add random numbers to the board
    void add_number();
    // Move the numbers down
    bool move_down();
    // Move the numbers up
    bool move_up();
    // Move the numbers to the right
    bool move_right();
    // Move the numbers to the left
    bool move_left();
    // Check if movements are possible
    bool board_checker();
};
#endif //C_BOARD_H
