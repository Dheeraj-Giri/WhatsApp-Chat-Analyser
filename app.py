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

    # stats user

    if st.sidebar.button("Show Analysis"):
        col1, col2, col3, col4 = st.columns(4)

        num_messages, num_words, num_media_shared, link_shared = header_section.fetch_stats(selected_user, df)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(num_words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_shared)
        with col4:
            st.header("Links Shared")
            st.title(link_shared)

    # finding the busiest user in the group(Group level)l
