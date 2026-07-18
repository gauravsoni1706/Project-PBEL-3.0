import pandas as pd

df = pd.read_csv("dataset/creditcard.csv")

# Remove the target column
X = df.drop(columns=["Class"])

# Select rows that contain fraud
fraud = df[df["Class"] == 1].drop(columns=["Class"]).head(20)

# Select some normal transactions
normal = df[df["Class"] == 0].drop(columns=["Class"]).head(80)

# Combine them
test = pd.concat([normal, fraud])

# Shuffle the rows
test = test.sample(frac=1, random_state=42)

test.to_csv("fraud_test.csv", index=False)

print("Created fraud_test.csv")