# Crime and Public Safety Data Analysis System

## 1. Project Overview

The Crime and Public Safety Data Analysis System is a Python-based data analysis application designed to process crime-related datasets, perform statistical analysis and generate visual representations of crime patterns.

The system uses a modular architecture to make data loading, preprocessing, analysis and visualization independent and reusable.

**Note:** The dataset used in this project is simulated for academic and educational purposes. It does not represent actual crime statistics.

## 2. Objectives

- Load crime-related data from CSV and JSON files.
- Identify and handle missing values and duplicate records.
- Perform descriptive statistical analysis.
- Generate graphical representations of crime patterns.
- Save cleaned datasets and analysis results.
- Ensure software reliability through automated unit testing.

## 3. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Pytest
- Git and GitHub

## 4. Project Structure

```text
software-development/
│
├── data/
│   └── crime_data.csv
│
├── output/
│   ├── cleaned_crime_data.csv
│   ├── statistical_summary.csv
│   ├── frequency_state.csv
│   ├── frequency_crime_type.csv
│   ├── frequency_area_type.csv
│   ├── crime_type_distribution.png
│   ├── victim_age_distribution.png
│   └── monthly_crime_trend.png
│
├── src/
│   ├── create_dataset.py
│   ├── data_loader.py
│   ├── data_preprocessing.py
│   ├── data_analysis.py
│   ├── data_visualization.py
│   └── main.py
│
├── tests/
│   ├── test_data_loader.py
│   ├── test_data_preprocessing.py
│   ├── test_data_analysis.py
│   └── test_data_visualization.py
│
├── DESIGN_DOCUMENT.md
├── requirements.txt
└── README.md
```

## 5. Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/Megha486/crime-public-safety-data-analysis
```

### Step 2: Navigate into the project directory

```bash
cd software-development
```

### Step 3: Create a virtual environment

```bash
python -m venv .venv
```

### Step 4: Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Running the Application

Execute the following command from the project root directory:

```bash
python src/main.py
```

The system will automatically load the dataset, preprocess the records, perform statistical analysis and generate visualizations.

Generated files are saved in the `output` directory.

## 7. Running Unit Tests

To execute the automated test suite, run:

```bash
pytest -v
```

The project currently contains 21 unit tests covering data loading, preprocessing, statistical analysis and visualization.

## 8. Data Analysis and Outputs

The application generates:

- A cleaned crime dataset.
- Statistical summaries containing mean, median, standard deviation, minimum and maximum values.
- Frequency distributions for categorical attributes.
- A crime type distribution bar chart.
- A victim age histogram.
- A monthly crime trend line chart.

## 9. Testing and Reliability

Pytest is used to verify individual software modules. Tests cover valid inputs, missing files, unsupported formats, missing values, duplicate records, statistical calculations and chart generation.

The current test suite has successfully passed all 21 tests.

## 10. Limitations and Future Scope

- The dataset is simulated and may not reflect real-world crime patterns.
- The current system primarily performs descriptive analysis.
- Future versions can incorporate larger authentic datasets, geographical crime mapping, predictive analytics and interactive dashboards.

## 11. Data Ethics

The project uses simulated and anonymized academic data. No personally identifiable victim information is intentionally included. Any future use of actual crime datasets must respect privacy, data protection requirements, source licensing and responsible interpretation of statistical findings.

## 12. Author

Developed as an academic project for Software Development for Data Science.