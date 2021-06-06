def generate_wordcloud(df):
    from wordcloud import WordCloud
    import numpy as np
    import matplotlib.pyplot as plt
    #print(df)
    input_dict = {}
    l=len(df['entity_name'])
    print(l)
    for x in range(l):
        input_dict[df['entity_name'][x]]=int(df['entity_salience'][x])
    #print(input_dict)
    #df_dict = df.to_dict('records')
    #print(input_dict)
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Pastel1', collocations=False).generate_from_frequencies(input_dict)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig('wc.png')

