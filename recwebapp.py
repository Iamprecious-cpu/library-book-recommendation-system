from flask import Flask, request, render_template
import os

# setting up template directory
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=TEMPLATE_DIR)
#app = Flask(__name__)

import pandas as pd
import numpy as np
from numpy import int64

import requests
import IPython.display as Disp

import sklearn
from sklearn.decomposition import TruncatedSVD

@app.route("/")
def hello():
	return TEMPLATE_DIR
 
import pandas as pd; 
df = pd.read_csv('./dataset/books.csv'); 
print(df.columns.tolist()); df2 = pd.read_csv('./dataset/ratings.csv');
print(df2.columns.tolist())

print("building recommendation engine")
print("reading data")
books_df = pd.read_csv("./dataset/books.csv")
ratings_df = pd.read_csv("./dataset/ratings.csv", encoding='UTF-8',  dtype={'UserID': int,'BookID':int, 'Rating':int} )
books_df_2 = books_df[['BookID', 'Location', 'AverageRating','OriginalTitle','Authors']]
combined_books_df = pd.merge(ratings_df, books_df, on='BookID')
print("creating pivot table")
ct_df = combined_books_df.pivot_table(values='Rating', index='UserID', columns='OriginalTitle', fill_value=0)
X = ct_df.values.T
print("Creating SVD")
SVD  = TruncatedSVD(n_components=20, random_state=17)
result_matrix = SVD.fit_transform(X)
print("building correlation")
corr_mat = np.corrcoef(result_matrix)
book_names = ct_df.columns
book_list = list(book_names)
isInitialized = True
print(book_list.index("Operating systems and architecture"))
print("done building recommendation engine")
print("ready for recommendation engine")
def getRecommendations(bookName):
	book_name_index = book_list.index(bookName)
	corr_book = corr_mat[book_name_index]
	recList = list(book_names[(corr_book<1.0) & (corr_book>0.9)])
	max=5
	if(len(recList)<5):
		max=len(recList)
	return books_df_2[books_df_2.OriginalTitle.isin(recList)]



@app.route("/rec", methods=['GET', 'POST'])
def rec():
    query = ''
    if request.method == "POST":
        query = request.form.get('query')
        recommendations = getRecommendations(query)
        recommendations_html = recommendations.to_html(classes='table table-bordered')
        return render_template('rec.html', query=query, recommendations=recommendations_html, book_list=book_list)
    else:
        return render_template('rec.html', query="", recommendations="<<unknown>>", book_list=book_list)



if __name__ == "__main__":
    app.run()
