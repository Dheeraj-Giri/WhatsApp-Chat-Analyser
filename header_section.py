from urlextract import URLExtract
from wordcloud import WordCloud

extract = URLExtract()


def fetch_stats(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    # total number of messages
    num_message = df.shape[0]

    # total number of words

    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch the number of media shared
    num_media_shared = df[df['message'] == '<Media omitted>\n'].shape[0]

    # Fetch the number of link shared

    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_message, len(words), num_media_shared, len(links)


def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={"index": "name", "user": "percent"})
    return x, df


def create_wordcloud(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    wc = WordCloud(width=500, height=400, min_font_size=10, background_color="white")
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc


