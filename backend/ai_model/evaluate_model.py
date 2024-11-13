import torch
import numpy as np
from model import TradingModel

def evaluate_model(model_path, test_data, input_size):
    """Evaluate the trained model on test data and print evaluation metrics."""
    # Load the trained model
    model = TradingModel(input_size)
    model.load_state_dict(torch.load(model_path))
    model.eval()  # Set the model to evaluation mode

    # Convert test data to tensors
    X_test = torch.tensor(np.array([d['features'] for d in test_data]), dtype=torch.float32)
    y_test = torch.tensor(np.array([d['label'] for d in test_data]), dtype=torch.float32).view(-1, 1)

    # Make predictions
    with torch.no_grad():
        predictions = model(X_test)
        predicted_labels = (predictions > 0.5).float()

    # Calculate accuracy
    correct = (predicted_labels == y_test).sum().item()
    total = y_test.size(0)
    accuracy = correct / total * 100

    print(f"Evaluation Accuracy: {accuracy:.2f}%")

    return accuracy

if __name__ == "__main__":
    # Example placeholder test data
    test_data = [{'features': [0.4, 0.5, 0.7], 'label': 1}, {'features': [0.2, 0.3, 0.4], 'label': 0}]
    evaluate_model('trained_model.pth', test_data, input_size=len(test_data[0]['features']))
