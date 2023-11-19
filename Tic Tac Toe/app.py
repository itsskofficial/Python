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
        print_board()

    with col_2 :
            
        winner = evaluate()
        if winner is not None:
            if winner == 1:
                st.write("Player 'X' wins!")
            elif winner == -1:
                st.write("Player 'O' wins!")
            else:
                st.write("It's a draw!")
            
            if st.button("Play again"):
                for key in st.session_state.keys :
                    del st.session_state[key]

                st.rerun()

        else :
            
            current_player = 'O' if current_player == 'X' else 'X'

        if st.session_state.player == 'X':
            move = find_best_move()
            row, col = move
            st.session_state.board[row][col] = st.session_state.player
    
        else:
            row = int(st.text_input("Enter row (0, 1, 2): "))
            col = int(st.text_input("Enter column (0, 1, 2): "))
            st.session_state.board[row][col] = st.session_state.player
            
