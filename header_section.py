def fetch_stats(selected_user, df):

    if selected_user == "Overall":
        return df.shape[0]