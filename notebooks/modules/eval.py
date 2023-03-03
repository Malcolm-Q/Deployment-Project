from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix,r2_score

def print_scores(y_test,y_pred, compare=False, y_predOld = None):
    if compare:
        r2 = (r2_score(y_test,y_pred)) - (r2_score(y_test,y_predOld))
        accuracy = accuracy_score(y_test, y_pred) - accuracy_score(y_test, y_predOld)
        precision = precision_score(y_test, y_pred) - precision_score(y_test, y_predOld)
        recall = recall_score(y_test, y_pred) - recall_score(y_test, y_predOld)
        f1 = f1_score(y_test, y_pred) - f1_score(y_test, y_predOld)
        auc = roc_auc_score(y_test, y_pred) - roc_auc_score(y_test, y_predOld)
        cm = confusion_matrix(y_test, y_pred) - confusion_matrix(y_test, y_predOld)

        print('R squared increased by:',r2,'\n')
        print('accuracy increased by:',accuracy)
        print('precision increased by:',precision)
        print('recall increased by:',recall)
        print('f1 increased by:',f1)
        print('auc increased by:',auc)
        print('confusion matrix difference:\n',cm)
    else:
        r2 = r2_score(y_test,y_pred)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)

        print('R squared:',r2,'\n')
        print('accuracy:',accuracy)
        print('precision:',precision)
        print('recall:',recall)
        print('f1:',f1)
        print('auc:',auc)
        print('confusion:\n',cm)