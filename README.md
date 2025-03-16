# Python Software Engineer Case
> December 2024, Cross Options

## Description
One of our analysts has come up with a new trading strategy that he wants to verify before taking it to the real markets.
To do this you can use a **backtester**, which is a way to check the performance of a trading strategy on historical data.
This gives the user a rough idea what its performance in real/live markets could be like.
In this case you will be building a simple version of a backtester and create some functions that are needed to execute the analysts' strategy.
Before building the backtester we need to have data to work with. 
Yahoo Finance has an open API for which a Python package has been implemented called [yfinance](https://pypi.org/project/yfinance/).
The `yfinance_1min_data_example.py` script inside the `scripts/` folder shows a basic example of fetching data using the `yfinance` package.
Note that this is a basic example which only fetches 5 days worth of 1-minute interval data, for the case you will need more data.

The idea of the analyst is as follows:
1. Whenever the S&P 500 Future (the E-mini future with ticker symbol `ES=F`) has a 5-minute rolling momentum of > `0.0005` we buy the S&P 500 index and if its < `-0.0005` we sell the index.
   1. NOTE: technically you cannot directly buy the S&P500 index but for this case we will assume you can
   2. We define momentum as $(X_n - X_{n-1})/X_n$ with $X_n$ the average of the current window at time step $n$ and $X_{n-1}$ the average of the previous window
2. After taking the long/short position, close it (e.g. sell when long or buy back when short) again after 10 minutes
3. Assume a fixed commission of \$2, so buying the S&P 500 index twice costs you \$4, selling it 3 times, \$6. Your starting portfolio is $100,000.0
4. Shorting takes up 50% of the notional value of your portfolio. So when you start with \$100K and short the S&P once when its at \$5000, you are left with \$97.5K to trade with

To check the performance of this strategy we ask you to finish the basics of the simple backtester created in `src/backtesting/backtester.py`.
We have added further hints on how to structure the project by giving you some structure already but note that this is still very simple.

We ask you to complete the following tasks:
1. Fetch 2 weeks of 1-minute interval S&P 500 index and future data
2. Implement the simple backtester by looping over the fetched dataframes
   1. Loop over the data in 1 minute steps making sure to update both the future and index data, align the time steps
3. Implement the necessary functions, objects and classes to complete the backtester
   1. You cannot use any functions built into Pandas to create statistics, only to store and load data
4. Track all your trading activity and show a live output of executed trades plus a summary at the end of each day
5. Compute relevant statistics for the trading strategy after running it on the entire 2 weeks
6. Create documentation on how to run your code, make sure it runs!

As you will see from these requirements, we have left it open and up to you to define what you are going to build.
For example the trading strategy statistics, we like to see you do some research and find for yourself what statistics will be useful.
To give you some direction; at least include the expected profit/loss per trade, number of winners, number of losers, geometric profit/loss per trade etc.
We also encourage you to expand upon the given structure and requirements yourself to fully showcase your abilities as a Python developer!

## Requirements
- Use Python 3.10
- Use a **private GitHub** repository
- Document your classes, methods and code in general (use 1 docstring format throughout)
- Adhere to [PEP8](https://peps.python.org/pep-0008/) standards
- Implement all methods to compute statistics for the strategy yourself without external packages
- Use Object-Oriented Programming (OOP)
- Add time and memory complexity estimates for the strategy related statistics

## Evaluation Criteria
- Code design & structure
- Documentation
- Performance of code 
- Knowledge of latest Python best practices

## Submission
When done, please add `gijspaardekooper` as a user to your **GitHub** repo and send an email to gijs.paardekooper@crossoptions.nl with the subject 'Case Submission Python Software Engineer - November 2024'.
Make sure to merge branches to the `main` branch before the deadline as we will be taking the last commit before then as the one to base our evaluation on.

## Getting Started
### 1. Setting up the environment
To get started on the assigment, you will need the following installed on your PC:
- [Python 3.10](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer): package manager for Python to ensure consistency in package versions

NOTE: on some Windows systems using Poetry can be tricky, in that case just directly install the Python packages in the `tool.poetry.dependencies` section of the `pyproject.toml` file (skipping `pyhton`).

Then we want to create and activate a new virtual environment (commands are for Unix systems, change for Windows accordingly):
```shell
python3.10 -m venv .venv3.10
source ./.venv3.10/bin/activate
poetry install --sync
```

### 2. Verify Installation
You can verify if the setup was successfull by running `poetry run python scripts/yfinance_1min_data_example.py` which should create two CSV files in the `data/` folder.

The `yfinance_1min_data_example.py` script inside `scripts/` shows a basic example of fetching data using the `yfinance` package.
Note that `^GSPC` is the ticker symbol used to denote the S&P 500 **Index** on Yahoo Finance, whereas the ticker symbol `ES=F` denotes the S&P 500 **Future**.

### 3. Good Luck!
Spend some time carefully going over the details of this case, researching unknown terms and then start designing your solution!
The case has specifically been created to be open to own ideas and extra features, if you have an idea that would improve the trading strategy or code, we encourage you to add this.
