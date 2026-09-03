# Project eClipseBord for FastlyDep

eClipseBord is a project with the purpose to use several techstacks to a fullstack application for deployment. The end product will be a deployed dashboard with data about lunar eclipses

## First step EDA
Exploratory Data Analysis (EDA) is used to understand the data before you start working with it. For example you can look at how many rows of data there is, what columns there are and what kind of data you have to work with.

## Tech stacks for the project

### Data Processing
- **Pandas** - Data manipulation and analysis


### Backend

- **Python** - programming language

- **FastAPI** - REST API framework for handling GET requests and retrieving specific data 


### Frontend

- **Streamlit** - Interactive dashboard for data visualization

- **HTTPX** - HTTP client for making GET requests to the FastAPI backend endpoints


### DevOps & Automation

- **Docker** - Containerization with two separate containers:
    - **Frontend container** - Streamlit app with all dependencies
    - **Backend container** - FastAPI with data processing
    - Enables independent updates of frontend and backend


### Infrastructure & Cloud

- **Azure** - 


## Want to try it out?

### Start with cloning the repo and sync the virtual environment
- In terminal (e.g. in git bash)
```bash
# Go in to your selected folder
git clone https://github.com/Anja-Sche/eClipseBord-FastlyDep_Anja_Scherwall.git
```
- Open the project in your code editor (I use VS Code)
- Open the terminal in the editor and run:
```bash
# Set up virtual environment and install all dependencies
uv sync --all-packages
```


### Run locally
- Open two terminals and run:
```bash
# Backend
cd backend
uv run uvicorn api:app --reload

# Frontend (in a new terminal)
cd frontend
uv run streamlit run dashboard.py
```

### Run with Docker
- Open Docker Desktop

- Stand in rootfolder in terminal and run:
```bash
# Build and start all containers
docker compose up -d --build

# Stop all containers
docker compose down
```