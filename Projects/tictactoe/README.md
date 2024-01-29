<br/>
<p align="center">

  <h3 align="center">TicTacToe</h3>

  <p align="center">
A Python implementation of the classic Tic-Tac-Toe game with alpha-beta pruning and a GUI.
    <br/>
    <br/>
    <a href="https://github.com/itsskofficial/Python">View Demo</a>
    .
    <a href="https://github.com/itsskofficial/Python/issues">Report Bug</a>
    .
    <a href="https://github.com/itsskofficial/Python/issues">Request Feature</a>
  </p>
</p>

![License](https://img.shields.io/github/license/itsskofficial/Python) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

This project provides an advanced version of the Tic-Tac-Toe game. It features an AI player that uses alpha-beta pruning for efficient decision-making and includes a graphical user interface (GUI) for an enhanced gaming experience.


## Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](htttps://python.org)
* [Streamlit](https://streamlit.io)

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* **pip:**
  
  Ensure you have Python installed, as pip comes bundled with Python distributions.

  ```sh
  # To upgrade pip to the latest version, run:
  python -m pip install --upgrade pip


### Installation

1. **Clone the repo**

    ```sh
    git clone https://github.com/itsskofficial/Python.git
    ```

2. **Enter into the directory**
    ```sh
    cd Projects/TicTacToe
    ```

3. **Install pip packages**

    ```sh
    pip install -r requirements.txt
    ```

4. **Start the Streamlit server**
    ```sh
    streamlit run app.py
    ```

## Usage

The TicTacToe project employs alpha-beta pruning, an optimization algorithm used in game trees, to enhance the efficiency of the AI player's decision-making process. Alpha-beta pruning reduces the number of nodes evaluated in the search tree by intelligently discarding branches that are guaranteed not to affect the final decision.

In the context of Tic-Tac-Toe, the game tree represents all possible moves and outcomes. Alpha-beta pruning ensures that the AI player explores only those branches that are essential for determining the optimal move, significantly reducing the computational effort required for decision-making.

This optimization technique allows the AI player to make strategic decisions in a more time-efficient manner, providing a challenging and responsive gaming experience for players.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the repository a star! Thanks again!

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/itsskofficial/Python/blob/main/LICENSE.md) for more information.

