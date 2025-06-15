from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)


y_pred = model.predict(X_test)

accuracy = round(accuracy_score(y_test, y_pred), 2)
precision = round(precision_score(y_test, y_pred, average='weighted'), 2)
recall = round(recall_score(y_test, y_pred, average='weighted'), 2)
f1 = round(f1_score(y_test, y_pred, average='weighted'), 2)
confusion = confusion_matrix(y_test, y_pred)

print(f'準確率：{accuracy}')
print(f'精確率：{precision}')
print(f'召回率：{recall}')
print(f'F1 分數：{f1}')
print('混淆矩陣：')
print(confusion)