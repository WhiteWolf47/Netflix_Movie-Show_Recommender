import pickle
import streamlit as st


def recommend(movie):
    index = movies[movies['Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    movie_links = []
    sm = []
    imdb = []
    trailers = []
    for i in distances[1:6]:
        # fetch the movie poster
        recommended_movie_posters.append(info.iloc[i[0]].Image)
        recommended_movie_names.append(movies.iloc[i[0]].Title)
        movie_links.append(info.iloc[i[0]]['Netflix Link'])
        sm.append(info.iloc[i[0]]['Series or Movie'])
        imdb.append(info.iloc[i[0]]['IMDb Link'])
        trailers.append(info.iloc[i[0]]['TMDb Trailer'])

    return recommended_movie_names,recommended_movie_posters, movie_links, sm, imdb, trailers


st.header('Netflix Movie/Series Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
info = pickle.load(open('movie_info.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))



movie_list = movies['Title'].values
selected_movie = st.selectbox(
    "SELECT A MOVIE OR SHOW FROM BELOW",
    movie_list
)

if st.button('SHOW RECOMMENDATION'):
    recommended_movie_names, recommended_movie_posters, movie_links, sm, imdb, trailers = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.text(sm[0])
        st.image(recommended_movie_posters[0])
        a = movie_links[0]
        st.write("[Watch on Netflix]({})".format(a))
        b = trailers[0]
        st.write("[Watch Trailer]({})".format(b))
        c = imdb[0]
        st.write("[IMDB]({})".format(c))




    with col2:
        st.text(recommended_movie_names[1])
        st.text(sm[1])
        st.image(recommended_movie_posters[1])
        a = movie_links[1]
        st.write("[Watch on Netflix]({})".format(a))
        b = trailers[1]
        st.write("[Watch Trailer]({})".format(b))
        c = imdb[1]
        st.write("[IMDB]({})".format(c))

    with col3:
        st.text(recommended_movie_names[2])
        st.text(sm[2])
        st.image(recommended_movie_posters[2])
        a = movie_links[2]
        st.write("[Watch on Netflix]({})".format(a))
        b = trailers[2]
        st.write("[Watch Trailer]({})".format(b))
        c = imdb[2]
        st.write("[IMDB]({})".format(c))
    with col4:
        st.text(recommended_movie_names[3])
        st.text(sm[3])
        st.image(recommended_movie_posters[3])
        a = movie_links[3]
        st.write("[Watch on Netflix]({})".format(a))
        b = trailers[3]
        st.write("[Watch Trailer]({})".format(b))
        c = imdb[1]
        st.write("[IMDB]({})".format(c))
    with col5:
        st.text(recommended_movie_names[4])
        st.text(sm[4])
        st.image(recommended_movie_posters[4])
        a = movie_links[4]
        st.write("[Watch on Netflix]({})".format(a))
        b = trailers[4]
        st.write("[Watch Trailer]({})".format(b))
        c = imdb[4]
        st.write("[IMDB]({})".format(c))

page_bg_img = '''
<style>
body {
background-image: url("https://www.desktopbackground.org/download/o/2011/03/30/180042_custom-netflix-wallpapers-2015-part-6-by-espioartwork-102-on-deviantart_1024x628_h.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)