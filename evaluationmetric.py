from sklearn.metrics import accuracy_score, precision_score, recall_score,  confusion_matrix, ConfusionMatrixDisplay,balanced_accuracy_score
from sklearn.metrics import precision_recall_fscore_support, f1_score, classification_report
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import roc_curve, RocCurveDisplay

class EvaluationMetrics:
    def __init__(self, pipe, X_t, X_val, y_t, y_val):
        self.pipe = pipe
        self.X_t = X_t
        self.X_val = X_val
        self.y_t = y_t
        self.y_val = y_val

    def print_scores(self):
        # Training set predictions
        y_t_pred = self.pipe.predict(self.X_t)
        train_results_dict = {'accuracy': accuracy_score(self.y_t, y_t_pred),
                              'recall': recall_score(self.y_t, y_t_pred, average='weighted'),
                              'precision': precision_score(self.y_t, y_t_pred, average='weighted'),
                              'f1_score': f1_score(self.y_t, y_t_pred, average='weighted')}

        # Validation set predictions
        y_val_pred = self.pipe.predict(self.X_val)
        val_results_dict = {'accuracy': accuracy_score(self.y_val, y_val_pred),
                            'recall': recall_score(self.y_val, y_val_pred, average='weighted'),
                            'precision': precision_score(self.y_val, y_val_pred, average='weighted'),
                            'f1_score': f1_score(self.y_val, y_val_pred, average='weighted')}

        return train_results_dict, val_results_dict
     # Plots roc curve for all classes 
    def plot_roc_curve_ovr(self):
        # Calculate FPR and TPR for each class (One-vs-Rest)
        y_val_pred_proba = self.pipe.predict_proba(self.X_val)
        n_classes = y_val_pred_proba.shape[1]
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(self.y_val, y_val_pred_proba[:, i], pos_label=i)

        # Plot ROC curve for each class (One-vs-Rest)
        plt.figure()
        for i in range(n_classes):
            plt.plot(fpr[i], tpr[i], label=f'Class {i}')
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curve - One-vs-Rest')
        plt.legend(loc="lower right")
        plt.show()
    # Plots confussion matrix
    def plot_confusion_matrix(self, y_val, y_val_pred):
        cm = confusion_matrix(y_val, y_val_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.show()