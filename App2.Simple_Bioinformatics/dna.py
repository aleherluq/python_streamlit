import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image



image = Image.open('dna-logo.jpg')
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count App

Esta app calcula los nucleotidos de una secuencia de ADN:

***
""")

#Inut text box

st.header('Introduce la secuencia de ADN')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input ", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]  # Para evitar el nombre de la secuencia
sequence = ''.join(sequence) # concatena la lista en un string

st.write("""
***
""")

# Muestra la cadena de ADN que se ha elegido

st.header('INPUT (DNA Query)')
sequence

# Cuenta de los nucleotidos del ADN
st.header('OUTPUT  (Cuenta de los nucleotidos del ADN)')

#1 muestra el diccionario
st.subheader('1. Print dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')), 
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
        ])
    return d
X = DNA_nucleotide_count(sequence)
X

### 2. Mostrar el texto
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

#3. Muestra el dataframe

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)


### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)

st.write(p)