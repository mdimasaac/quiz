def datatypes():
    import streamlit as st
    import pandas as pd

    df1 = [2,3,5,7,11,13,17,19,23,29]
    df1 = pd.DataFrame(df1, columns = ["Primzahl"])
    c1 = "Number"
    df2 = ["22,5°C","15,8°C","29,2°C","18,6C","26,7°C","10,9°C","30,1°C","23,4°C","17,2°C","20,3°C"]
    df2 = pd.DataFrame(df2, columns = ["Temperatur"])
    c2 = "Text"
    df3 = [22.5,15.8,29.2,18.6,26.7,10.9,30.1,23.4,17.2,20.3]
    df3 = pd.DataFrame(df3, columns = ["Temperatur (in °C)"])
    c3 = "Number"
    df4 = ["$1245.67","$987.45","$356.89","$2200.32","$150.20","$743.91","$512.50","$1856.78","$402.15","$3000.00"]
    df4 = pd.DataFrame(df4, columns = ["Sales"])
    c4 = "Text"
    df5 = [3.3,3.7,3.3,4.0,2.0,1.7,1.7,4.0,2.3,2.7]
    df5 = pd.DataFrame(df5, columns = ["Schulnote"])
    c5 = "Number"
    df6 = ["08/25/2023","11/03/2022","06/18/2021","01/10/2023","04/30/2022","09/15/2021",
    "03/08/2023","12/05/2021","05/28/2023"]
    df6 = pd.DataFrame(df6, columns = ["Order Date"])
    c6 = "Datetime"
    df7 = ["Hamburg","München","Berlin","Köln","Frankfurt","Stuttgart","Düsseldorf","Leipzig","Dresden","Nürnberg"]
    df7 = pd.DataFrame(df7, columns = ["City"])
    c7 = "Text"
    # df8 = [1,0,0,1,1,0,1,1,1,0]
    # df8 = pd.DataFrame(df8, columns = ["Kauf bezahlt"])

    df81 = [1,0,0,1,1,0,1,1,1,0]
    df82 = [0,1,1,0,0,1,0,0,0,1]
    df8 = pd.DataFrame(columns = ["Male","Female"])
    df8["Male"] = df81
    df8["Female"] = df82
    c8 = "Boolean (Ja/Nein)"
    df9 = ["Ali Öztürk","Sophia Nguyen","David Müller","Amina Al-Mansoori",
    "Lukas Patel","Lea Kim","Amir Kowalski","Ebru Garcia","Timo Meier","Aisha Schmidt"]
    df9 = pd.DataFrame(df9, columns = ["Studentenname"])
    c9 = "Text"
    df10 = ["10:15","14:30","08:45","16:20","12:00","18:00","09:40","11:55","13:25","15:10"]
    df10 = pd.DataFrame(df10, columns = ["Uhrzeit"])
    c10 = "Datetime"

    c = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
    check = False
    st.markdown('<div style="text-align: center;"><h1><em>--- Welche Datentypen? ---</em></h1></div>', unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write("1. Sie finden unten unterschiedliche Tabelle aus 1-2 Spalten.")
    st.write("2. Lesen Sie die Spaltenname(n). Identifizieren Sie, mit welchen Datentypen die Values formattiert sind.")
    st.write("3. Machen Sie den Quiz fertig, dann können Sie Ihre Antworten mit der Taste kontrollieren.")
    st.write("4. Achten Sie auf Sonderzeichen. Nicht alle Values mit Zahlen sind als 'Zahlen' formattiert. :)")
    st.write("_____")
    d1,d2,d3,d4,d5 = st.columns(5)
    with d3:
        check = st.checkbox("Check Your Answers")
    types = ["Number","Text","Boolean (Ja/Nein)","Datetime"]
    a01a, a01b,a01c = st.columns([2,1,2])
    with a01a:
        b01a = st.selectbox("Datentyp:", types, key = "01a")
        s01a = st.checkbox("Show Data:", key = "s01a")
        if s01a:
            st.write(df1, wide = True)
        else:
            st.write(df1.head(0))
        if check:
            if b01a == c[0]:
                st.success("Richtig!")
            else:
                st.error("Falsch")
    with a01c:
        b01c = st.selectbox("Datentyp:", types, key = "01c")
        s01c = st.checkbox("Show Data:", key = "s01c")
        if s01c:
            st.write(df2)
        else:
            st.write(df2.head(0))
        if check:
            if b01c == c[1]:
                st.success("Richtig!")
            else:
                st.error("Falsch")
    st.write("_____")
    a02a, a02b,a02c = st.columns([2,1,2])
    with a02a:
        b02a = st.selectbox("Datentyp:", types, key = "02a")
        s02a = st.checkbox("Show Data:", key = "s02a")
        if s02a:
            st.write(df3)
        else:
            st.write(df3.head(0))
        if check:
            if b02a == c[2]:
                st.success("Richtig!")
            else:
                st.error("Falsch")
    with a02c:
        b02c = st.selectbox("Datentyp:", types, key = "02c")
        s02c = st.checkbox("Show Data:", key = "s02c")
        if s02c:
            st.write(df4)
        else:
            st.write(df4.head(0))
        if check:
            if b02c == c[3]:
                st.success("Richtig!")
            else:
                st.error("Falsch")
    st.write("_____")
    a03a, a03b,a03c = st.columns([2,1,2])
    with a03a:
        b03a = st.selectbox("Datentyp:", types, key = "03a")
        s03a = st.checkbox("Show Data:", key = "s03a")
        if s03a:
            st.write(df5)
        else:
            st.write(df5.head(0))
        if check:
            if b03a == c[4]:
                st.success("Richtig!")
            else:
                st.error("Falsch")
    with a03c:
        b03c = st.selectbox("Datentyp:", types, key = "03c")
        s03c = st.checkbox("Show Data:", key = "s03c")
        if s03c:
            st.write(df6)
        else:
            st.write(df6.head(0))
        if check:
            if b03c == c[5]:
                st.success("Richtig!")
            else:
                st.error("Falsch")
    st.write("_____")
    a04a, a04b,a04c = st.columns([2,1,2])
    with a04a:
        b04a = st.selectbox("Datentyp:", types, key = "04a")
        s04a = st.checkbox("Show Data:", key = "s04a")
        if s04a:
            st.write(df7)
        else:
            st.write(df7.head(0))
        if check:
            if b04a == c[6]:
                st.success("Richtig!")
            else:
                st.error("Falsch")
    with a04c:
        b04c = st.selectbox("Datentyp:", types, key = "04c")
        s04c = st.checkbox("Show Data:", key = "s04c")
        if s04c:
            st.write(df8)
        else:
            st.write(df8.head(0))
        if check:
            if b04c == c[7]:
                st.success("Richtig!")
            else:
                st.error("Falsch")
    st.write("_____")
    a05a, a05b,a05c = st.columns([2,1,2])
    with a05a:
        b05a = st.selectbox("Datentyp:", types, key = "05a")
        s05a = st.checkbox("Show Data:", key = "s05a")
        if s05a:
            st.write(df9)
        else:
            st.write(df9.head(0))
        if check:
            if b05a == c[8]:
                st.success("Richtig!")
            else:
                st.error("Falsch")
    with a05c:
        b05c = st.selectbox("Datentyp:", types, key = "05c")
        s05c = st.checkbox("Show Data:", key = "s05c")
        if s05c:
            st.write(df10)
        else:
            st.write(df10.head(0))
        if check:
            if b05c == c[9]:
                st.success("Richtig!")
            else:
                st.error("Falsch")
    st.write("_____")
    


