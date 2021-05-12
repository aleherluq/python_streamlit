import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price 

Muestra los valores del precio y del volumen del stock de Google
""")

#se define el ticker symbol
tickerSymbol = 'GOOGL'

#Obtener los datos de este ticker
tickerData = yf.Ticker(tickerSymbol)

#Obtener el histórico para el ticker -- El ticker es como el simbolo de la empresa para buscarlo en la bolsa
tickerDf = tickerData.history(period="id", start='2010-05-31', end='2020-05-31')

# los datos que devuelve son Open High Low Close Volume Dividends Stock Splits
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
