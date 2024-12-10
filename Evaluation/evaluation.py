
!pip install pycocotools
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import json

# Paths to Ground Truth and Predictions
GROUND_TRUTH_PATH = "path/to/Ground_Truth.json"  # Update with the path to your ground truth file
PREDICTIONS_PATH = "path/to/Predictions.json"   # Update with the path to your predictions file

def load_coco_data(ground_truth_path, predictions_path):
    """Loads COCO Ground Truth and Predictions."""
    print("Loading Ground Truth...")
    coco_gt = COCO(ground_truth_path)
    print("Loading Predictions...")
    coco_pred = coco_gt.loadRes(predictions_path)
    return coco_gt, coco_pred

def evaluate_coco(coco_gt, coco_pred):
    """Evaluates predictions using COCO Evaluation metrics."""
    print("Evaluating...")
    coco_eval = COCOeval(coco_gt, coco_pred, iouType='bbox')
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

def main():
    try:
        # Load Data
        coco_gt, coco_pred = load_coco_data(GROUND_TRUTH_PATH, PREDICTIONS_PATH)
        
        # Evaluate
        evaluate_coco(coco_gt, coco_pred)
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
