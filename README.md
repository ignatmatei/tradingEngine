# Trading Engine

## Description
This project is a trading engine built with Python and Anaconda. It is designed to execute trading strategies and manage trading operations efficiently. For this limited data from the BVB stock exchange it can predict with ~70% accuracy whether the price will go up or down. 

## Future improvements
 * gather more training data
 * expand the number of layers
 * take more into consideration the variance of the stock

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/ignatmatei/trading-engine.git
    ```
2. Navigate to the project directory:
    ```bash
    cd trading-engine
    ```
3. Create a new Anaconda environment:
    ```bash
    conda create --name trading-env python=3.8
    ```
4. Activate the environment:
    ```bash
    conda activate trading-env
    ```
5. Install the dependencies:
    ```bash
    conda install --file bio-env.txt
    ```

## Usage
1. Ensure the Anaconda environment is activated:
    ```bash
    conda activate trading-env
    ```
2. Run the trading engine:
    ```bash
    python main.py
    ```
## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

