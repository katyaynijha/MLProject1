echo [$(date)]: "START"

echo [$(date)]: "Creating virtual environment with python version 3.8"

conda create --prefix ./myenv python=3.8 -y

echo [$(date)]: "Activating virtual environment"

source activate ./myenv

echo [$(date)]: "Installing development requirements"

pip install -r requirements.txt

echo [$(date)]: "END"