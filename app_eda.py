import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda() :
    df = pd.read_csv('data/review2.csv', index_col=0)

    st.dataframe(df)

    st.text('리뷰의 길이별 히스토그램')

    fig1 = plt.figure()
    df['length'].hist()
    st.pyplot(fig1)

    st.text('리뷰의 길이가 가장 긴 데이터')
    st.dataframe(df.loc[ df['length'] == df['length'].max() , ])

    st.text('리뷰의 길이가 가장 짧은 데이터')
    st.dataframe(df.loc[ df['length'] == df['length'].min() , ])



    # 리뷰의 별점을 셀랙트 박스로 만들어서 유저에게 보여준다.
    # 유저는, 4를 선택하면, 별점이 4인 데이터만 가져와서,
    # 별점과 리뷰내용만 보여준다.
    star_menu = sorted(df['stars'].unique())

    selected =st.selectbox('별점 선택', star_menu )

    st.dataframe(df.loc[df['stars']==selected, ['stars','text']])

       