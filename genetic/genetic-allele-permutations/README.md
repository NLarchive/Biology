# Genetic Allele Permutations with Fixed Loci

## Overview

This repository models how different alleles (variants of a gene) are arranged across three fixed loci (positions on a chromosome). By using permutations, the project explores how these alleles may combine across loci, considering their respective probabilities.

## Features

- **Permutation Calculation:** Generates all possible sequences of alleles across three loci using permutations.
- **Probability Mapping:** Assigns and calculates the probability of each allele at each locus.
- **Dynamic Probability Adjustment:** Adjusts probabilities based on previously selected alleles, simulating conditional probabilities.
- **Data Visualization:** Outputs the combinations and their probabilities in a structured format.

## Technologies Used

- Python 3.x
- Pandas
- itertools

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- `pip` package manager.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/NLarchive/genetic-allele-permutations.git
   cd genetic-allele-permutations
