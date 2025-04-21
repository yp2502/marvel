

import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE

data = pd.read_excel('exp5_Admission_St.xlsx')

X = data.drop('Admit', axis=1)
y = data['Admit']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print("Before SMOTE - Train Distribution:", Counter(y_train))

model_before = LogisticRegression()
model_before.fit(X_train, y_train)
y_pred_before = model_before.predict(X_test)

print("\nBefore SMOTE - Accuracy:", accuracy_score(y_test, y_pred_before))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_before))
print("Classification Report:\n", classification_report(y_test, y_pred_before))

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

print("\nAfter SMOTE - Train Distribution:", Counter(y_resampled))

model_after = LogisticRegression()
model_after.fit(X_resampled, y_resampled)
y_pred_after = model_after.predict(X_test)

print("\nAfter SMOTE - Accuracy:", accuracy_score(y_test, y_pred_after))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_after))
print("Classification Report:\n", classification_report(y_test, y_pred_after))