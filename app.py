import numpy as np
from flask import Flask, render_template, request
import pickle

top_50 = pickle.load(open('top_50.pkl','rb'))
PVT = pickle.load(open('PVT.pkl','rb'))
similarity_score = pickle.load(open('simiarity_score.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Index.html',
                           book_name = list(top_50['Book-Title'].values),
                           author = list(top_50['Book-Author'].values),
                           image = list(top_50['Image-URL-M'].values),
                           votes = list(top_50['No_of_ratings'].values),
                           rating = list(top_50['avg_rating'].values)
                           )
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(PVT.index == user_input)[0][0]
    distances = similarity_score[index]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:9]

    data = []

    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == PVT.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return render_template('recommend.html',data=data)

@app.route('/contact',methods=['GET'])
def contact():
    return "www.linkedin.com/in/b-akshay-k"

if __name__ == '__main__':
    app.run(debug=True)
