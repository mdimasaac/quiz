def vis_q():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objs as go
    st.markdown('<div style="text-align: center;"><h1><em>--- Datenvisualisation ---</em></h1></div>', unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write("Übungsaufgaben:")
    st.write("1. Sie haben verschiedene Datentypen und Datenskalen kennengelernt.")
    st.write("2. Machen Sie sinnvolle Visualisation für folgende Variablen.")
    st.write("3. Achten Sie auf die Achsen. Nominale, ordinale und andere diskrete Variablen stehen normalerweise auf x-Achse.")
    st.write("4. Verhältnis- und andere kontinuierliche Variablen werden oft an der y-Achse beschrieben.")
    st.write("5. Falls Sie Error-Message bekommen, versuchen Sie, die Werte an den Achsen zu ändern.")
    st.write("6. Falls das Diagramm nicht richtig angezeigt wird, aktivieren Sie die Taste 'Group by this Axis'.")

    st.write(" ")
    st.write(" ")
    st.write("A1) Öffnen Sie den Covid-Datensatz (covid.csv)")
    st.write("A2) Zeigen Sie Num. of Case per Country")
    st.write("A3) Zeigen Sie Num. of Case over time (date)")
    st.write("A4) Zeigen Sie Num. of Case over time (month)")
    st.write("A5) Zeigen Sie Num. of Case over time (year)")
    st.write(" ")
    st.write(" ")
    st.write("B1) Öffnen Sie den Superstore-Datensatz (superstore.csv)")
    st.write("B2) Zeigen Sie Num. of Case per Country")
    st.write("B3) Zeigen Sie Num. of Case over time (date)")
    st.write("B4) Zeigen Sie Num. of Case over time (month)")
    st.write("B5) Zeigen Sie Num. of Case over time (year)")

    st.write("_____")
    files = ["covid.csv","superstore.csv","auto_mpg.csv","netflix_titles.csv"]
    openfiles = st.selectbox("Select file to open:", files)
    df = pd.DataFrame()
    if openfiles == files[0]:
        df = pd.read_csv("covid.csv")
        df["dateRep"] = pd.to_datetime(df["dateRep"])

    elif openfiles == files[1]:
        df = pd.read_csv("superstore.csv")
        df = df.iloc[:200]
    elif openfiles == files[2]:
        df = pd.read_csv("auto_mpg.csv")
        df = df.iloc[:200]
    elif openfiles == files[3]:
        df = pd.read_csv("netflix_titles.csv")
    # df = df.iloc[:200]
    cols = df.columns.tolist()
    style = ["Bar","Scatter","Line"]
    st.write("_____")
    c1,c2,c3 = st.columns([1,4,1])
    data = []
    with c2:
        colx = st.selectbox("Select Value for x-Axis:", cols)
        x = df[colx].values.tolist()
        pivot = st.radio("Group by this axis", ["sum","count","do not group"])
        if pivot == "sum":
            grouped = df.groupby(colx).sum()
            st.write("aggfunc: [sum]")
            grouped = grouped.sort_index()
            x = grouped.index.tolist()
        elif pivot == "count":
            grouped = df.groupby(colx).count()
            st.write("aggfunc: [count]")
            grouped = grouped.sort_index()
            x = grouped.index.tolist()
        else:
            x = df[colx].values.tolist()
        st.write("_____")
        colya = st.selectbox("Select Value for y-Axis (graph A):", cols)
        typea = st.selectbox("Select Plot Style (graph A)", style)
        if pivot == "sum" or pivot == "count":
            ya = grouped[colya].values.tolist()
        else:
            ya = df[colya].values.tolist()
        if typea == "Bar":
            trace1 = go.Bar(
            x = x,
            y = ya,
            width = .5,
            textposition='outside',name = colya
            )
        elif typea == "Scatter":
            trace1 = go.Scatter(
            x = x,
            y = ya,
            mode = "markers",name = colya
            )
        elif typea == "Line":
            trace1 = go.Scatter(
            x = x,
            y = ya,
            mode = "lines",name = colya
            )
        try:
            data.append(trace1)
            fig = go.Figure(data = data)
            fig.update_layout(template="plotly_dark",
            autosize=True, height = 600
            )
            st.plotly_chart(fig, use_container_width=True)
        except:
            datanull = []
            st.error("Etwas ist schief gelaufen. Versuchen Sie, die Werte an den Achsen zu ändern.")
            fig = go.Figure(data = datanull)
            fig.update_layout(template="plotly_dark",
            autosize=True, height = 600
            )
            st.plotly_chart(fig, use_container_width=True)