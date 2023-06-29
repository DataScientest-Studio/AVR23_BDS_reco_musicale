import pandas as pd
import streamlit as st
import os
from pathlib import Path

CUR_DIR = os.path.abspath('')
DECO_DIR = str(Path(CUR_DIR) / "decoration") + "\\"

# Titre de l'application
#st.title("RECOMMANDATION MUSICALE")

# Barre latérale avec le sommaire
st.sidebar.title("Sommaire")
pages = ["Introduction", "Les Données", "Prétraitement des données", "Exploration", "Modèle de recommandation", "Evaluation et résultats"]
page = st.sidebar.radio("Aller vers", pages)

if page == pages[0]:
    st.header("Introduction")
    #st.write(DECO_DIR)
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
        
        st.image("decoration/syst_reco_mus.png")
        

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
        st.image("decoration/types_reco_syst.png")
    
    
    
    
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
    
    st.image("decoration/Data Sci.png")

elif page == pages[1]:
    st.header("Les données utilisées pour le projet")
    
    st.text("\n")
    st.text("\n")
    

    st.image("decoration/acoustic_db.png", width = 400)
    
    st.text("\n")

    st.write("""
    Afin de construire un système de recommandations musicales, nous avons  
    recomposé un jeu de données à partir de 3 sources dont 2 d'entre elles
    appartiennent au jeu de données Million Song [http://millionsongdataset.com/](http://millionsongdataset.com/)  


    - Le premier fichier [train_triplets.txt](millionsongdataset.com/sites/default/files/challenge/train_triplets.txt.zip) contient des identifiants d'utilisateurs anonymisés  
      ainsi que les identifiant des chansons et le nombre d'écoute par chanson pour chacun des utilisateurs

    
    - Le deuxième fichier [track_metadata.db](labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/track_metadata.db) correspond à une base de métadonnées
      permettant notamment de relier les identifiants des chansons à leurs noms et artistes  


    - Le dernier fichier [tracks_features.csv](https://www.kaggle.com/rodolfofigueroa/spotify-12m-songs) est un jeu de données 
      recensant les caractéristiques acoustiques de plus d'1,2 million de chansons parmi lesquelles se trouvent des métriques mesurant le caractère danseant des chansons,
      leur tempo, caractère acoustique, propension à être jouées en live, le degré de paroles qu'elles contiennent, leur intensité sonore ou bien encore leur valence 
      (note entre 0 et 1 associée à la positivité que véhicule le son)        


    """)
    st.text("\n")
    st.text("\n")

    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        Le jeu de données que nous avons recomposé  
        est disponible sous forme partitionnée   
        sur notre dépot GitHub [https://github.com/DataScientest-Studio/AVR23_BDS_reco_musicale/tree/main/data](https://github.com/DataScientest-Studio/AVR23_BDS_reco_musicale/tree/main/data)')
        """)
        
    with col2:
        st.image("decoration/acoustic.png", width=200)
        
    

elif page == pages[2]:
    st.header("Prétraitement des données")
    st.text("\n")
    st.text("\n")

        
    col1, col2 = st.columns(2)
    with col1:
        st.image("prettt/table_join.png")
    with col2:
        st.write("""
        - Informations contenant le comportement de consommation des utilisateurs et caractéristiques acoustiques des sons dans dans 2 tables distinctes:
          *triplet* et *track_features* 
        """)
        st.text("\n")
        st.write("""
        - Pas de variable commune permettant de joindre directement ces deux tables  
        Jointure en 2 temps: grâce à la table *track_metadata* qui identifie les "tracks" par une variable commune avec la table *triplet*  
        Obtention des titres et artistes permettant d'obtenir les caractéristiques acoustiques (table *tracks_features*)
        """)
    
        st.write("""
        - Cependant, il existe de nombreuses reprises d'un son par différents artistes.
        La jointure avec la table *track_features* se fait donc sur les noms de chansons ET d'artistes correspondants communs aux 2 jeux de données    
        """)

    st.write("""
    - Table résultante: titres et artistes correspondants des sons, nombre d'écoutes et caractéristiques acoustiques de chaque son pour tous les utilisateurs.
    - Plusieurs interprétations d'un même son par un même artiste existent. La fusion éffectuée ne permet pas d'identifier la version d'un son écouté par l'utilisateur  
    Pour chaque artiste, une seule version d'un son est donc conservée (aucun duplicat n'est plus légitime qu'un autre).
    - Tableau: 4,973,744 entrées, 849,209 utilisateurs et 27,607 sons différents 
    """)

    st.text("\n")

    st.write("""
    - Les caractéristiques acoustiques des sons sont ensuite **normalisées** selon une distribution normale standard
    """)    
    

elif page == pages[3]:
    st.header("Visualisations")
    st.text("\n")
    st.text("\n")

    features = st.checkbox('**Caractéristiques Musicales**')
    if features:
        display = ["", 'Distribution', 'Corrélations', ] #caption
        selected_display = st.selectbox("Sélectionnez un affichage", display)    
        if selected_display == display[1]:
            st.image("Data_viz/audio_features_distribution.jpg", caption= "Distribution des caractéristiques acoustiques normalisées")
            st.write("""
            - Variables *speechiness*, *acousticness*, *instumentalness* et *liveness*: distributions asymmétriques
              - Majorité des sons: pas de paroles, pas d'intruments acoustiques, non enregistrés en live

            - Variable danceability: distribution suivant une loi normale  
            - Majorité des sons: forte valeur de la variable *energy*
            """)
        elif selected_display == display[2]:
            st.image("Data_viz/audio_features_corr_tracks.jpg", width = 500, caption= "Heatmap des corrélations entre caractéristiques acoustiques")
            st.write("""
            - Valeurs absolues de corrélations faibles
            - Les seules présentant une valeur absolue de corrélation > 0.7 sont 
                - *acousticness* et *energy*, *loudness* et *energy* 
            """)
    st.text("\n")

    interaction = st.checkbox('**Intéractions items/utilisateurs**')
    if interaction:
        st.image("Data_viz/items_users_interactions.png", width = 1000)
        st.text("\n")
        st.write("""
        - Les nombres de sons, d'écoutes et d'artistes par utilisateur présentent des distributions très asymétriques
        - Echelle logarithmique pour visualiser l'allongement de la queue droite vers les valeurs élevées
        - En terme pratique: un quart des utilisateurs 
        """)

else:
    pass

