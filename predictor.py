from tensorflow.keras.models import load_model
import joblib

class Predictor:
    model = None
    scaler = None

    def __init__(self) -> None:
        model = load_model('pretrained_objects/osf_model.h5')
        scaler = joblib.load('pretrained_objects/osf_scaler.pkl')

    def predict_risk():

        return 1
