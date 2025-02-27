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

- **Step 1** - Each member works on creating and training models in their own workspace.
- **Step 2** - After training a model, use `evaluation/revenue_sample_submission_generator.ipynb` to generate a submission dataframe.
- **Step 3** - Fill MODEL_NAME and STATE_NAME
  - MODEL_NAME: str = "my_model_name"
  - STATE_NAME: State = State.`CA_1`
- A data frame as follow will be generated with name `CA_1_my_model_name.csv`

| id   | date       | d      | CA_1 |
|------|-----------|--------|------|
| 1914 | 2016-04-25 | d_1914 | 0    |
| 1915 | 2016-04-26 | d_1915 | 0    |
| 1916 | 2016-04-27 | d_1916 | 0    |
| 1917 | 2016-04-28 | d_1917 | 0    |
| 1918 | 2016-04-29 | d_1918 | 0    |
| 1919 | 2016-04-30 | d_1919 | 0    |
| 1920 | 2016-05-01 | d_1920 | 0    |
| 1921 | 2016-05-02 | d_1921 | 0    |
| 1922 | 2016-05-03 | d_1922 | 0    |
| 1923 | 2016-05-04 | d_1923 | 0    |
| 1924 | 2016-05-05 | d_1924 | 0    |
| 1925 | 2016-05-06 | d_1925 | 0    |
| 1926 | 2016-05-07 | d_1926 | 0    |
| 1927 | 2016-05-08 | d_1927 | 0    |
| 1928 | 2016-05-09 | d_1928 | 0    |
| 1929 | 2016-05-10 | d_1929 | 0    |
| 1930 | 2016-05-11 | d_1930 | 0    |
| 1931 | 2016-05-12 | d_1931 | 0    |
| 1932 | 2016-05-13 | d_1932 | 0    |
| 1933 | 2016-05-14 | d_1933 | 0    |
| 1934 | 2016-05-15 | d_1934 | 0    |
| 1935 | 2016-05-16 | d_1935 | 0    |
| 1936 | 2016-05-17 | d_1936 | 0    |
| 1937 | 2016-05-18 | d_1937 | 0    |
| 1938 | 2016-05-19 | d_1938 | 0    |
| 1939 | 2016-05-20 | d_1939 | 0    |
| 1940 | 2016-05-21 | d_1940 | 0    |
| 1941 | 2016-05-22 | d_1941 | 0    |

- **Step 4** - Fill the results in the dataframe.
- **Step 5** - Save all result files in `evaluation/Result/<member_name>`, then upload them to GitHub.
