//
// Created by Arã Araújo on 12/15/22.
//

#include "Board.h"
#include <vector>
#include <tuple>
#include <iostream>
#include <random>

using namespace std;
namespace {
    random_device rd;
    mt19937 gen(rd());}

Board::Board() {
    // Feeds the board.
    board.push_back({1,0,0,0});
    board.push_back({2,0,0,0});
    board.push_back({3,0,0,0});
    board.push_back({4,0,0,0});
}

void Board::display_board() {
    //Receives the board in a form of a 2D vector and print in the terminal
    for (const vector<int>& row : this->board) {
        for (int x: row){
            cout << x << " ";
        }
        cout << endl;
    }
}

//tuple<int,int> Board::empty_checker() {
//    tuple<int,int> spot;
//    while (true) {
//        uniform_int_distribution dist(0, 3);
//        int randomRow = dist(gen);
//        vector row = this->board[randomRow];
//        int index = dist(gen);
//        if (row[index] == 0) {
//            spot = make_tuple(randomRow,index);
//            break;
//        }
//    }
//    return spot;
//}

bool Board::empty_checker() {
    uniform_int_distribution dist(0, 3);
    bool status = true;
    int position_checker = 0;
    for (vector<int> row : this->board){
        for (int value : row){
            if (value == 0){
                position_checker += 1;
            }
        }
    }
    if (position_checker == 0){
        return false;
    }else{
        return true;
    }
}

void Board::add_number() {
        while (true) {
            uniform_int_distribution dist(0, 3);
            int random_row = dist(gen);
            vector row = this->board[random_row];
            int spot = dist(gen);
            if (row[spot] == 0) {
                uniform_int_distribution value_dist(0, 4);
                int value = value_dist(gen);
                switch (value) {
                    case 0:
                    case 1:
                    case 3: {
                        value = 2;
                        break;
                        default: {
                            continue;
                        }
                    }
                }
                break;
            }
        }

}
