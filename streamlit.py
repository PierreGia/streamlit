import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Fonction pour charger les données et utiliser le cache


def load_data():

    df = pd.read_csv("C:/Users/33761/OneDrive/Bureau/streamlit/Data/test.csv")
    return df


# Charger les données
df = load_data()

# Titre principal
st.title("Analyse des données du Titanic")

# En-têtes et sous-en-têtes
st.header("Exploration des données")
st.subheader("Données des passagers")

# Texte simple et Markdown
st.write("Cette application permet d'explorer le célèbre dataset du Titanic.")
st.markdown(
    "*Données source :* [Kaggle Titanic dataset](https://www.kaggle.com/c/titanic/data)"
)

# Afficher le DataFrame dans l'application
if st.checkbox("Afficher les 5 premières lignes du dataset"):
    st.dataframe(df.head())

# Afficher un tableau statique
if st.checkbox("Afficher un tableau statique des 10 premières lignes"):
    st.table(df.head(10))

# Widgets interactifs


# Champ de saisie de texte pour rechercher un passager
nom_passager = st.text_input("Recherchez un passager par nom:")
if nom_passager:
    st.write(df[df["Name"].str.contains(nom_passager)])

# Sélecteur déroulant pour afficher une colonne spécifique
colonnes = st.selectbox("Sélectionnez une colonne à afficher", df.columns)
st.write(df[[colonnes]].head())

# Curseur pour filtrer par âge
age_min, age_max = st.slider("Sélectionnez une tranche d'âge", 0, 80, (20, 40))
st.write(df[(df["Age"] >= age_min) & (df["Age"] <= age_max)])

# Mise en page avec colonnes
col1, col2 = st.columns(2)
with col1:
    st.write("Classe des passagers")
    st.dataframe(df[["Pclass", "Name"]].head())
with col2:
    st.write("Répartition des sexes")
    st.dataframe(df[["Sex", "Name"]].head())

# Conteneur extensible pour voir les statistiques descriptives
with st.expander("Voir les statistiques descriptives"):
    st.write(df.describe())

# Onglets pour tableau et graphiques
tab1, tab2 = st.tabs(["Tableau", "Graphiques"])
with tab1:
    st.write(df.head())
with tab2:
    # Matplotlib - Histogramme des âges
    fig, ax = plt.subplots()
    df["Age"].hist(bins=20, ax=ax)
    st.pyplot(fig)

    # Seaborn - Boxplot de l'âge selon la classe
    fig, ax = plt.subplots()
    sns.boxplot(x="Pclass", y="Age", data=df, ax=ax)
    st.pyplot(fig)

    # Plotly - Histogramme des tarifs
    fig_plotly = px.histogram(df, x="Fare", nbins=50)
    st.plotly_chart(fig_plotly)


# Caching des données pour accélérer le chargement


def get_filtered_data(pclass):
    return df[df["Pclass"] == pclass]


# Filtrage des données
pclass_selected = st.selectbox("Filtrer par classe", df["Pclass"].unique())
st.write(get_filtered_data(pclass_selected))

# Exemple d'utilisation de st.session_state
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Incrémenter"):
    st.session_state.counter += 1

st.write(f"Compteur : {st.session_state.counter}")


# Callbacks pour déclencher des actions
def on_click():
    st.write("Le bouton a été cliqué!")


st.button("Cliquez-moi", on_click=on_click)

# Gestion des fichiers - Upload de fichier
uploaded_file = st.file_uploader("Choisissez un fichier CSV")
if uploaded_file:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write(df_uploaded)

# Téléchargement de données
csv = df.to_csv().encode("utf-8")
st.download_button(
    "Télécharger les données du Titanic",
    data=csv,
    file_name="titanic_data.csv",
    mime="text/csv",
)
