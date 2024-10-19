# @title INDIVIDUAL LOCUS WITH 3 ALLELES PERMUTATIONS, FIXED LOCI, pos_prob3 = prob3 / (1 - prob1 - prob2).
# P(6,3)=6!/(6-3)!=120
import pandas as pd
from itertools import permutations

# Define the parent alleles and their original transmission probabilities
# alleles_p1 represents the alleles from Parent 1, and alleles_p2 represents the alleles from Parent 2
# Each list contains different alleles that the parent can transmit to the offspring
alleles_p1 = ["a1", "a2", "a3"]
alleles_p2 = ["aa1", "aa2", "aa3"]

# Original transmission probabilities for each parent's alleles
# probs_p1 and probs_p2 represent the probabilities that each allele from Parent 1 or Parent 2 will be passed on
# These probabilities should sum to 1 across all alleles of a given parent to represent a complete distribution
probs_p1 = [0.3, 0.15, 0.05]
probs_p2 = [0.3, 0.15, 0.05]

# Generate all possible sequences using permutations
# allele_combos stores all possible ways to combine 3 alleles from the combined list of Parent 1 and Parent 2 alleles
# The order of alleles matters, and no allele is repeated in each combination, reflecting unique inheritance scenarios
allele_combos = list(permutations(alleles_p1 + alleles_p2, 3))

# Function to map an allele to its original transmission probability
# get_prob takes an allele and returns its corresponding transmission probability from the respective parent
# This function ensures that each allele is correctly mapped to its original likelihood of being transmitted
def get_prob(allele):
    # Map each allele to its corresponding probability from Parent 1 or Parent 2
    if allele in alleles_p1:
        return probs_p1[alleles_p1.index(allele)]
    elif allele in alleles_p2:
        return probs_p2[alleles_p2.index(allele)]
    return 0  # Safety fallback to handle unexpected input, though it should not occur in this context

# Create a DataFrame with the allele combinations
# df is used to store each allele combination and associated calculations for easier manipulation and analysis
df = pd.DataFrame(allele_combos, columns=["Locus1", "Locus2", "Locus3"])

# Add the original transmission probabilities for each allele at its respective locus
# The probabilities are added as separate columns (Prob_Locus1, Prob_Locus2, Prob_Locus3)
# These columns store the likelihood that each allele in the combination was inherited from its parent
df["Prob_Locus1"] = df["Locus1"].apply(get_prob)
df["Prob_Locus2"] = df["Locus2"].apply(get_prob)
df["Prob_Locus3"] = df["Locus3"].apply(get_prob)

# Function to calculate position-based probabilities dynamically
# calc_pos_probs calculates the adjusted probability of an allele being in a specific position, considering previous selections
# This reflects the conditional probability of inheriting an allele given that earlier alleles in the sequence have already been chosen
def calc_pos_probs(row):
    # Extract the transmission probabilities from the row
    prob1 = row["Prob_Locus1"]  # Probability that the allele in Locus1 was inherited from its parent
    prob2 = row["Prob_Locus2"]  # Probability that the allele in Locus2 was inherited from its parent
    prob3 = row["Prob_Locus3"]  # Probability that the allele in Locus3 was inherited from its parent

    # Calculate position-based probabilities with precise logic
    pos_prob1 = prob1  # The probability for the first position is simply the original transmission probability
    pos_prob2 = prob2 / (1 - prob1)  # Adjusted probability for the second position, given the first allele is already chosen

    # Ensure the denominator is correct for the third position probability
    # The third position is calculated based on the fact that both previous alleles have already been chosen
    pos_prob3 = prob3 / (1 - prob1 - prob2)

    # Return the calculated position-based probabilities
    return pd.Series([pos_prob1, pos_prob2, pos_prob3])

# Apply the function to compute the positional transmission probabilities
# This adds three new columns to df (Pos_Prob1, Pos_Prob2, Pos_Prob3), representing the adjusted probabilities at each position
df[["Pos_Prob1", "Pos_Prob2", "Pos_Prob3"]] = df.apply(calc_pos_probs, axis=1)

# Calculate the total sequence transmission probability as the product of all position-based probabilities
# Total_Prob represents the overall probability of the specific combination of alleles being transmitted
# This value is obtained by multiplying the position-based probabilities for each locus
df["Total_Prob"] = df["Pos_Prob1"] * df["Pos_Prob2"] * df["Pos_Prob3"]

# Display the first 10 rows for verification
# Output is limited to the first 10 rows to provide a snapshot of the allele combinations and their associated probabilities
print("Allele Combinations with Position-Based Transmission Probabilities:")
print(df.head(10))  # Display only the first 10 rows for brevity

# Save the DataFrame to a CSV file if needed
# This allows the results to be saved for further analysis or record-keeping
# df.to_csv("allele_combos_with_pos_probs.csv", index=False)
