def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    
    # zeroclass = prediction[0]
    
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    
    
    for i in range(prediction.shape[0]):
        if prediction[i] == 0:
            if prediction[i] == ground_truth[i]:
                TN += 1
            else: 
                FN += 1
        else:
            if prediction[i] == ground_truth[i]:
                TP += 1
            else: 
                FP += 1
    
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    if TP + FP > 0:
        precision = TP / (TP + FP)
    else:
        precision = 0
    recall = TP / (TP + FN)
    f1 = 2*precision*recall / (precision + recall)
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    accuracy = 0
    for i in range(len(prediction)):
        if prediction[i] == ground_truth[i]:
            accuracy +=1
    return accuracy / len(prediction)
