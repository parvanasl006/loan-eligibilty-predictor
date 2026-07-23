import joblib


def predict(df):

    model = joblib.load("models/loan_model.pkl")

    X = df.drop("Loan_Status", axis=1)

    sample = X.iloc[[0]]

    prediction = model.predict(sample)

    if prediction[0] == 1:

        print("\nLoan Approved")

    else:

        print("\nLoan Rejected")
