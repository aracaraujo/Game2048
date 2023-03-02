#include <iostream>
#include "Board.h"

using namespace std;

int main() {
    Board board;

    board.display_board();
    cout << "" << endl;
    board.add_number();
    board.display_board();



    return 0;
}
