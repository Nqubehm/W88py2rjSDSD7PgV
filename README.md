# W88py2rjSDSD7PgV


We want to predict how fit the candidate is based on their unique identifiers, their job titles, geographical location and number of connections each candidate has.

Given the above keywords, we can first find the similarities between them and the job titles. After finding these similarities, we will then rank candidates based on them.

We will use methods like jaccard and cosine similarities to find the similarity scores we'll use as the fitness score. Jaccard Similarity takes in the text data as inputs but Cosine Similarity takes in numbers as input. This means that we'll have to represent our data as numerical vectors using methods like word embeddings (word2vec and glove) that are context independent and BERT embeddings which learns contextual representations on unlabeled data.
