import pandas as pd
import streamlit as st

# Charger le jeu de données
df = pd.read_csv('triplets_metadata_spotify.csv')

# Filtrer les utilisateurs ayant au moins 10 écoutes
df_filtered = df.groupby('user').filter(lambda x: x['listening_count'].sum() >= 10)

# Sélectionner 1000 lignes aléatoires
df = df_filtered.sample(n=1000, random_state=42)

# Titre de l'application
st.title("RECOMMANDATION MUSICALE")

# Barre latérale avec le sommaire
st.sidebar.title("Sommaire")
pages = ["Introduction", "Prétraitement des données", "Visualisation des données", "Modèle de recommandation"]
page = st.sidebar.radio("Aller vers", pages)

if page == pages[0]:
    st.header("Introduction")
    st.markdown("""
    Le projet de recommandation musicale vise à créer un système qui propose des recommandations personnalisées
    aux utilisateurs en fonction de leurs préférences musicales. Grâce à l'utilisation d'algorithmes avancés,
    ce système exploite les données des utilisateurs telles que leurs goûts musicaux, leurs historiques
    d'écoute et leurs interactions avec la plateforme pour générer des suggestions pertinentes.
    
    L'objectif principal est de fournir une expérience d'écoute musicale enrichissante en aidant les utilisateurs à
    découvrir de nouvelles chansons, artistes et genres musicaux qui correspondent à leurs intérêts.
    
    L'application, basée sur Streamlit, offre une interface conviviale où les utilisateurs peuvent
    saisir leur nom d'utilisateur, choisir parmi différentes options de recommandation
    et obtenir des suggestions musicales. En utilisant des méthodes de recommandation
    aléatoire ou basée sur les préférences de l'utilisateur, le système offre
    une expérience personnalisée et interactive. Ce projet permet ainsi aux amateurs
    de musique d'explorer et de profiter d'un large éventail de morceaux adaptés à
    leurs goûts individuels.
    """)
    st.image("spotify.png")
    st.header("Choix du dataset")
    st.markdown("""
    Nous avons initialement travaillé avec un dataset nommé "module4_cleaned". Cependant, après avoir réalisé plusieurs
    opérations et réflexions sur la structure et l'exploitation des données, nous avons conclu, en accord avec notre encadrant,
    que ce jeu de données n'était plus pertinent ni à jour pour générer des recommandations adaptées au contexte actuel.
    """)
    st.image("Data Sci.png")
    
elif page == pages[1]:
    st.header("Prétraitement des données")
    st.subheader("Affichage des cinq premières lignes du dataset")
    st.dataframe(df.head(5))
    st.write("Nombre de lignes du dataframe :", len(df))
    st.write("Description du dataframe :")
    st.write(df.describe())
    
    # Suppression des duplications
    df = df.drop_duplicates(subset=['song_name', 'artist_name'], keep='first').reset_index()
    st.write("Nombre de duplications supprimées :", df['song_name'].duplicated().sum())
    st.write("Nouveau nombre de lignes après suppression des duplications :", len(df))
    
    tracks_feats = df.drop(['user', 'listening_count'], axis=1).drop_duplicates()
    artists = tracks_feats.artist_name
    songs = tracks_feats.song_name
    labels = artists + '-' + songs
    
    st.header("Exemple des étiquettes")
    st.write(labels.head())
    st.image("reco.png")
    st.image("Data Sci.png")
    
elif page == pages[2]:
    st.header("Visualisation des données")
    st.image("Data Sci.png")
    
    visualizations = ['Histogramme', 'Nuage de points', 'Corrélation', 'Corrélation entre les audio features',
                      'Box plot des variables', 'Distribution de la valence', 'Nombre écoutes par paire utilisateurs']

    selected_viz = st.sidebar.selectbox("Sélectionnez une visualisation", visualizations)

    if selected_viz == 'Histogramme':
        st.image("quanti_ditrib.png")
    elif selected_viz == 'Nuage de points':
        st.image("corr_dist_spe.png")
    elif selected_viz == 'Corrélation':
        st.image("quanti_corr_heatmap.png")
    elif selected_viz == 'Corrélation entre les audio features':
        st.image("corr_audio_features.png")
    elif selected_viz == 'Box plot des variables':
        st.image("quanti_boxplot_normalized.png")
    elif selected_viz == 'Distribution de la valence':
        st.image("valence_distrib.png")
    elif selected_viz == 'Nombre écoutes par paire utilisateurs':
        st.image("pair-users.png")
    
elif page == pages[3]:
    st.image("Data Sci.png")
    utilisateur = st.text_input("Entrez votre nom d'utilisateur")

    recommandation = st.selectbox("Choisissez une option de recommandation",
                                 ("Recommandation aléatoire", "Recommandation basée sur vos préférences"))

    if st.button("Obtenir une recommandation"):
        if recommandation == "Recommandation aléatoire":
            st.write("Voici une recommandation aléatoire pour vous :", recommendation_random())
        elif recommandation == "Recommandation basée sur vos préférences":
            if utilisateur:
                st.write("Voici une recommandation basée sur vos préférences :", recommendation_user_based(utilisateur))
            else:
                st.write("Veuillez saisir votre nom d'utilisateur pour obtenir une recommandation personnalisée.")

    def recommendation_random():
        # Code pour générer une recommandation aléatoire
        return "Titre de la chanson recommandée"

    def recommendation_user_based(user):
        # Code pour générer une recommandation basée sur les préférences de l'utilisateur
        return "Titre de la chanson recommandée"
