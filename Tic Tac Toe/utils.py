import streamlit as st

def print_board():
    for row in st.session_state.board:
        st.write(" ".join(row))
    st.write()