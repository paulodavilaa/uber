import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('internacionalLimpio1.csv')

st.set_page_config(layout="wide")


st.title('Dashboard Programas Internacionales')
st.text('Paulo Dávila A00825929')
st.text('Este dashboard muestra los hallazgos de la base de datos de programas internacionales')


plot_col1, plot_col2 = st.columns(2)

plot_col3, plot_col4 = st.columns(2)

plot_col5 = st.columns(2)


with plot_col1:
    st.markdown("### Tipo de Intercambio")
    plot4 = px.pie(df, names='Int_SA', values='TipoIntercambio')
    st.write(plot4)
   
with plot_col2:
    st.markdown("### %Asignados y %Rechazados")
    plot3 = px.pie(df, values='OpciónAsignada', names='EstatusLimpio')
    st.write(plot3)

with plot_col3:
    st.markdown("### Aplicantes por nivel")
    plot2 = px.histogram(df, x="Nivel")
    st.write(plot2)

with plot_col4:
    st.markdown("### Rango Promedios - Estatus")
    plot4 = px.density_heatmap(df, x="RangoPromedios", y="EstatusLimpio")
    st.write(plot4)

with plot_col5:
    st.markdown("### Diagrama Primera Opción - Estatus - Rango")
    plot5 = px.parallel_categories(df, dimensions=['PrimeraOpción', 'EstatusLimpio', 'RangoPromedios'],
                color="EstatusLimpio", color_continuous_scale=px.colors.diverging.Tealrose,
                labels={'PrimeraOpción':'Primera Opción', 'EstatusLimpio':'Estatus', 'RangoPromedios':'Rango de Promedios'})
    st.write(plot5)






df = pd.read_csv('internacionalLimpio1.csv')

st.title('Dashboard Programas Internacionales')
st.text('Paulo Dávila A00825929')
st.text('Este dashboard muestra los hallazgos de la base de datos de programas internacionales')

plot_col1, plot_col2 = st.columns(2)

plot_col3, plot_col4 = st.columns(2)

plot_col5 = st.columns(2)


with plot_col1:
    st.markdown("### Tipo de Intercambio")
    plot4 = px.pie(df, names='Int_SA', values='TipoIntercambio')
    st.write(plot4)
   
with plot_col2:
    st.markdown("### %Asignados y %Rechazados")
    plot3 = px.pie(df, values='OpciónAsignada', names='EstatusLimpio')
    st.write(plot3)

with plot_col3:
    st.markdown("### Aplicantes por nivel")
    plot2 = px.histogram(df, x="Nivel")
    st.write(plot2)

with plot_col4:
    st.markdown("### Rango Promedios - Estatus")
    plot4 = px.density_heatmap(df, x="RangoPromedios", y="EstatusLimpio")
    st.write(plot4)

with plot_col5:
    st.markdown("### Diagrama Primera Opción - Estatus - Rango")
    plot5 = px.parallel_categories(df, dimensions=['PrimeraOpción', 'EstatusLimpio', 'RangoPromedios'],
                color="EstatusLimpio", color_continuous_scale=px.colors.diverging.Tealrose,
                labels={'PrimeraOpción':'Primera Opción', 'EstatusLimpio':'Estatus', 'RangoPromedios':'Rango de Promedios'})
    st.write(plot5)









df = pd.read_csv('internacionalLimpio1.csv')

st.title('Dashboard Programas Internacionales')
st.text('Paulo Dávila A00825929')
st.text('Este dashboard muestra los hallazgos de la base de datos de programas internacionales')

st.sidebar.title('Navegación')

plot_col1, plot_col2 = st.columns(2)

plot_col3, plot_col4 = st.columns(2)

plot_col5 = st.columns(2)

def plot_col1(df):
    st.markdown("### Tipo de Intercambio")
    plot1 = px.pie(df, names='Int_SA', values='TipoIntercambio')
    st.write(plot1)

def plot_col2(df):
    st.markdown("### %Asignados y %Rechazados")
    plot2 = px.pie(df, values='OpciónAsignada', names='EstatusLimpio')
    st.write(plot2)

def plot_col3(df):
    st.markdown("### Aplicantes por nivel")
    plot3 = px.histogram(df, x="Nivel")
    st.write(plot3)

def plot_col4(df):
    st.markdown("### Rango Promedios - Estatus")
    plot4 = px.density_heatmap(df, x="RangoPromedios", y="EstatusLimpio")
    st.write(plot4)


def plot_col5(df):
    st.markdown("### Diagrama Primera Opción - Estatus - Rango")
    plot5 = px.parallel_categories(df, dimensions=['PrimeraOpción', 'EstatusLimpio', 'RangoPromedios'],
                color="EstatusLimpio", color_continuous_scale=px.colors.diverging.Tealrose,
                labels={'PrimeraOpción':'Primera Opción', 'EstatusLimpio':'Estatus', 'RangoPromedios':'Rango de Promedios'})
    st.write(plot5)


opciones = st.radio('Páginas', 
opciones = ['Tipo de Intercambio','%Asignados y %Rechazados','Aplicantes por nivel','Rango Promedios - Estatus','Tipo de Intercambio','Diagrama Primera Opción - Estatus - Rango'])

if opciones == 'TipoIntercambio':
    plot_col1(df)
elif opciones == '%Asignados y %Rechazados':
    plot_col2(df)
elif opciones == 'Aplicantes por nivel':
    plot_col3(df)
elif opciones == 'Rango Promedios - Estatus':
    plot_col4(df)
elif opciones == 'Diagrama Primera Opción - Estatus - Rango':
    plot_col5(df)