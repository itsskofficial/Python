import streamlit as st
from utils import *

def app() :
    st.title("Tic Tac Toe")
    col_1, col_2 = st.columns(2)
    with col_1 :
        print_board()
    with col_2 :
        row = st.text_input("Enter row number (0 - 2)")
