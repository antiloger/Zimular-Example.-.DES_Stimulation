# Zimula Simulation Project

This project is a Python-based discrete event simulation using the SimPy library. It simulates a system of machines and workflows, and can be used to model and analyze various scenarios.

## Project Structure

- `main.py`: The entry point of the application. It runs the simulation.
- `componets.py`: Contains the definitions of various components used in the simulation, such as machines or workflows.
- `input.py`: Handles input data for the simulation.
- `manage.py`: Manages various aspects of the application, such as configuration or setup.
- `run.py`: Executes the simulation with specific parameters or settings.
- `ZIM/ZGen.py`: Responsible for generating entities for the simulation.
- `ZIM/ZResource.py` and `ZIM/ZStore.py`: Manage resources and storage in the simulation.
- `ZIM/ZContainer.py`: Represents containers with a certain capacity in the simulation.
- `ZIM/charts/charts.py`: Generates charts or visualizations based on the simulation results.
- `ZIM/API/test.py`: Contains tests for the API of the application.

## Installation

To install the project, clone the repository and install the required Python packages:

```bash
git clone https://github.com/yourusername/Zimula.git
cd Zimula
pip install -r requirements.txt
