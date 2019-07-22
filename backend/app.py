from flask import Flask, request, jsonify
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib
import pandas as pd
import time

# declare constants
HOST = '0.0.0.0'
PORT = 8081

# initialize flask application
app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    # get iris object from request
    X = request.get_json()    
    X = [float(X['course1']), float(X['course2']), float(X['course3']), float(X['course4']),float(X['course5']), float(X['course6']), float(X['course7']), float(X['course8']), float(X['course9']), float(X['course10']), float(X['course11']), float(X['course12'])] 
    courses = {
        111:0,
        112:1,
        113:2,
        116:3,
        200:4,
        216:5,
        226:6,
        230:7,
        236:8,
        246:9,
        251:10,
        255:11,
        281:12,
        302:13,
        316:14,
        326:15,
        333:16,
        342:17,
        379:18,
        401:19,
        402:20,
        405:21,
        406:22,
        411:23,
        412:24,
        422:25,
        427:26,
        428:27,
        431:28,
        440:29,
        442:30,
        450:31,
        453:32,
        454:33,
        455:34,
        456:35,
        461:37,
        462:38,
        467:39,
        474:40,
        481:41,
        482:42,
        484:43
    }
    course_to_value = [0]*43
    for x in X:
        if x in courses:
            course_to_value[courses[x]] = 1
    df = pd.read_csv("course_taken.csv")
    df1 = df.drop([71])
    X=df1[df1.columns[1:44]].values
    model = ensemble.GradientBoostingRegressor(n_estimators=600, learning_rate=0.1, max_depth=7, min_samples_leaf=3, max_features=0.1, loss='huber') 
    courses_to_value = [course_to_value]

    grad_courses = []

    for i in range(44, 102):
        y = df1[df1.columns[i]].values
        model.fit(X,y)
        predicted_course_values = model.predict(courses_to_value)
        predicted_value = predicted_course_values[0]
        #print("hello")
        #print(predicted_course_values)
        if(predicted_value>=0.6):
            #print("lol")
            #print("You should take course " +df1.columns[i ] +": "+format(predicted_value))
            grad_courses.append({'value': df1.columns[i]})
            #print(grad_courses)
        # return jsonify([{'name': grad_courses[0]},
        #             {'name': 'Iris-Versicolour', 'value': round(probabilities[0, 1] * 100, 2)},
        #             {'name': 'Iris-Virginica', 'value': round(probabilities[0, 2] * 100, 2)}])
    print(grad_courses)
    print("i have passed this stage")
    return jsonify(grad_courses)

# @app.route('/api/train', methods=['POST'])
# def train():
#     # get parameters from request
#     parameters = request.get_json()

#     # read iris data set
#     iris = datasets.load_iris()
#     X, y = iris.data, iris.target

#     # fit model
#     clf = svm.SVC(C=float(parameters['C']),
#                   probability=True,
#                   random_state=1)
#     clf.fit(X, y)

#     # persist model
#     joblib.dump(clf, 'model.pkl')

#     return jsonify({'accuracy': round(clf.score(X, y) * 100, 2)})


# @app.route('/api/predict', methods=['POST'])
# def predict():
#     # get iris object from request
#     X = request.get_json()    
#     X = [[float(X['course1']), float(X['course2']), float(X['course3']), float(X['course4']),float(X['course5']), float(X['course6']), float(X['course7']), float(X['course8']), float(X['course9']), float(X['course10']), float(X['course11']), float(X['course12'])]]
#     print("The response is: ", X)
#     # read model
#     clf = joblib.load('model.pkl')
#     probabilities = clf.predict_proba(X)
#     return "HELLO"
#     


if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)
