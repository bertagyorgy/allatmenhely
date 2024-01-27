import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Állat menhely",
    page_icon='🍆',
)

def main():
    st.title("Streamlit Forms & Animal Shelter")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")

        with st.form(key='forml'):
            nev = st.text_input("Állat neve")
            chipszam = st.text_input("Chipszám")
            ivar = st.selectbox("Ivar", ["Hím", "Nőstény"])
            if ivar == "Nőstény":
                fajta = st.text_input("Fajta")
            else:
                fajta = st.text_input("Fajta vagy keverék típus")
            egeszsegi_allapot = st.text_input("Egészségi állapot")
            fogazat = st.text_input("Fogazat")
            kor = st.number_input("Kor", min_value=0, max_value=100)
            viselkedes = st.text_area("Viselkedés")
            egyeb_jellemzok = st.text_area("Egyéb jellemzők")

            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                # Adatok tárolása az SQLite adatbázisban
                conn = sqlite3.connect("allat_menhely.db")
                c = conn.cursor()

                c.execute('''CREATE TABLE IF NOT EXISTS allatok 
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT,
                              chipszam TEXT,
                              ivar TEXT,
                              fajta TEXT,
                              egeszsegi_allapot TEXT,
                              fogazat TEXT,
                              kor INTEGER,
                              viselkedes TEXT,
                              egyeb_jellemzok TEXT)''')

                c.execute("INSERT INTO allatok (nev, chipszam, ivar, fajta, egeszsegi_allapot, fogazat, kor, viselkedes, egyeb_jellemzok) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          (nev, chipszam, ivar, fajta, egeszsegi_allapot, fogazat, kor, viselkedes, egyeb_jellemzok))

                conn.commit()
                conn.close()
                st.success("Adatok sikeresen hozzáadva az adatbázishoz")

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()