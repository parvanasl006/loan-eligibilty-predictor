import matplotlib.pyplot as plt


def visualize_data(df):

    # Loan Status

    plt.figure(figsize=(6,4))

    df["Loan_Status"].value_counts().plot(kind='bar')

    plt.title("Loan Status")
    plt.xlabel("Loan Approved")
    plt.ylabel("Count")

    plt.show()

    # Applicant Income

    plt.figure(figsize=(7,5))

    plt.hist(df["ApplicantIncome"], bins=20)

    plt.title("Applicant Income Distribution")

    plt.xlabel("Income")

    plt.ylabel("Frequency")

    plt.show()

    # Loan Amount

    plt.figure(figsize=(7,5))

    plt.hist(df["LoanAmount"], bins=20)

    plt.title("Loan Amount Distribution")

    plt.xlabel("Loan Amount")

    plt.ylabel("Frequency")

    plt.show()
