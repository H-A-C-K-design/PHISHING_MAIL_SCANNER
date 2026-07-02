from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions, output_dict=True)
    matrix = confusion_matrix(y_test, predictions)
    roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    return {
        "classification_report": report,
        "confusion_matrix": matrix,
        "roc_auc": roc_auc,
    }
