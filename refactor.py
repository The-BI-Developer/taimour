# def 

import pandas as pd
import benford as bf


data = pd.read_excel("clean_company.xlsx", "clean_CFS")
data.drop(columns="gvkey", inplace=True)
list_of_lists = data.values.tolist()
flat_list = [item for sublist in list_of_lists for item in sublist]
flat_list = [x for x in flat_list if x != 0]


f1d = bf.first_digits(
    flat_list,
    digs=1,
    decimals="infer",
    MAD=True,
    chi_square=True,
    KS=True,
    confidence=95,
    show_plot=True,
)

chi = list(bf.stats.chi_sq(f1d, 8, 95))
ks = list(bf.stats.kolmogorov_smirnov(f1d, 95, len(flat_list), verbose=True))
mad = bf.benford.mad(flat_list, 1, decimals="infer", sign="all", verbose=True)

print(mad)
