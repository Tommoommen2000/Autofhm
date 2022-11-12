# AutoML

An automated machine learning tool that performs auto-feature engineering, model selection and hyperparameter optimisation(HPO). This project uses Genetic Algorithm to perform the model selection and HPO.

## Installation

1. `pip install Autofhm` 


## Running 

1. create a configuration file (shown below)
2. `python -m Autofhm -c path/to/config/file ` to generate a model.
   
## To run tests

- Run `python test/test.py` inside the project root folder (This takes a lot of time).
- To build a specific model run `python test/test.py -c {dataset folder name}`. Where the directory is the test datasets folder.
- Results will be stored at [test/results](test/results) with file name same as to the dataset Folder name.
- The format and sample data are shown below (varies based on classification/regression)

|Date Time|accuracy|balanced_accuracy|f1|precision|recall|time to build|
|---|---|---|--|---|---|---|
|2021-06-05 10:03:09 |0.851261054498923|10.907589576871073|2.0325990974167425|22.489063492063487|0.8516438951901327|23.94397735595703|

|Date Time|r^2|mean_squared_error|mean_absolute_error|max_error|explained_variance|time to build|
|---|---|---|--|---|---|---|
|2021-06-05 10:03:09 |0.851261054498923|10.907589576871073|2.0325990974167425|22.489063492063487|0.8516438951901327|23.94397735595703|






