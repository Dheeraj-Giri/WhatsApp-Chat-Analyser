from urlextract import  URLExtract

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
