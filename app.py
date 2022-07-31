import streamlit as st

import preprocessor, header_section

st.sidebar.title("WhatsApp Chat Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:

    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    # st.text(data)
    df = preprocessor.preprocess(data)
    st.dataframe(df)

    user_list = df['user'].unique().tolist()
    user_list.remove('Group Notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox('Show Analyst With Respect to ', user_list)

    if st.sidebar.button("Show Analysis"):
        col1, col2, col3, col4 = st.columns(4)

        num_messages = header_section.fetch_stats(selected_user, df)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)