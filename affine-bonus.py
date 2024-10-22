import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Etape 1: Générer une droite affine y = ax + b avec des points aléatoires
st.title("Courbe affine avec points aléatoires et calcul du MSE")

# Sliders pour choisir a et b
a = st.slider("Choisir la pente (a)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
b = st.slider("Choisir l'ordonnée à l'origine (b)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1,)

# Génération des valeurs x dans l'intervalle [-10, 10]
x = np.linspace(-10, 10, 400)

# Droite affine y = ax + b
y = a * x + b

# Générer des points aléatoires ayant la même longueur que la droite affine
points_aleatoires = y + np.random.randn(len(x))  # ajouter un bruit aléatoire

# Création de la figure avec Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y, label=f"Droite affine y = {a}x + {b}", color="blue")
ax.scatter(x, points_aleatoires, color="red", label="Points aléatoires", marker="o")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.legend()

# Afficher le graphique dans Streamlit
st.pyplot(fig)

# Etape 2: Calcul de l'erreur quadratique moyenne (MSE)
mse = np.mean((y - points_aleatoires) ** 2)
st.write(
    f"Erreur quadratique moyenne (MSE) entre la droite affine et les points aléatoires : {mse}"
)

# Stocker a et mse dans une liste pour les afficher
mse_values = []
a_values = []

# Parcourir différentes valeurs de a pour observer le MSE
for a_iter in np.linspace(-10, 10, 100):  # Variation de a
    y_iter = a_iter * x + b
    mse_iter = np.mean((y_iter - points_aleatoires) ** 2)
    mse_values.append(mse_iter)
    a_values.append(a_iter)

# Etape 3: Afficher le graphique de MSE en fonction de a
fig2, ax2 = plt.subplots()
ax2.plot(a_values, mse_values, label="MSE en fonction de a", color="blue")
ax2.set_xlabel("a (pente)")
ax2.set_ylabel("MSE (Erreur quadratique moyenne)")
ax2.grid(True)
ax2.legend()

# Afficher le graphique de MSE dans Streamlit
st.pyplot(fig2)