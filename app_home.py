import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def run_home():
    st.subheader('이 앱은 리뷰데이터를 분석하고, 어떤 문장이 들어오면, 긍정/부정을 에측하는 앱입니다.')