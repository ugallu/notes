import os
from sklearn.feature_extraction.text import CountVectorizer # fast learning courve lib
from sklearn.ensemble import RandomForestClassifier  # fast learning courve lib

from KaggleWord2VecUtility import KaggleWord2VecUtility # clean data
import pandas as pd # read csv
import nltk # remove junk words

if __name__=='__main__':
    # read the data
    train = pd.read_csv(os.path.join(os.path.dirname(__file__),'data', 'labeledTrainData.tsv'), header=0, \
    delimiter="\t", quoting=3)
    test = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'testData.tsv'), header=0, delimiter="\t", \
    quoting=3)

# we read the data correctly? print out the first thing
print 'The first review is:'
print train["review"][0]
#raw_input("Press Enter to continue...")

# clean the training data
print "Download text dta sets."
#nltk.download()
clean_train_reviews = []
print "Cleaning and parsing the training set moview reviews..\n"
for i in xrange(0, len(train["review"])):
    clean_train_reviews.append("".join(KaggleWord2VecUtility.review_to_wordlist(train["review"][i], True)))

# create the bag of words
# word frequencies, max 5k word
print "Creating the bag of words...\n"
vectorizer = CountVectorizer(analyzer='word',
                            tokenzier = None,
                            preprocessor=None,
                            stop_words=None,
                            max_features=5000)

# fit model to data
train_data_features = vectorizer.fit_transform(clean_train_reviews)
train_data_features = train_data_features.toarray()

# create a classifier
# random forest - set of dec trees
print "Training the random forest needs some time..."
forest = RandomForestClassifier(n_estimators=100)
forest = forest.fit(train_data_features, train["sentiment"])
clean_test_reviews = []

# format and test data
print "Cleaning and parsing test set moview reviews...\n"
for i in xrange(0, len(test["review"])):
    clean_test_reviews.append("".join(KaggleWord2VecUtility.review_to_wordlist(test["review"][i], True)))
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_Data_features.toarray()

# predict reviews in testing data
print "Predicting test labels...\n"
result = forest.predict(test_data_features)
output = pd.DataFrame(data={"id":test["id"], "sentiment": result})
output.to_csv(os.path.join(os.path.dirname(__file__),
'data', 'Bag_of_Words_model.csv'), index=False, quoting=3)
print "Wrote results to Bag_of_Words_model.csv"





