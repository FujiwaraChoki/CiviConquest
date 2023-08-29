# CiviConquest

Welcome to CiviConquest! This project simulates a strategy game where players compete to build structures, gather resources, and conquer territories. The game features a GUI interface for interaction and includes an AI opponent.

## ToC

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Game Mechanics](#game-mechanics)
- [AI Advisor](#ai-advisor)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter library
- PIL (Pillow) library
- PyTorch library

### Installation

1. Clone the repository:

   `git clone https://github.com/FujiwaraChoki/CiviConquest.git`
   `cd CiviConquest`

2. Install the required dependencies:

   `pip install -r requirements.txt`

## Usage

To play the CiviConquest, run the main script:

`python main.py`

Follow the prompts and GUI interactions to make decisions, build structures, and conquer territories. The game simulates turns for both the player and AI opponent.

## Game Mechanics

- Players take turns to make decisions, manage resources, and expand their territories.
- Players can choose to build structures, gather resources, or conquer new territories.
- The game's GUI interface displays player information, resources, and territories.

## AI Advisor

The AI opponent is powered by an AI Advisor model. This model suggests actions for the AI player based on its current state, such as resource availability and territory count. The AI's decisions are influenced by probabilities, and the model is trained using reinforcement learning techniques.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
