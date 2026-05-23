import numpy as np

def extract_sniff_features(sniff_intensity, rhythm_stability):
    """
    Simulates extracting MFCC features from a sniff.
    In a real app, this would use Librosa on an audio file.
    """
    # We create a 1D array representing the 'latent space' of the sniff
    features = np.array([[sniff_intensity, rhythm_stability]])
    return features

def calculate_risk_score(reconstruction_error):
    """
    Simulates the LSTM-Autoencoder reconstruction error.
    Higher error = Higher Neurological anomaly.
    """
    # Map the error to a 0-100% scale
    risk = min(max(reconstruction_error * 10, 0), 100)
    return risk