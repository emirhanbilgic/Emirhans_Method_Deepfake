import os
import subprocess
import sys

def run_prediction(image_path):
    print(f"Predicting for image: {image_path}")
    command = [
        'sudo', 'cog', 'predict', 
        '-i', f'image=@{image_path}', 
        '-i', 'caption=false', 
        '-i', 'question="is the face in the picture manipulated with deepfake kind of technology?"', 
        '-i', 'temperature=1', 
        '-i', 'use_nucleus_sampling=false'
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    print(f"Prediction result: {result.stdout.strip()}")
    return 'yes' in result.stdout.lower()  # Assuming 'yes' indicates a deepfake

def evaluate_folder(folder_path):
    fake_count = 0
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(f"Evaluating folder: {folder_path}")
    for image_file in image_files:
        if run_prediction(image_file):
            fake_count += 1
    print(f"Number of fakes detected in the folder: {fake_count}")
    return fake_count

def main(base_path):
    categories = {'fakes': 0, 'reals': 1}
    results = {'true_positive': 0, 'false_positive': 0, 'true_negative': 0, 'false_negative': 0}
    
    for category, label in categories.items():
        category_path = os.path.join(base_path, category)
        subfolders = [os.path.join(category_path, f) for f in os.listdir(category_path) if os.path.isdir(os.path.join(category_path, f))]
        
        for folder in subfolders:
            majority_fake = evaluate_folder(folder) >= 2
            if majority_fake and label == 0:
                results['true_positive'] += 1
            elif majority_fake and label == 1:
                results['false_positive'] += 1
            elif not majority_fake and label == 0:
                results['false_negative'] += 1
            elif not majority_fake and label == 1:
                results['true_negative'] += 1
    
    total_predictions = sum(results.values())
    accuracy = (results['true_positive'] + results['true_negative']) / total_predictions
    print("Final Accuracy:", accuracy)
    print("Detailed Results:", results)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py [base_path]")
        sys.exit(1)
    main(sys.argv[1])
