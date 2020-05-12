"""
Convert word2vec models to JSON database by cosine distance metric
"""

from gensim.models import KeyedVectors
import json
__author__ = "Phi Van Thuy"

# Trained model
model_path = "/home/basel/Data/data/ijabat/AllTitles.bin"

print("Loading model...")
model = KeyedVectors.load_word2vec_format(model_path, binary=True, encoding='utf-8', unicode_errors='ignore')  # C binary format
print("Loading model: Done")

# Name of output file
with open('custom_cosine_simialrity.json', 'w') as f:
    #f.write("{\n")

    number_words = len(model.vocab)
    # number_words = 10000
    dic = {}
    for i in range(0, number_words):
        stringA = list(model.vocab.items())[i][0]
        #f.write("\n\"" + stringA.replace('"', '') + "\":[\n")
        dic[stringA] = []
        nearest_words = model.most_similar(positive=[stringA], negative=[], topn=20)
        number_nearest_words = len(nearest_words)

        for j in range(0, number_nearest_words):
            #f.write("{\"w\":\"" + nearest_words[j][0].replace('"', "") + "\",\"d\":" + str(round(nearest_words[j][1], 3)) + "}")
            dic[stringA].append({
                'w' : nearest_words[j][0],
                'd' : str(round(nearest_words[j][1], 3))
            })
            #if j != number_nearest_words - 1:
            #    #f.write(",\n")
            #else:
            #    f.write("]")

        #if i != number_words - 1:
        #    f.write(",\n")
        #else:
        #    f.write("\n")
    json.dump(dic, f, ensure_ascii=False, indent=4)
    #f.write("\n}\n")

print("Finished!")
