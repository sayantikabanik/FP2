import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
print(model, file=sys.stderr)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [ int(x) for x in request.form.values() ]
    final_features = [ np.array(int_features) ]
    prediction = model.predict(final_features)
    print(prediction, file=sys.stderr)
    output = prediction #round(prediction[0], 2)
    return render_template('index.html', prediction_text='Predicted Price (Monthly Avg - INR) $ {}'.format(output))


if __name__=='__main__':
    app.run(debug=True)
