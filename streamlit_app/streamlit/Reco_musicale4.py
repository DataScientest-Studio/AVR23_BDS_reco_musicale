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
    #st.markdown(""

    
    definition = st.checkbox("**Qu'est-ce qu'un système de recommandation ?**")
    
    
    if definition:
        #st.write("## Markdown")
        st.write("""
        - Il s'agit d'un système dit "intelligent" composé d'algorithmes d'analyse et de filtrage des données de différents utilisateurs
            qui a pour but de mesurer leur affinité pour certains items et, grâce à cette affinité,
            de prédire un classement des items les plus susceptibles de leur plaire afin de proposer aux utilisateurs des **recommandations ciblées**.
        
        - **Ou en rencontre t'on**?
        Ils sont aujourd'hui omniprésents: plateformes de recommandation de films, de musiques, réseaux sociaux, sites d'e-commerce
        """)
        
    objectif = st.checkbox("**Les objectifs d'un système de recommandation musicale**")
    if objectif:
        st.write("""
        - Fournir une expérience d'écoute musicale enrichissante 
        - Aider les utilisateurs à découvrir de nouvelles chansons, artistes et genres musicaux 
        - En leur proposant des titres semblales ou différents de leurs goûts 

        **Quels problèmes cela pose t'il?**
        - Proposition de titres similaires aux goûts des utilisateurs: problème de 'bulles de filtre' ou l'accès à l'information est limitée
        - Proposition de titres différents: pari risqué, cela plaira t'il à l'utilisateur? Potentiellement oui, la sérendipité est au rendez-vous 
        """)
        st.image('syst_reco_mus.png')

    types = st.checkbox("**Les types de systèmes de recommandation**")
    if types:
        st.write("""
        - Il en existe 3 principaux:
            - Le filtrage collaboratif: 2 utilisateurs aiment les mêmes types d'items  
              Recommandation des items que l'un n'a pas exploré à l'autre et vice versa

            - Le filtrage basé sur la similarité des items entre eux    
              Recommandation d'items similaires à un autre exploré par un utilisateur

            - Les systèmes hybrides alliant 'Collaborative filtering' et 'Content-based filtering'
        """)
        st.image('types_reco_syst.png')
    
    
    
    
    choice = st.checkbox('**Dataset**')
    if choice:
        st.header("Choix du dataset")
        st.write("""
        - Dataset de la feuille de projet disponible [ici](https://www.kaggle.com/chelseapower/module4-project)
            - Evènements d'écoutes restreints à l'année 2014 par des utilisateurs ayant publié leurs réactions sur Twitter
                - Difficulté à déterminer l'affinité des utilisateurs pour les chansons écoutées à partir des sentiments associés aux tweets
                - Impossibilité d'obtenir les métadonnées des chansons (titre, artiste, album) 
                - Problème d'interprétabilité des recommandations potentielles
        \n     
                
                    
        - Nous avons donc sélectionner le jeu de données Million Song et l'avons enrichi 
            - Présence d'une variable d'affinité entre les utilisateurs et les morceaux sous forme du nombre d'écoutes par chanson: *Feedback implicite* 
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

