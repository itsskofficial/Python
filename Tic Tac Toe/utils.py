import streamlit as st

def print_board(board):
    for row in board:
        st.write(" ".join(row))
    st.write()