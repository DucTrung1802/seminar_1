import numpy as np

def rmsse(train: np.ndarray, actual: np.ndarray, forecast: np.ndarray) -> float:
    """
    Compute Root Mean Squared Scaled Error (RMSSE) based on the correct formula.

    Parameters:
        train (np.ndarray): Array of historical (training) data
        actual (np.ndarray): Array of actual values for the test period
        forecast (np.ndarray): Array of forecasted values

    Returns:
        float: RMSSE value
    """

    # Compute scale denominator
    denominator = np.mean(np.square(np.diff(train)))

    if denominator == 0:
        return np.nan  # Avoid division by zero

    # Compute numerator
    numerator = np.mean(np.square(actual - forecast))

    return np.sqrt(numerator / denominator)