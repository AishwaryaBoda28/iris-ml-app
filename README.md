IRIS FLOWER PREDICTION WEB APP

Project Description
This project is a Machine Learning web application that predicts Iris flower species using a trained Random Forest model. The app includes a beautiful user interface and stores prediction history using a SQLite database.

Features
- Predict Iris species (Setosa, Versicolor, Virginica)
- Beautiful responsive UI
- SQLite database to store prediction history
- History dashboard to view past predictions
- Easy deployment-ready Flask application

Technology Stack
Python
Flask
Scikit-learn
NumPy
SQLite
HTML & CSS

Project Structure
iris-ml-app/
    app.py
    train.py
    model.pkl
    database.db
    requirements.txt
    templates/
        index.html
        history.html

How to Run the Project
1. Install Python packages
   pip install -r requirements.txt

2. Train the model
   python train.py

3. Run the application
   python app.py

4. Open browser
   http://127.0.0.1:5000

Example Input
Sepal Length = 5.1
Sepal Width  = 3.5
Petal Length = 1.4
Petal Width  = 0.2

Output Example
Setosa

Future Improvements
- Add Deep Learning model
- Deploy to cloud (Render or Heroku)
- Add charts dashboard
- Add login system

Author
Aishwarya Boda
B.Tech AIML Student
GitHub: https://github.com/AishwaryaBoda28
