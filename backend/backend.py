from flask import Flask
from flask_cors import CORS
from flask import request
import json
# How to start the server for Flask on windows...
# $ export FLASK_APP=backend.py
# $ export FLASK_DEBUG=1
# $ python -m flask run
# or do this in 1 command
# FLASK_APP=backend.py FLASK_DEBUG=1 python -m flask run

app = Flask(__name__)
CORS(app)

@app.route("/")
# @cross_origin()
def hello():
    return "Welcome to the dark side of this webapp."

@app.route("/getAnimeList")
def getAnimeList():
    import json
    import pandas as pd
    anime = pd.read_csv("Anime.csv")
    return json.dumps(anime[' name'].tolist()) # do this so we are sending a python list to the frontend

@app.route("/getRecommendations")
# @cross_origin()
# http://10.1.1.1:5000/login?username=alex&password=pw1
# http://localhost:5000/getRecommendations?anime=kannagi&score=5&medium=False&status=False
def getRecommendations():
    animeName = request.args.get('anime');

    # showRating = int(request.args.get('score'));
    # showType = request.args.get('medium');
    # showStatus = request.args.get('status');
    return doRecommendations(animeName)


def doRecommendations(title, scoreThreshold = 0, isTV = False, isCompleted = False):
    ### 1: LIBRARIES

    import json
    import nltk
    import string
    import pandas as pd
    from nltk.stem.porter import PorterStemmer
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

    # let nltk download corpus
    nltk.download('punkt')

    ### 2: DATASET

    anime = pd.read_csv("Anime.csv")
    # let's get some information
    # print("Shape of dataset: ", anime.shape)

    # let's clean our dataset a little bit
    # fix column names so we don't have to deal with leading spaces
    anime = anime.rename(columns={" name": "name",
                                  " title_english": "title_english",
                                  " title_japanese": "title_japanese",
                                  " title_synonyms": "title_synonyms",
                                  " type": "type",
                                  " source": "source",
                                  " producers": "producers",
                                  " genre": "genre",
                                  " studio": "studio",
                                  " episodes": "episodes",
                                  " status": "status",
                                  " airing": "airing",
                                  " aired": "aired",
                                  " duration": "duration",
                                  " rating": "rating",
                                  " score": "score",
                                  " scored_by": "scored_by",
                                  " rank": "rank",
                                  " popularity": "popularity",
                                  " members": "members",
                                  " favorites": "favorites",
                                  " synopsis": "synopsis",
                                  " background": "background",
                                  " premiered": "premiered",
                                  " broadcast": "broadcast",
                                  " related": "related"})

    # lots of synopsis are missing. we will replace NaN values with empty string
    anime['synopsis'].fillna("", inplace=True)

    # CountVectorizer treats all punctuation as delimiter and generates tokens based on that.
    def cleanGenre(anime):
        if (isinstance(anime['genre'], str)):
            toReturn = anime['genre']
            toReturn = toReturn.replace("[", "")
            toReturn = toReturn.replace("]", "")
            toReturn = toReturn.replace("'", "")
            toReturn = toReturn.replace(", ", ",")
            toReturn = toReturn.replace(" ", "")
            toReturn = toReturn.replace("-", "")
        else:
            toReturn = ""
        return toReturn

    # clean genre
    anime['genre'] = anime.apply(cleanGenre, axis=1)

    # fill in missing scores with 0, we don't care about them
    anime['score'].fillna(0.00, inplace = True)

    ### 3: SIMILARITY MATRICES
    ### Ideally for this section, we would generate multiple similarity matrices, which will then
    ### be used to calculate a weighted average.

    # get a series relating the names of anime to their indicies in the anime table
    indices = pd.Series(anime.index, index=anime['name'])

    # what index is this show located at? assume the title is correctly spelled/formatted
    titleIndex = indices[title]

    # SYNOPSIS SIMILARITY MATRIX
    # create a tokenizer to stem our tokens
    def tokenize(text):  # takes care of stemming
        tokens = nltk.word_tokenize(text)
        stemmed = []
        for item in tokens:
            stemmed.append(PorterStemmer().stem(item))
        return stemmed
    # create custom token dictionary
    token_dict = anime['synopsis'].copy()
    # lowercase and remove punctuation
    for i in token_dict.index:
        token_dict[i] = token_dict[i].lower().translate(str.maketrans('', '', string.punctuation))
    # vectorize our synposis' using TF
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words="english")
    # Learn vocabulary and IDF, return term-document matrix.
    tfidfMatrix = tfidf.fit_transform(token_dict)  # use custom token dictionary to remove uppercase and punctuation
    # the actual similarity matrices. values inside represent the cosine similarity score between the two shows.
    # close to 1 = similar, close to 0 = unrelated, close to -1 = opposite
    synopsisSimilarityMatrix = cosine_similarity(tfidfMatrix[titleIndex], tfidfMatrix)

    # GENRE SIMILARITY MATRIX
    # vectorize genres with CountVectorizer
    genreVector = CountVectorizer()
    # Learn the vocabulary dictionary and return term-document matrix.
    genreMatrix = genreVector.fit_transform(anime['genre'])
    genreSimilarityMatrix = cosine_similarity(genreMatrix[titleIndex], genreMatrix)

    # debug statements for similarity matrices
    # print(synopsisSimilarityMatrix)
    # print(genreSimilarityMatrix)

    ### 4: RECOMMENDATION - Similarity matrices and scoring lists are weighted here
    # This method will return ALL anime based on recommendation
    def generateRecommendations(title):
        # get the cosine similarity score based on feature type
        synopsisScore = list(enumerate(synopsisSimilarityMatrix[0]))
        genreScore = list(enumerate(genreSimilarityMatrix[0]))

        # sort based on anime index first so we can combine weights
        synopsisScoreSorted = sorted(synopsisScore, key=lambda x: x[0], reverse=False)
        genreScoreSorted = sorted(genreScore, key=lambda x: x[0], reverse=False)

        # combine all cosine similarity scores into one cumulative score
        combinedScoresIterator = zip(synopsisScoreSorted,
                                     genreScoreSorted,)

        # debug statement
        # print(set(combinedScoresIterator))

        combinedScore = [(index,
                          ##########################################################
                          (synScore + genScore) / 2)  # WEIGHTING IS CONTROLLED HERE
                         ##########################################################
                         for (index, synScore),
                             (_, genScore),
                         in combinedScoresIterator] # UNPACKED VALUES
        combinedScoreSorted = sorted(combinedScore, key=lambda x: x[1], reverse=True)

        # return all of the sorted shows, to be filtered after this
        return combinedScoreSorted

    ### DATA FILTERING
    def filterRecommendations(sortedBySimilarityArray, numberOfRecommendations, scoreThreshold, isTV, isCompleted):
        # grab indicies of all similarity-sorted shows
        allSortedIndicies = [i[0] for i in sortedBySimilarityArray[0 : len(sortedBySimilarityArray)]]

        # remove all shows with score below score threshold
        scoreFiltered = [i for i in allSortedIndicies if anime['score'][i] >= scoreThreshold]

        # TODO: do the other filtering here

        # only grab the top numberOfRecommendations # of shows
        numFiltered = [i for i in scoreFiltered[1 : min(len(scoreFiltered), numberOfRecommendations + 1)]]

        # return anime names
        return json.dumps((anime['name'].iloc[numFiltered]).tolist()) # do this so we are sending a python list to the frontend

    numRecommendations = 10 # HOW MANY RECOMMENDATIONS DO WE WANT TO SHOW? TEMPORARY VALUE
    return filterRecommendations(sortedBySimilarityArray = generateRecommendations(title),
                                 numberOfRecommendations = numRecommendations,
                                 scoreThreshold = scoreThreshold,
                                 isTV = isTV,
                                 isCompleted = isCompleted)