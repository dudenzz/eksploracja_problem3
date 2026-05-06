import kagglehub
import os

download_path = kagglehub.dataset_download("daniilor/semeval-2026-task13")

train_filename = "SemEval-2026-Task13\\task_a\\task_a_training_set_1.parquet"
val_filename = "SemEval-2026-Task13\\task_a\\task_a_validation_set.parquet"
test_filename = "SemEval-2026-Task13\\task_a\\task_a_test_set_sample.parquet"
full_train_path = os.path.join(download_path, train_filename)
full_val_path = os.path.join(download_path, val_filename)
full_test_path = os.path.join(download_path, test_filename)

with open('src/config.py', 'w+', encoding='utf-8') as f:
    f.write(f'traindatapath = {repr(full_train_path)}\n')
    f.write(f'testdatapath = {repr(full_test_path)}\n')
    f.write(f'valdatapath = {repr(full_val_path)}')

print(f"Sukces! Ścieżka zapisana w config.py: {download_path}")