from src.data_preprocessing import preprocess_data

from src.visualization import visualize_data

from src.train_model import train_model

from src.predict import predict

from src.utils import line


line()

df = preprocess_data("data/loan_data.csv")

line()

visualize_data(df)

line()

train_model(df)

line()

predict(df)

line()
