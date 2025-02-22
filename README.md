# seminar_1

## 1. How We Work Together

### 1. Structure Description

- The `dataset` folder contains all main datasets and their variants.
- The `evaluation` folder contains tools for evaluating models.
- The `prepare_data` folder contains all logic for cleaning and preparing the data.
- The `workspace` folder contains subfolders for each member's workspace.

### 2. Workflow

- Each member works on creating and training models in their own workspace.
- After training a model, use `evaluation/revenue_sample_submission_generator.ipynb` to generate a submission dataframe.
- Fill in the results in the dataframe and rename the file with the corresponding model name.
- Save all result files in `evaluation/Result/<member_name>`, then upload them to GitHub.
