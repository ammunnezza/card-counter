import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("🔢 Contatore Persistente")

# Connessione al foglio (i parametri vanno nei 'Secrets' di Streamlit)
conn = st.connection("gsheets", type=GSheetsConnection)

# 1. Leggi i dati attuali
df = conn.read(worksheet="Foglio1")
current_value = int(df.loc[df['nome_contatore'] == 'generale', 'valore'].values[0])

st.metric("Conteggio Attuale", current_value)

# 2. Pulsanti per modificare
col1, col2 = st.columns(2)

if col1.button("➕ Incrementa"):
    new_value = current_value + 1
    # Aggiorna il DataFrame e salva sul foglio
    df.loc[df['nome_contatore'] == 'generale', 'valore'] = new_value
    conn.update(worksheet="Foglio1", data=df)
    st.rerun()

if col2.button("🔄 Reset"):
    df.loc[df['nome_contatore'] == 'generale', 'valore'] = 0
    conn.update(worksheet="Foglio1", data=df)
    st.rerun()
