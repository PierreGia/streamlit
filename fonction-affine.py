import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre principal
st.title("Graphique d'une fonction affine y = ax + b")

# Sliders pour a et b
a = st.slider("Choisir la valeur de (a)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
b = st.slider("Choisir la valeur de (b)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# Géner les valeurs x dans l'intervalle [-10, 10]
x = np.linspace(-10, 10, 400)

# Calcul des valeurs y correspondantes avec la formule y = ax + b
y = a * x + b

# Création de la figure avec Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {a}x + {b}")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.grid(True)
ax.legend()

# Affichage du graphique dans Streamlit
st.pyplot(fig)

# Affichage des valeurs de a et b
st.write(f"La fonction affine est y = {a}x + {b}")
