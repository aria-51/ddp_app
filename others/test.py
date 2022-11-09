import pandas
import pickle
loaded_vect = pickle.load(open('others/vectorizer.sav','rb'))
print(loaded_vect)

text = 'yooo this is the sickest plan ever wow hot wooah'
transf_text = loaded_vect.transform([text])
print(transf_text.toarray())

loaded_model = pickle.load(open('others/logreg_model.sav', 'rb'))
prediction = loaded_model.predict(transf_text)
print(prediction)
#print(loaded_model)