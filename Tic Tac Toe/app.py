import streamlit as st
from utils import *
import time

if "board" not in st.session_state:
    st.session_state.board = [[' ' for _ in range(3)] for _ in range(3)]

if "player" not in st.session_state:
    st.session_state.player = "X"

def app() :
    st.title(":x::o: Tic Tac Toe")
    st.write("You are playing 'O' and the computer is playing 'X'")
    st.write("")
    st.write("")
    st.write("")
    col_1, col_2 = st.columns(2)

    with col_1 :
        print_board()

    with col_2 :
        winner = evaluate()
        if winner is not None:
            if winner == 1:
                st.header(body = "Computer wins!", divider = "rainbow")
            elif winner == -1:
                st.header(body = "You win!", divider = "rainbow")
            else:
                st.header(body = "It's a draw!", divider = "rainbow")
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            if st.button(label = "Play again", type = "primary"):
                for key in st.session_state.keys() :
                    del st.session_state[key]

                st.rerun()

        else :
            if st.session_state.player == 'X':
                st.header(body = "Computer is playing...", divider = "red")
                time.sleep(3)
                move = find_best_move()
                row, col = move
                st.session_state.board[row][col] = st.session_state.player
                st.session_state.player = 'O' 
                st.rerun()
        
            else:
                st.header(body = "Its your turn", divider = "blue")
                row = st.number_input(label = "Enter row: ", min_value = 0, max_value = 2)
                col = st.number_input(label = "Enter column: ", min_value = 0, max_value = 2)
                if st.button(label = "Confirm move", type = "primary") :
                    if st.session_state.board[row][col] == " " :
                        st.session_state.board[row][col] = st.session_state.player
                        st.session_state.player = 'X' 
                        st.rerun()
                    else :
                        st.warning("That block is filled")
app()