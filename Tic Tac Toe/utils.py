import streamlit as st

def print_board():
    for row in st.session_state.board:
        body = "\t".join(row)
        print(body)
        st.subheader(body = f"{row[0]}\t{row[1]}\t{row[2]}", divider = False)
        st.write("")
        st.write("")

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

def minimax(depth, is_maximizing, alpha, beta):
    result = evaluate()

    if result is not None:
        return result

    if is_maximizing:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if st.session_state.board[row][col] == ' ':
                    st.session_state.board[row][col] = 'X'
                    eval = minimax(depth + 1, False, alpha, beta)
                    st.session_state.board[row][col] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if st.session_state.board[row][col] == ' ':
                    st.session_state.board[row][col] = 'O'
                    eval = minimax(depth + 1, True, alpha, beta)
                    st.session_state.board[row][col] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move() :
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