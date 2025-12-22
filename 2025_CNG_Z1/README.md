# Conceptual Neighborhood Graphs of Discrete Time Intervals

This repository contains code and visualizations for the IJGI paper "Conceptual Neighborhood Graphs of Discrete Time Intervals."

| | |
|---|---|
| **Authors** | Matthew P. Dube, Brendan P. Hall |
| **Journal** | ISPRS International Journal of Geo-Information |
| **Manuscript** | ijgi-3988820 |

## Project Overview

This project visualizes **42 discretized temporal relations** organized into 8 Allen relation families. The graphs show how relations transition under different operations (translation, isotropic scaling, anisotropic scaling).

## Interactive Figures

Click the links below to view interactive neighborhood graphs in your browser:

| Figure | Type | Interactive Link |
|--------|------|------------------|
| Figure 9 | Translation | [View Interactive](https://brendanphall.github.io/BrendanHall_Research/2025_CNG_Z1/figure_9_interactive.html) |
| Figure 10 | Isotropic | [View Interactive](https://brendanphall.github.io/BrendanHall_Research/2025_CNG_Z1/figure_10_interactive.html) |
| Figure 11 | Anisotropic | [View Interactive](https://brendanphall.github.io/BrendanHall_Research/2025_CNG_Z1/figure_11_interactive.html) |
| Figure 12 | Translation Temporal | [View Interactive](https://brendanphall.github.io/BrendanHall_Research/2025_CNG_Z1/figure_12_interactive.html) |
| Figure 13 | Isotropic Temporal | [View Interactive](https://brendanphall.github.io/BrendanHall_Research/2025_CNG_Z1/figure_13_interactive.html) |
| Figure 14 | Anisotropic Temporal | [View Interactive](https://brendanphall.github.io/BrendanHall_Research/2025_CNG_Z1/figure_14_interactive.html) |

## Repository Structure

```
1D_Raster_Lines/
├── README.md                           # This file
└── Figures/
    ├── README.md                       # Detailed project documentation
    ├── relation_dictionary.md          # 42 relations with codes and families
    ├── Figure_Improvement_Gameplan.md  # Strategy for figure improvements
    ├── edge_lists/                     # Graph edge data (CSV files)
    │   └── New/                        # Updated edge lists with BA data
    ├── Fig_6_isotropic.ipynb           # Isotropic neighborhood
    ├── Fig_7_translation.ipynb         # Translation neighborhood
    ├── Fig_8_anisotropic.ipynb         # Anisotropic neighborhood
    ├── Fig_9_isotropic_temporal.ipynb  # Isotropic temporal
    ├── Fig_10_translation_temporal.ipynb # Translation temporal
    ├── Fig_11_anisotropic_temporal.ipynb # Anisotropic temporal
    ├── Fig_6_isotropic_3D.ipynb        # 3D isotropic visualization
    ├── Fig_6_isotropic_3D_interactive.ipynb # Interactive 3D version
    └── figures_generated/              # Output PNG and HTML files
        └── Interactive/                # Interactive HTML visualizations
```

## Quick Start

```bash
cd 1D_Raster_Lines/Figures
jupyter notebook
```

Open any `Fig_*.ipynb` notebook and run all cells to generate figures.

## Graph Complexity

| Neighborhood | Nodes | Edges | Components | Description |
|--------------|-------|-------|------------|-------------|
| Translation | 74 | 88 | 4 | Size-restricted (simplest) |
| Isotropic | 74 | 144 | 1 | Temporal isotropic scaling |
| Anisotropic | ~42 | ~86 | 1 | Asymmetric scaling (most complex) |

## Dual Encoding System

Each node uses dual encoding for accessibility and clarity:

### Color by Allen Family

| Family | Color | Hex |
|--------|-------|-----|
| Disjoint | Red | #E74C3C |
| Meet | Orange | #F39C12 |
| Overlap | Yellow | #F1C40F |
| Covered By | Green | #2ECC71 |
| Covers | Blue | #3498DB |
| Inside | Purple | #9B59B6 |
| Contains | Pink | #E91E63 |
| Equal | Teal | #1ABC9C |

### Shape by Interior Property

| Shape | Code | Interior Property | Example Relations |
|-------|------|-------------------|-------------------|
| Circle (●) | `'o'` | Both have interior | disjoint, overlap, contains |
| Square (■) | `'s'` | Neither has interior | disjointNoInterior, equalNoInterior |
| Triangle (▲) | `'^'` | A lacks interior | minimalCoveredBy, minimalInside |
| Diamond (◆) | `'D'` | B lacks interior | minimalCovers, minimalContains |

## Features

Interactive visualizations allow you to:
- Hover over nodes to see relation details
- Pan and zoom to explore graph structure
- See the dual encoding system (color + shape) in action
- Compare different neighborhood types side by side

## Key Insights

- **Translation neighborhood** shows structural limitations: small-to-small, large-to-large only (4 isolated components)
- **Scaling neighborhoods** create cross-connections between size groups (single connected component)
- **Anisotropic** is the "Wild West" with 7 possible branches at each step

## Dependencies

- Python 3.x
- networkx
- matplotlib
- pandas
- plotly (for interactive figures)

## Citation

If you use these visualizations, please cite:

```bibtex
@article{dube2025cng,
  title={Conceptual Neighborhood Graphs of Discrete Time Intervals},
  author={Dube, Matthew P. and Hall, Brendan P.},
  journal={ISPRS International Journal of Geo-Information},
  year={2025}
}
```

## Contact

For questions or issues, please contact the authors or open an issue in this repository.
