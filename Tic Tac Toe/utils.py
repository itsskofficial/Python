import streamlit as st

def print_board():
    for row in st.session_state.board:
        st.write(" ".join(row))
    st.write()

def evaluate():
    for row in st.session_state.board:
        if all(cell == 'X' for cell in row):
            return 1
        if all(cell == 'O' for cell in row):
            return -1

    for col in range(3):
        if all(st.session_state.board[row][col] == 'X' for row in range(3)):
            return 1
        if all(st.session_state.board[row][col] == 'O' for row in range(3)):
            return -1

    if all(st.session_state.board[i][i] == 'X' for i in range(3)) or all(st.session_state.board[i][2 - i] == 'X' for i in range(3)):
        return 1

    if all(st.session_state.board[i][i] == 'O' for i in range(3)) or all(st.session_state.board[i][2 - i] == 'O' for i in range(3)):
        return -1

    if all(cell != ' ' for row in st.session_state.board for cell in row):
        return 0

    return None