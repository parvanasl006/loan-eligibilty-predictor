from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

import joblib


def train_model(df):

    X = df.drop("Loan_Status", axis=1)

    y = df["Loan_Status"]

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,
        test_size=0.20,
        random_state=42

    )

    model = RandomForestClassifier(

        n_estimators=100,
        random_state=42

    )

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print("\nModel Accuracy:", accuracy)

    joblib.dump(model, "models/loan_model.pkl")

    print("Model Saved")

    return model
