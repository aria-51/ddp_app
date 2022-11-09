import pickle

def get_trained_model():
    loaded_model = pickle.load(open('logreg_model.sav', 'rb'))

    return loaded_model


def get_trained_vectorizer():
    loaded_vect = pickle.load(open('vectorizer.sav', 'rb'))
    
    return loaded_vect