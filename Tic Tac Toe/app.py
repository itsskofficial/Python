import streamlit as st
from utils import *

def app() :
    st.title("Tic Tac Toe")
    col_1, col_2 = st.columns(2)
    with col_1 :
        move = find_best_move(board, current_player)
        row, col = move
        board[row][col] = current_player

        print_board(board)
    with col_2 :
        row = int(st.text_input("Enter row number (0 - 2):"))
        col = int(st.text_input("Enter column number (0 - 2): "))
        if st.button("Confirm Move") :
            
