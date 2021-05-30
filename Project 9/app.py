
from flask import Flask, request, render_template
import numpy as np
import pickle

app   = Flask(__name__, template_folder='.')
model = pickle.load(open('model', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    post = dict(request.form)

    features = [np.array(list(post.values())).astype('int')]
    predict  = int(round(model.predict(features)[0], -2))

    return render_template('index.html',
                prediction='Predicted Salary: ${:,}'.format(predict).replace(',', ' '))

if __name__ == "__main__":
    app.run(debug=True, port=8889)
