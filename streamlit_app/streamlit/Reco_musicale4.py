import pandas as pd
import streamlit as st
import os
from pathlib import Path

CUR_DIR = os.path.abspath('')
DECO_DIR = str(Path(CUR_DIR) / "decoration") + "\\"
import streamlit.components.v1 as components

# Titre de l'application
#st.title("RECOMMANDATION MUSICALE")

# Barre latérale avec le sommaire
st.sidebar.title("Sommaire")
pages = ["Introduction", "Les Données", "Prétraitement des données", "Exploration", "Modèles de recommandation", "Evaluation et résultats"]
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
        - En terme pratique: un quart des utilisateurs ont écouté moins de 2 pistes différentes et cumulent moins de 2 écoutes
        - La plupart des utilisateurs écoutent des pistes interprétées par un seul ou peu d'artistes différents
        """)

elif page == pages[4]:
    st.header('Modèles de recommandations')
    st.text("\n")
    st.text("\n")
    st.write("""
    - **Objectif** : développer un système de recommandation de titres à un utilisateur en fonction de ses goûts musicaux.
    - **Variable réponse** : affinité d'un utilisateur pour un titre (estimé par le fait qu'il ait ou non écouté le titre : variable unaire).
    - **Formulation de la problématique** : *top-k recommendation problem*
    - **Type d'algorithmes développés** : *Content-based ranking*
    """)
    
    avg_b_ranking = st.checkbox('**Average-based ranking algorithm**')
    if avg_b_ranking:
        principle1 = st.checkbox('Principe', key = 'princip1')
        if principle1:
            st.image("algo_principle/averaging_based_good_example.png", width = 900)
            st.text("\n")
            st.write("""
                     - Moyenne pondérée par nombre d'écoute des caractéristiques acoustiques des titres de la playlist : centroïde représentatif des goûts musicaux de l'utilisateur.
                     - Définition d'un rang à chaque titre en fonction de sa distance au centroïde.
                     - Proposition des  premiers titres.
                    """)
                    
        limit1 = st.checkbox('Limites', key = 'limit1')
        if limit1:
            st.image("algo_principle/averaging_based_bad_example.png", width = 900)
            st.text("\n")
            st.write("""
                     Algorithme peu adapté pour des utilisateurs :
                         
                    - avec des goûts musicaux très dispersés
                    - avec des gouts musicaux polarisés (plusieurs genres musicaux appréciés)
                     """)
        
    kmeans_b_ranking = st.checkbox('**Kmeans-based ranking algorithm**')
    if kmeans_b_ranking:
        principle2 = st.checkbox('Principe', key = 'princip2')
        if principle2:
            st.image("algo_principle/kmeans_based_example.png", width = 900)
            st.text("\n")
            st.write("""
                     - Clustering des titres de la playlist de l'utilisateur par Kmeans : centroides représentant les K (sous)-genres musicaux appréciés par l'utilisateur
                     - Définition de K rangs pour chaque titres en fonctions de leurs distances aux centroides.
                     - Sélection du rang le plus faible pour chacun des titres.
                     - Proposition des k premiers titres.
                     """)
        limit2 = st.checkbox('Limites', key = 'limit2')
        if limit2:
            st.text("\n")
            st.write("""
                     - Algorithme peu adapté pour des utilisateurs avec des goûts musicaux très dispersés.
                     - Ne tiens compte que des caractéristiques acoustiques (quantitatives) des titres pour déterminer les goûts d'un utilisateur.
             """)
    artist_filter = st.checkbox('**Filtrage par artiste**')
    if artist_filter:
        st.image("algo_principle/artist_filtering.png", width = 900)
        st.text("\n")
        st.write("""
            **Principe**
            - Classement des artistes par nombre de titres dans la playlist de l'utilisateur.
            - Modification des rangs des titres en forçant ceux des artistes les plus écoutés à occuper les premières places du classement, l'ordre des titres d'un même artiste dépendant de leur rang pré-filtrage.
            
            **Limites**
            - Peu de sérendipité (effet "bulle de filtre").
        """)
    st.write("## Exemples d'applications")
    st.text("\n")
    users  = ['22e08d5e101ab5b86dc394856d508e175a5242a6',
              '72b7c0b7ef846805b61e7a82534beded246a95c2',
              'b393acb0d2f15b13fb1377c2998b222f6e174619',
              'b784fec0b1e04dbf02a2f095da6ec1e3a8561391',
              'af3ee32357049dd96231238bd1b019e8142ee6aa', # l'espagnol
              '3fa44653315697f42410a30cb766a4eb102080bb',
              "ec6dfcf19485cb011e0b22637075037aae34cf26",
              '6a46aee45cc177cf8e2025e59d21c7939902deee',
              '716ed1ec67d67bfa05db3ffeb641d13f46dca6ec',
              'd035c4a2b179ef8c756d73f9f3018ec7a87d8594']
    lims = [10,
            5,
            5,
            4,
            3,
            3,
            7,
            4,
            3,
            3
            ]

    
    
    sel_user = st.selectbox("Sélectionnez un utilisateur", users)
    lim = [*range(1, lims[users.index(str(sel_user))]+1)]
    
    avg_profile = st.checkbox("**Average based ranking algorithm**")
    if avg_profile:
        polar = st.checkbox("**Polar plot du profile moyen**")
        if polar:
            html_file = open("users_viz/" + str(sel_user) + "_avg_profile.html", 'r', encoding = 'utf-8')
            source_code = html_file.read()
            components.html(source_code, height = 1700, width=2000)
        result = st.checkbox("**Détection des titres de la playlist de l'utilisateur par proposition des 5 voisins les plus proches**")
        if result:
            st.image("users_viz/" + str(sel_user) + "_avg_profile_df.png")

    centroid_profiles = st.checkbox("**K-means based ranking algorithm**")
    if centroid_profiles:
        scores = st.checkbox("**Nombre de clusters du profile acoustique de cet utilisateur**")
        if scores:
            st.image("users_viz/" + str(sel_user) + "_silhouette_scores.png")
        polar_centroids = st.checkbox("**Polar plots des sous profiles acoustiques de l'utilisateur**")
        if polar_centroids:
            target_centroid = st.selectbox("Centroïde N°", lim)
            html_file = open("users_viz/" + str(sel_user) + f"_centroid_{str(target_centroid)}_profile .html", 'r', encoding = 'utf-8')
            source_code = html_file.read()
            components.html(source_code, height = 1700, width=2100)    
        result = st.checkbox("**Détection des titres de la playlist de l'utilisateur par proposition des 5 voisins les plus proches de chaque centroide**")
        if result:
            st.image("users_viz/" + str(sel_user) + "_centroids_profiles_df.png")


elif page == pages[5]:
    st.header("Evaluation des algorithmes")
    st.text("\n")
    st.text("\n")
    methodo = st.checkbox('**Methodologie**')
    if methodo:
        st.markdown("""
            - Sélection d'une sous-population d'utilisateur en fonction 
                - Du nombre de titres différents dans leur playlist
                - Du nombre d'écoutes cumulées dans leur playlist
            - Tirage aléatoire d'un échatillon dans cette sous-population
            - Séparation aléatoire de la playlist de chaque user selon le facteur $p$ :
                - Une proportion $p$ des titres de la playlist de l'utilisateur sera cachée à l'algorithme
                - La proporiton $1-p$ des titres restant sert à définir les goûts des utilisateur
            - Définition des rangs des morceaux n'appartenant pas à la playlist apparente par l'algorithme de ranking.
            - Calcul en fonction de $k$, le nombre de titres proposés à l'utilisateur\* :
                - $TPR(k)$ : la proportion de titre de la playlist cachée qui sont proposés à l'utilisateur
                - $FPR(k)$ : la proporition de titres n'appartenant pas à la playlist cachée proposés à l'utilisateur
            - **Evaluation** :
                - Calcul de la courbe ROC curve et de l'AUC à partir de $TPR(k)$ et $FPR(k)$
                - Comparaison d'AUC entre algorithme et avec les rangs attribués aléatoirement
            \n
            \n
            \*Section 7.5.4 *Evaluating Ranking via Reciever Operating Characteristic*, *Recommenders System*, Aggarwal (2016)
        """)
        st.image("evaluation/workflow.png", width = 500)
    results = st.checkbox('**Resultats**')
    if results:
        st.markdown("""
            - Sous-groupes :
                - Sous Groupe 1 (SG1) : 200 utilisateurs tirés aléatoirement parmis ceux ayant écouté entre 5 et 25 titres différentes
                - SG2 : 200 utilisateurs tirés aléatoirement parmis ceux ayant écouté entre 26 et 50 titres différentes
                - SG3 : 200 utilisateurs tirés aléatoirement parmis ceux ayant écouté entre 51 et 75 titres différentes
                - SG4 : 200 utilisateurs tirés aléatoirement parmis ceux ayant écouté entre 76 et 100 titres différentes
                - SG5 : les 176 utilisateurs ayant écouté plus de 100 titres différentes
            - Proportion de la playlist cachée : $p=0.20$
        """)
        
        display = ["Echantillon complet", 'SG1', 'SG2', 'SG3', 'SG4', 'SG5']
        selected_display = st.selectbox("Sélectionnez un échantillon", display)
        
        if selected_display == display[0]:
            st.image("evaluation/ROC_5_inf.jpg", caption= "ROC Curve : échantillon complet")
            
        elif selected_display == display[1]:
            st.image("evaluation/ROC_5_25.jpg", caption= "ROC Curve : SG1")
            
        elif selected_display == display[2]:
            st.image("evaluation/ROC_26_50.jpg", caption= "ROC Curve : SG2")
            
        elif selected_display == display[3]:
            st.image("evaluation/ROC_51_75.jpg", caption= "ROC Curve : SG3")
            
        elif selected_display == display[4]:
            st.image("evaluation/ROC_76_100.jpg", caption= "ROC Curve : SG4")
            
        elif selected_display == display[5]:
            st.image("evaluation/ROC_101_inf.jpg", caption= "ROC Curve : SG5")
        st.write("""
            Notes:
            - Random reco. : Recommandations après attribution de rang aléatoire
            - Avg-b reco. : Recommandations après attribution de rang par *Average-based ranking*
            - Km-b reco. : Recommandations après attribution de rang par *Kmeans-based ranking*
            - \{nom-de-l-algo\}-af reco. : Recommandations après filtrage des rangs sur les artistes.
            
        """)
        
    conclusion =  st.checkbox('**Conclusion**')
    if conclusion:
        st.write("""
            **Discussion** :
            - Tous les algorithmes sont meilleurs que la recommandation aléatoire
            - *Kmeans-based ranking* > *Average-based ranking*
            - *Filtrage par les artistes* > *Sans filtrage*
            - Meilleurs perfomances de l'agorithme Kmeans-based ranking + filtrage par artiste : Importance de tenir compte de la diversité des goûts musicaux de l'utilisateur et de plusieurs sources d'informations concernant les titres de sa playlist.
            - Attention aux mesures de performances 'pures' : Peu de sérendipité et effet bulle.
            
            **Limites** :
            - Jeu de données : vieux (2011), pas d'information spatiale ou temporelle
            - Séparation de la playlist des utilisateurs sans tenir compte de l'ordre d'écoute
            - Les titres n'ayant été écouté par aucun utilisateur n'ont pas été intégré dans les propositions possibles
            
            **Perspectives** :
            - Développer d'autres filtres: langue, thème, artistes *similaires* 
            - Evaluation des performances sur plus d'échantillons
            - Comparer les performances à un algorithme de *Collaborative-filtering*
            - Développer un algorithme de recommandation hybride intégrant de mulitples sources d'informations
            
            Notes : La méthodo pour évaluer les algorithmes a été développé grâce au livre *Recommenders Systems* d'Aggarwal (500 pages).
            
        """)
else:
    pass

