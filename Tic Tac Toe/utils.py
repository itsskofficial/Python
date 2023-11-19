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

def minimax():
    result = evaluate(st.session_state.board)

    if result is not None:
        return result

    if st.session_state.is_maximizing:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if st.session_state.board[row][col] == ' ':
                    st.session_state.board[row][col] = 'X'
                    eval = minimax(st.session_state.board, st.session_state.depth + 1, False, st.session_state.alpha, st.session_state.beta)
                    st.session_state.board[row][col] = ' '
                    max_eval = max(max_eval, eval)
                    st.session_state.alpha = max(st.session_state.alpha, eval)
                    if st.session_state.beta <= st.session_state.alpha:
                        break
        return max_eval
    
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if st.session_state.board[row][col] == ' ':
                    st.session_state.board[row][col] = 'O'
                    eval = minimax(st.session_state.board, st.session_state.depth + 1, True, st.session_state.alpha, st.session_state.beta)
                    st.session_state.board[row][col] = ' '
                    min_eval = min(min_eval, eval)
                    st.session_state.beta = min(beta, eval)
                    if st.session_state.beta <= st.session_state.alpha:
                        break
        return min_eval