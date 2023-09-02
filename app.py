import pickle
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('Course Recommender System')
course = pickle.load(open('courses.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

indices = pd.Series(
    course.index, index=course['Course Name']).drop_duplicates()


def get_recommendations(title, cosine_sim=similarity):
    idx = indices[title]
    recommended_course_names = []
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    courses_fin = [i[0] for i in sim_scores]
    for i in range(5):
        recommended_course_names.append(
            course['Course Name'].iloc[courses_fin[i]])

    return recommended_course_names, courses_fin


course_list = course['Course Name'].values
selected_course = st.selectbox(
    "Type or select a course from the dropdown",
    course_list
)

if st.button('Show Recommendation'):
    recommended_course_names, course_index = get_recommendations(
        selected_course)
    tab1, tab2, tab3, tab4, tab5 = st.tabs(recommended_course_names)
    with tab1:
        st.text(f"University:    {course['University'].iloc[course_index[0]]}")
        st.text(
            f"Difficulty Level:   {course['Difficulty Level'].iloc[course_index[0]]}")
        st.write(
            f"[Course Link]({course['Course URL'].iloc[course_index[0]]})")
    with tab2:
        st.text(f"University:    {course['University'].iloc[course_index[1]]}")
        st.text(
            f"Difficulty Level:   {course['Difficulty Level'].iloc[course_index[1]]}")
        st.write(
            f"[Course Link]({course['Course URL'].iloc[course_index[1]]})")
    with tab3:
        st.text(f"University:    {course['University'].iloc[course_index[2]]}")
        st.text(
            f"Difficulty Level:   {course['Difficulty Level'].iloc[course_index[2]]}")
        st.write(
            f"[Course Link]({course['Course URL'].iloc[course_index[2]]})")
    with tab4:
        st.text(f"University:    {course['University'].iloc[course_index[3]]}")
        st.text(
            f"Difficulty Level:   {course['Difficulty Level'].iloc[course_index[3]]}")
        st.write(
            f"[Course Link]({course['Course URL'].iloc[course_index[3]]})")
    with tab5:
        st.text(f"University:    {course['University'].iloc[course_index[4]]}")
        st.text(
            f"Difficulty Level:   {course['Difficulty Level'].iloc[course_index[4]]}")
        st.write(
            f"[Course Link]({course['Course URL'].iloc[course_index[4]]})")
