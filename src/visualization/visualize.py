# Imports
from wordcloud import WordCloud # visualize text data where size of each word indicates its frequency or importance
import matplotlib.pyplot as plt 

job_titles = data_copy.job_title.values

wordcloud = WordCloud().generate(str(job_titles))

plt.figure(figsize=(15,15))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
