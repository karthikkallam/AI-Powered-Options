import torch
import numpy as np

def prepare_data_for_training(data):
    """Prepare raw data for training by splitting features and labels."""
    X = np.array([d['features'] for d in data], dtype=np.float32)
    y = np.array([d['label'] for d in data], dtype=np.float32)
    return torch.tensor(X), torch.tensor(y).view(-1, 1)

def calculate_metrics(predictions, actuals):
    """Calculate evaluation metrics for model predictions."""
    predicted_labels = (predictions > 0.5).float()
    accuracy = (predicted_labels == actuals).sum().item() / actuals.size(0) * 100

    # Example: Add more metrics as needed
    return {
        'accuracy': accuracy
    }

def save_model(model, file_path='trained_model.pth'):
    """Save the trained model to a file."""
    try:
        torch.save(model.state_dict(), file_path)
        print(f"Model saved to {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")
        raise

def load_model(model_class, file_path, input_size):
    """Load a model from a file."""
    model = model_class(input_size)
    try:
        model.load_state_dict(torch.load(file_path))
        model.eval()
        print(f"Model loaded from {file_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise
