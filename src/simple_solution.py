import pandas as pd
import config
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score, classification_report

df_train = pd.read_parquet(config.traindatapath)
df_val = pd.read_parquet(config.valdatapath)
df_test = pd.read_parquet(config.testdatapath)


preprocessor = ColumnTransformer(
    transformers=[

        ('code_tfidf', TfidfVectorizer(
            max_features=100
        ), 'code'),
        
        ('lang_enc', OneHotEncoder(handle_unknown='ignore'), ['language'])
    ]
)


pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', SGDClassifier(loss='hinge', penalty='l2', random_state=42))
])


features = ['code', 'language']
pipeline.fit(df_train[features], df_train['label'])

#### Ewaluacja wewnętrzna####
# 1. Ewaluacja na zbiorze treningowym
print("Ewaluacja na zbiorze treningowym:")
train_acc = pipeline.score(df_train[features], df_train['label'])
print(f"Dokładność(treningowy): {train_acc:.4f}")


# 2. Ewaluacja na zbiorze walidacyjnym
print("\nEwaluacja na zbiorze walidacyjnym:")
y_pred = pipeline.predict(df_val[features])
val_f1 = f1_score(df_val['label'], y_pred, average='macro')

print(f"F1(walidacyjny):  {val_f1:.4f}")
print("\nRaport(walidacyjny):")
print(classification_report(df_val['label'], y_pred))
###################

#### Ewaluacja właściwa####
print("\nEwaluacja na zbiorze testowym:")
y_pred = pipeline.predict(df_test[features])
print(f"F1: {f1_score(df_test['label'], y_pred):.4f}")
print("\nRaport:")
print(classification_report(df_test['label'], y_pred))
###################