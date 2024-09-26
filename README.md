# Tuning Halide Ions to Offset Bending in Lead-Based Perovskite Optoelectronic Properties

## Project Overview
This project investigates how the optoelectronic properties of lead-based perovskites (PVKs) can be optimized by tuning the concentration of halide ions to offset the effects of bending curvature (hence the tensile or compressive strain). The research is particularly focused on perovskite applications for solar cells attached to **vehicle surfaces**.

<p align="center">
<img width="869" alt="Screenshot 2024-09-25 at 23 59 55" src="https://github.com/user-attachments/assets/1482a2a8-87fc-434a-bc95-bce74176a1b2">
</p>

## Research Goals
1. **Understand the effect of bending strain on perovskite solar cells**: How tensile and compressive strain influence bandgap energy, charge carrier mobility, and thermal conductivity.
2. **Optimize the performance of perovskites through halide ion tuning**: Adjust halide ion concentrations to mitigate negative effects of strain.
3. **Develop models and simulations**: Simulate the impact of the bending curvature (Gaussian curvature) on the optoelectronic properties of perovskites and propose strain compensation strategies on vehicle surfaces.

## Key Findings
- **Strain Engineering**: Compressive strain increases charge carrier mobility and thermal conductivity by shifting valence band maxima (VBM) upwards, whereas tensile strain degrades performance by shifting VBM downwards. Overall, tensile strain harms the optoelectronic properties of a perovskite, hence the power conversion efficiency (PCE) of a perovskite solar cell (PVK).
- **Compositional Tuning**: Tuning halide ion concentration (Br and I) can offset the effect of the bending curvature by inducing an opposite internal strain, optimizing the performance of the perovskite layer on curved surfaces like vehicles.
- **Simulations**: A series of simulations show how different strain distributions impact perovskite properties and how these can be optimized by varying the halide ion content. These are also done on a vehicle surface apart from just the graphs.

## Features
1. **Finite Element Analysis (FEA) & Partial Differential Equation (PDE) Simulations**: Simulate strain and temperature distribution on flexible perovskites attached to vehicle surfaces.
2. **Material Modeling with Quantum Espresso**: DFT calculations for understanding PVK properties. 
3. **Python Scripts for Data Analysis**: Scripts used to process experimental data, visualize strain effects, and map performance improvements due to halide ion tuning.

## Folder Structure
- `/src/`: Contains the Python and Matlab scripts for running simulations and data analysis.
- `/models/`: Contains the strain-engineering models used in this research.
- `/data/`: Raw and processed data from experiments and simulations.
- `/images/`: Visual results, including strain maps, graphs, and plots.
- `/reports/`: Includes the final project report and the poster.

## Getting Started
To get started with the simulations or analysis:

### Prerequisites
- **Python 3.x** and relevant libraries (`NumPy`, `SciPy`, `Matplotlib`, `Pandas`)
- **Matlab** for FEA and PDE-based strain modeling.
- **Quantum Espresso** for DFT calculations.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/perovskite-strain-engineering.git
   ```
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Running Simulations
- **Matlab Simulations**: Navigate to the `/src/matlab` folder and run the desired script. For example:
  ```matlab
  runStrainAnalysis.m
  ```
- **Python Data Analysis**: Navigate to the `/src/python` folder and run the scripts to process the experimental data:
  ```bash
  python analyze_perovskite_strain.py
  ```

## Results
- **Strain vs. Optoelectronic Properties**: Simulations and experimental results show how curvature impacts the bandgap and charge mobility of lead-based perovskites. These findings were mapped to vehicle surfaces.
- **Halide Ion Tuning**: The project identified the optimal halide ion concentration needed to counteract bending-induced strain, improving solar cell efficiency and stability.

## Future Work
- Expand real-world testing of perovskites under continuous bending and environmental conditions.
- Investigate scalability and industrial manufacturing methods for applying flexible perovskites on curved surfaces like vehicles.
- Look into the perovskite's life cycle to determine its end-of-life applications.

## Acknowledgments
This project was supervised by **Dr. Claire Barlow** and **Dr. Stephanie Adeyemo** at the University of Cambridge, and was completed as part of the **Laidlaw Scholars Program**. I am internally grateful to **Dr. Claire Barlow** for her support and making me finish the project.
Additionally, I am grateful to **Dr. Miloš Dubajić** and **Capucine Mamak** for their help with the samples and hyperspectral imaging data for PL spectra. 

## References
Include relevant research papers and links used in the project.
