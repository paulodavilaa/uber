import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('internacionalLimpio2.csv')

st.set_page_config(layout="wide")


st.title('Dashboard Programas Internacionales')
st.text('Paulo Dávila A00825929')
st.text('Este dashboard muestra los hallazgos de la base de datos de programas internacionales:')
st.text('El 16.37 porciento se va de intercambio, el resto se va en otro tipo de programa.')
st.text('El 84.2 porciento es aceptado en su primera opción')
st.text('77,153 alumnos son de profesional y se van de intercambio')
st.text('El rango de promedios de los aplicantes está entre 80 y 90 en este rango hay mayor aceptación')
st.text('Es muy similar la cifra de aplicantes aceptados en el rango de 90 a 100 que el de rechazados de 80 a 90')


plot_col1, plot_col2 = st.columns(2)

plot_col3, plot_col4 = st.columns(2)

plot_col5 = st.columns(2)


with plot_col1:
    st.markdown("### Tipo de Intercambio")
    plot4 = px.pie(df, names='Int_SA', values='TipoIntercambio')
    st.write(plot4)
   
with plot_col2:
    st.markdown("### %Asignados en su Primera Oportunidad")
    plot3 = px.pie(df, values='OpciónAsignada', names='EstatusLimpio')
    st.write(plot3)

with plot_col3:
    st.markdown("### Aplicantes por nivel")
    plot2 = px.histogram(df, x="Nivel")
    st.write(plot2)

with plot_col4:
    st.markdown("### Diagrama Primera Opción - Estatus - Rango")
    plot4 = px.parallel_categories(df, dimensions=['RangoPromedios', 'EstatusLimpio', 'TipoIntercambio'],
                color="TipoIntercambio", color_continuous_scale=px.colors.diverging.Tealrose,
                labels={'RangoPromedios':'Rango de Promedios', 'EstatusLimpio':'Estatus', 'TipoIntercambio':'Intercambio "1" o Study Abroad "0"'})
    st.write(plot4)

with plot_col4:
    st.markdown("### Rango Promedios - Estatus")
    plot4 = px.density_heatmap(df, x="RangoPromedios", y="EstatusLimpio")
    st.write(plot4)