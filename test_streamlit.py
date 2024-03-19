####################################
## 用于快速选择更优的题目的可视化评价平台
####################################

import streamlit as st
from data_gen import test_data
import random

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if 'cnt' not in st.session_state:
    st.session_state.cnt = 0
    

def submit(dict_map):
    st.session_state.submitted = True
    st.session_state.cnt += 1
    with open("results.txt", "a") as f:
        f.write(f"{dict_map[st.session_state.genre_key]}\n")
   
def unsubmit():
    st.session_state.submitted = False

genre = st.empty()
if not st.session_state.submitted and st.session_state.cnt < len(test_data):
    content = test_data[st.session_state.cnt]
    dict_map = {content['selection1']: '0', content['selection2']: '1'}  # 0: raw, 1: RAG optimized
    selection_list = [content['selection1'], content['selection2']]
    random.seed(st.session_state.cnt)
    random.shuffle(selection_list)
    genre.radio(
        content['description'],
        selection_list,
        index=None,
        key="genre_key",
    )
    st.write("You selected:", st.session_state.genre_key)
    st.button('Submit', on_click=submit, args=(dict_map, ))
elif st.session_state.cnt < len(test_data):
    genre.empty()
    st.button('Next', on_click=unsubmit)
else:
    genre.empty()
    st.write("All finished")