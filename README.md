# seminar_1

## 1. How We Work Together

### 1. Structure Description

- The `dataset` folder contains all main datasets and their variants.
- The `evaluation` folder contains tools for evaluating models.
- The `prepare_data` folder contains all logic for cleaning and preparing the data.
- The `workspace` folder contains subfolders for each member's workspace.

### 2. Purpose

- Predict the revenues of 10 stores (`CA_1`, `CA_2`, `CA_3`, `CA_4`, `TX_1`, `TX_2`, `TX_3`, `WI_1`, `WI_2`, `WI_3`) from day `25-04-2016` (`d_1914`) to `22-05-2016` (`d_1941`).

- Note: Submission dataframe could be generated using `evaluation/revenue_sample_submission_generator.ipynb`.

### 3. Workflow

- Each member works on creating and training models in their own workspace.
- After training a model, use `evaluation/revenue_sample_submission_generator.ipynb` to generate a submission dataframe.
- Fill in the results in the dataframe and rename the file with the corresponding model name.
- Save all result files in `evaluation/Result/<member_name>`, then upload them to GitHub.
