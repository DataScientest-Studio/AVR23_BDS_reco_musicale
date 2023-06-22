import pandas as pd
import streamlit as st

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
    
    affichages = ['Head', 'Informations sur les variables', 'Longueur du dataframe', 'Réduction des redondances',
                  'Statistiques', 'Création des labels (artistes-chansons)']
    
    selected_affichage = st.sidebar.selectbox("Sélectionnez un affichage", affichages)

    if selected_affichage == 'Head':
        st.write("Affichage des cinq premières lignes du dataset")
        st.image("df_head.png")
    elif selected_affichage == 'Informations sur les variables':
        st.write("Informations sur les données du dataframe :")
        st.image("df_info.png")
    elif selected_affichage == 'Longueur du dataframe':
        st.write("Longueur du dataframe avant traitement :")
        st.image("df_len.png")
    elif selected_affichage == 'Réduction des redondances':
        st.write("Réduction des redondances :")
        st.image("df_drop_dup.png")
    elif selected_affichage == 'Statistiques':
        st.write("Statistiques du dataframe:")
        st.image("df_stat.png")    
    elif selected_affichage == 'Création des labels (artistes-chansons)':
        st.write("Création des labels (artistes-chansons):")
        st.image("df_label.png")
    st.image("reco.png")
    st.image("Data Sci.png")
    
elif page == pages[2]:
    st.header("Visualisation des données")
    st.image("Data Sci.png")
    
    visualizations = ['Histogramme : Distribution du nombre découtes', 'Histogramme : Distribution du nombre de morceaux différents',
                      'Histogramme : Distribution du nombre dartistes différents', 'Nuage de points', 'Corrélation',
                      'Box plot des variables', 'Nombre découtes par paire dutilisateurs', 'Top 30 des morceaux en fonction des variables']
    
    selected_viz = st.sidebar.selectbox("Sélectionnez une visualisation", visualizations)

    if selected_viz == 'Histogramme : Distribution du nombre découtes':
        st.image("user_list_count_dis.png")
    elif selected_viz == 'Nuage de points':
        st.image("pairplot_tracks.png")
    elif selected_viz == 'Corrélation':
        st.image("corr_tracks.png")
    elif selected_viz == 'Histogramme : Distribution du nombre de morceaux différents':
        st.image("user_song_dist.png")
    elif selected_viz == 'Box plot des variables':
        st.image("boxplots_tracks.png")
    elif selected_viz == 'Histogramme : Distribution du nombre dartistes différents':
        st.image("user_art_dist.png")
    elif selected_viz == 'Nombre découtes par paire dutilisateurs':
        st.image("pair-users.png")
    elif selected_viz == 'Top 30 des morceaux en fonction des variables':
        st.image("top_thirty.png")
        
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

