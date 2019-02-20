# ml-data-generator

A Python script to generate fake datasets optimized for testing machine learning/deep learning workflows using [Faker](https://github.com/joke2k/faker). The script generates test datasets with a deterministic target variable for regression, binary classification, and classification problems (with balanced classes for the latter two types of problems).

These datasets also work well when testing against AutoML approaches, as it has several traps just for that use case. The generated datasets have the following properties which test the limits of ML/DL models:

* Numeric, text, datetime, and categorical input data fields.
* Target variable is calculated nonlinearly, favoring architectures beyond simple linear models.
* Target variable is calculated using explicit interactions effects between input variables.
* Dataset contains fields which have zero contribution to the target field, forcing a model/workflow to learn to discard/ignore those fields.

## Usage

Install the prerequisites pandas and faker:

```shell
pip3 install pandas faker
```

Download the repo, set the number of rows you want to resulting dataset to be in `ml_data_generator.py`, and then run:

```shell
python3 ml_data_generator.py
```

The 3 resulting datasets will be generated into the current directory.

## Fields

* `id`: Record ID.
* `name`: Random name.
* `num1`: Numbers sampled from the standard normal distribution.
* `num2`: Integers sampled between 1 and 100.
* `text1`: Random 10 +/- 40% words.
* `text2`: Random 4 +/- 40% words.
* `cat1`: Integers sampled between 1 and 10. (but it should not be parsed as a numeric field, as the value contributions are not linear!)
* `cat2`: Letters `a, b, c` sampled at unequal proabilities. (`c` is rare and has a high value contribution)
* `datetime1`: Random datetime in 2017-2018.
* `datetime2`: The `datetime1` value, plus a random value between 0 and 72 hours.
* `target`: The objective variable, derived from the other fields.

The fields `id` and `name` have zero contribution to the `target` variable. Make sure your your model doesn't attempt to process them!

The `target` field is the calculated value for regression problems, 0 or 1 for binary classification problems, and 0 - 9 inclusive for classification problems.

## Maintainer/Creator

Max Woolf ([@minimaxir](http://minimaxir.com))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## License

MIT