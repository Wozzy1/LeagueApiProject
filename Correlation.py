import pandas as pd
from sklearn.linear_model import LogisticRegression

# Data
data = {
    'Win': [True, False, True, False, False, False, True, True, False, False, False, True, False, True, True, True, False, True, False, False],
    'CS': [285, 281, 299, 146, 247, 163, 289, 251, 175, 199, 145, 266, 186, 163, 11, 239, 64, 169, 128, 75]
}

df = pd.DataFrame(data)

# Create the logistic regression model
model = LogisticRegression()

# Fit the model
model.fit(df[['CS']], df['Win'])

# Print the coefficient and intercept
print("Coefficient:", model.coef_[0][0])
print("Intercept:", model.intercept_[0])
