import streamlit as st
from utils import *

if "board" not in st.session_state:
    st.session_state.board = [[' ' for _ in range(3)] for _ in range(3)]

if "player" not in st.session_state:
    st.session.state.player = "X"

def app() :
    st.title("Tic Tac Toe")
    col_1, col_2 = st.columns(2)

    with col_1 :
        move = find_best_move()
        row, col = move
        st.session_state.board[row][col] = st.session_state.player

        print_board()

    with col_2 :

        while True:
            move = find_best_move()

            row, col = move
            board[row][col] = current_player

            print_board(board)

            winner = evaluate(board)
            if winner is not None:
                if winner == 1:
                    print("Player 'X' wins!")
                elif winner == -1:
                    print("Player 'O' wins!")
                else:
                    print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        if st.session_state.player == 'X':
            best_val = -float('inf')
            best_move = None
            alpha = -float('inf')
            beta = float('inf')

            for row in range(3):
                for col in range(3):
                    if st.session_state.board[row][col] == ' ':
                        st.session_state.board[row][col] = 'X'
                        move_val = minimax(0, False, alpha, beta)
                        st.session_state.board[row][col] = ' '

                        if move_val > best_val:
                            best_move = (row, col)
                            best_val = move_val
            return best_move
    
        elif st.session_state.player == 'O':
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            return row, col
            
