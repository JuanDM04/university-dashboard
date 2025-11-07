import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="University Analytics Dashboard", layout="wide")
st.title(" University Student Analytics Dashboard")

# --- Cargar datos ---
df = pd.read_csv("university_student_data.csv")

# Calcular tasa de retención si no existe
if 'Retention Rate (%)' not in df.columns:
    df['Retention Rate (%)'] = (df['Retained'] / df['Enrolled']) * 100

# --- Filtros interactivos ---
st.sidebar.header("Filtros")
years = st.sidebar.multiselect("Seleccionar Año(s):", options=sorted(df['Year'].unique()), default=sorted(df['Year'].unique()))
terms = st.sidebar.multiselect("Seleccionar Periodo(s):", options=df['Term'].unique(), default=df['Term'].unique())

# Filtrar datos
filtered = df[(df['Year'].isin(years)) & (df['Term'].isin(terms))]

# --- Visualización 1: Retención en el tiempo ---
st.subheader("Retention Rate Over Time")
fig1, ax1 = plt.subplots()
sns.lineplot(data=filtered.groupby('Year')['Retention Rate (%)'].mean().reset_index(),
             x='Year', y='Retention Rate (%)', marker='o', ax=ax1)
ax1.set_ylabel("Retention Rate (%)")
st.pyplot(fig1)

# --- Visualización 2: Satisfacción por año ---
st.subheader("Student Satisfaction by Year")
fig2, ax2 = plt.subplots()
sns.barplot(data=filtered.groupby('Year')['Student Satisfaction (%)'].mean().reset_index(),
            x='Year', y='Student Satisfaction (%)', ax=ax2)
ax2.set_ylabel("Satisfaction (%)")
st.pyplot(fig2)

# --- Visualización 3: Comparación entre términos ---
st.subheader("Comparison Between Spring and Fall Terms")
fig3, ax3 = plt.subplots()
sns.barplot(data=filtered.groupby('Term')[['Enrolled', 'Retention Rate (%)', 'Student Satisfaction (%)']].mean().reset_index(),
            x='Term', y='Enrolled', ax=ax3)
ax3.set_ylabel("Average Values")
st.pyplot(fig3)

st.markdown("---")
st.markdown("**Dashboard desarrollado por JUAN DUQUE, EDGARDO OLIVARES, JORGE PEREZ, JUAN OCHOA – Universidad de la Costa (2025)**")



