# Bass_Model_HW1
# Bass Diffusion Model Analysis

Welcome to the **Bass Diffusion Model Analysis** project! This repository applies the Bass model to forecast the adoption of LG’s transparent TV, drawing parallels with historical data on TV sales in Germany.

---

## 1. Project Overview
- **Objective**: Estimate the Bass model parameters (p, q, M) using a look-alike innovation’s sales data, then predict how quickly the transparent TV might diffuse in a similar market context.
- **Key Insights**: 
  - **p (Innovation)** measures external influence (marketing, advertising).
  - **q (Imitation)** captures word-of-mouth or social proof.
  - **M (Market Size)** represents the total potential number of adopters.

---
### Key Directories

- **data/**  
  Contains the Excel file `TV2.xlsx`, which holds the time-series data used for the Bass model analysis (e.g., yearly TV sales).

- **Img/**  
  Holds images and plots generated or referenced in the project, such as the Bass model visualization, cumulative adoption curves, and data points.

- **report/**  
  - `report_source.md`: The primary Markdown file that describes the methodology, results, and references.  
  - `report_source.pdf`: The final, compiled PDF report (generated from `report_source.md`).

- **Script/**  
  - `helper_function.ipynb` and `helper_function.py`: Contain functions that assist with data cleaning, model fitting, or plotting.  
  - `Script2.ipynb`: The main Jupyter Notebook where the Bass model is implemented and the analysis is performed.

---

## 2. Setup & Requirements

1. **Python 3.7+**  
2. **Libraries**:  
   - `pandas` (data handling)  
   - `numpy` (numerical operations)  
   - `matplotlib` (visualizations)  
   - `scipy` (curve fitting and optimization)
    - `scipy` (curve fitting and optimization)

Install the dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt

```
## Author 

Mane Koshkaryan