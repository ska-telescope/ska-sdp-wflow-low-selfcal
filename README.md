# SKA SDP Wflow Low Selfcal
This repository defines a self calibration pipeline for the SKA LOW. It relies on DP3 and WSClean. This repository is currently being set up, and not in a usable state yet.

## Getting started
This project is defined on the basis of this template https://gitlab.com/ska-telescope/templates/ska-python-skeleton ([![Documentation Status](https://readthedocs.org/projects/ska-telescope-templates-ska-python-skeleton/badge/?version=latest)](https://developer.skatelescope.org/projects/ska-python-skeleton/en/latest/?badge=latest))

## Project status
This repository is created in PI18, currently being developed by Team Schaap.

## Usage
TODO (AST-1205)

## Contribute
If you want to contribute to this project, please consult the section below.

The system used for development needs to have Python 3 and `pip` installed.

## Installation
In order to clone and work with this repository, you need to have poetry installed. You can get it with:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - 
```

Clone the repository with its submodules
``` 
git clone --recursive https://gitlab.com/ska-telescope/sdp/ska-sdp-screen-fitting.git
git submodule init
git submodule update  
cd ska-sdp-screen-fitting
```

Enter poetry virtual environment and build the project
```
poetry shell
poetry build && poetry install
```
Now you can use the make instructions of the submodule and run (for example) the tests:
```
make python-build
make python-test
```
You can also format the code with ```make python-format``` and check the linting with ```make python-lint```
