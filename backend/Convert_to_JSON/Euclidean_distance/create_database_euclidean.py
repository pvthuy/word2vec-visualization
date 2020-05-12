"""
Convert word2vec models to JSON database by Euclidean distance metric (instead of Cosine distance)
"""


from gensim.models import KeyedVectors

__author__ = "Phi Van Thuy"

# Trained model
model_path = "your/model/path/here.bin"

print("Loading model...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True)  # C binary format
print("Loading model: Done")

with open('en_data_euclidean_skipgram.json', 'w') as f:
    f.write("{\n")

    number_words = len(model.vocab)
    # number_words = 10000
    for i in range(0, number_words):

        stringA = list(model.vocab.items())[i][0]
        f.write("\n\"" + stringA + "\":[\n")

        nearest_words = model.most_similar_euclidean(positive=[stringA], negative=[], topn=20)
        number_nearest_words = len(nearest_words)

        for j in range(0, number_nearest_words):
            f.write("{\"w\":\"" + nearest_words[j][0] + "\",\"d\":" + str(round(nearest_words[j][1], 3)) + "}")
            if j != number_nearest_words - 1:
                f.write(",\n")
            else:
                f.write("]")

        if i != number_words - 1:
            f.write(",\n")
        else:
            f.write("\n")

    f.write("\n}\n")

print("Finished!")
