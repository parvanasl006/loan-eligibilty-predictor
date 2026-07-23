import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(filepath):

    df = pd.read_csv(filepath)

    print("Dataset Loaded Successfully")
    print(df.head())

    # Fill Missing Values
    for col in df.columns:

        if df[col].dtype == 'object':
            df[col].fillna(df[col].mode()[0], inplace=True)

        else:
            df[col].fillna(df[col].median(), inplace=True)

    # Encode Categorical Columns
    encoder = LabelEncoder()

    for col in df.columns:

        if df[col].dtype == 'object':
            df[col] = encoder.fit_transform(df[col])

    print("\nMissing Values Removed")

    return df
