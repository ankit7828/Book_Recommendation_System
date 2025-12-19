from flask import Flask, render_template, request
import pickle
import numpy as np

books_data = pickle.load(open('books_data.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_score.pkl','rb'))

app = Flask(__name__)

book_titles = list(pt.index)

@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(books_data['Book_Title'].values),
        author=list(books_data['Book_Author'].values),
        image=list(books_data['Image_URL_M'].values),
        votes=list(books_data['num_ratings'].values),
        rating=list(books_data['avg_ratings'].values)
    )

@app.route('/recommend')
def recommend_ui():
    return render_template(
        'recommend.html',
        book_titles=book_titles
    )

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]

    data = []
    for i in similar_items:
        temp_df = books[books['Book_Title'] == pt.index[i[0]]]

        item = [
            temp_df.drop_duplicates('Book_Title')['Book_Title'].values[0],
            temp_df.drop_duplicates('Book_Title')['Book_Author'].values[0],
            temp_df.drop_duplicates('Book_Title')['Image_URL_M'].values[0]
        ]
        data.append(item)

    return render_template(
        'recommend.html',
        book_titles=book_titles,
        data=data
    )

if __name__ == '__main__':
    app.run(debug=True)
