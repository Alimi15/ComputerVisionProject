def get_prediction(prediction):
    if prediction[0][0] > 0.5:
        return "Rock"
    elif prediction[0][1] > 0.5:
        return "Paper"
    elif prediction[0][2] > 0.5:
        return "Scissors"
    else:
        return "Nothing"