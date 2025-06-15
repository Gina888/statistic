from sklearn.model_selection import train_test_split


X = df_selected.drop(columns='Y')
y = df_selected['Y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)