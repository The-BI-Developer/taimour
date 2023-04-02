import benford as bf  # where is this coming from?
import pandas as pd
import statsmodels.api as sm
import researchpy as rp
from statsmodels.iolib.summary2 import summary_col


# Taking numbers from all firms as a whole- FRAUD

# IS

"""REFACTOR"""
data = pd.read_excel("Fraud_Python upload.xlsx", "F-IS")
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


# BS

data = pd.read_excel("Fraud_Python upload.xlsx", "F-BS")
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
# CFS

data = pd.read_excel("Fraud_Python upload.xlsx", "F-CF")
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


# TOTAL(FRAUD)

data = pd.read_excel("Fraud_Python upload.xlsx", "All")
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


# aking numbers from all firms as a whole- NON-FRAUD


# IS

data = pd.read_excel("Clean_Python upload.xlsx", "NF-IS")
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


# BS

data = pd.read_excel("Clean_Python upload.xlsx", "NF-BS")
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


# CFS

data = pd.read_excel("Clean_Python upload.xlsx", "NF-CF")
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
# TOTAL (CLEAN)

data = pd.read_excel("CLEAN_Python upload.xlsx", "All")
data.drop(columns="gvkey", inplace=True)
list_of_lists = data.values.tolist()
flat_list = [item for sublist in list_of_lists for item in sublist]
flat_list = [x for x in flat_list if x != 0]

"""REFACTOR"""

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


###########################################################################
# for t-test
###########################################################################
# taking numbers from individual firms-FRAUD
###########################################


data = pd.read_excel("Fraud_Python upload.xlsx", "F-IS")
data.drop(columns="gvkey", inplace=True)


# list of lists

values_by_company = data.values.tolist()
values_by_company = [x for x in values_by_company if sum(x) != 0]

# create dictionary

company_dict = {}

for i in range(0, len(values_by_company)):
    company_dict[i] = values_by_company[i]
    # Do something with each/all companies e.g.

result_dictionary = {}

for key, value in company_dict.items():
    stats = []

    f1d = bf.first_digits(value, digs=1, decimals="infer", show_plot=False)

    chi = list(bf.stats.chi_sq(f1d, 8, 95))
    ks = list(bf.stats.kolmogorov_smirnov(f1d, 95, len(value), verbose=False))
    mad = bf.benford.mad(value, 1, decimals="infer", sign="all", verbose=False)

    stats.append(mad)
    stats.append(ks[0])
    stats.append(ks[1])
    stats.append(chi[0])
    stats.append(chi[1])

    result_dictionary[key] = stats


resultsF = pd.DataFrame.from_dict(
    result_dictionary, orient="index", columns=["MAD", "KS", "KS_CV", "CHI", "CHI_CV"]
)

F_IS_MAD = resultsF["MAD"]
F_IS_KS = resultsF["KS"]
F_IS_CHI = resultsF["CHI"]


# taking numbers from individual firms-CLEAN
###########################################


data = pd.read_excel("Clean_Python upload.xlsx", "NF-IS")
data.drop(columns="gvkey", inplace=True)


# list of lists

values_by_company = data.values.tolist()
values_by_company = [x for x in values_by_company if sum(x) != 0]

# create dictionary
company_dict = {}

for i in range(0, len(values_by_company)):
    company_dict[i] = values_by_company[i]


# Do something with each/all companies e.g.

result_dictionary = {}

for key, value in company_dict.items():
    stats = []

    f1d = bf.first_digits(value, digs=1, decimals="infer", show_plot=False)

    chi = list(bf.stats.chi_sq(f1d, 8, 95))
    ks = list(bf.stats.kolmogorov_smirnov(f1d, 95, len(value), verbose=False))
    mad = bf.benford.mad(value, 1, decimals="infer", sign="all", verbose=False)

    stats.append(mad)
    stats.append(ks[0])
    stats.append(ks[1])
    stats.append(chi[0])
    stats.append(chi[1])

    result_dictionary[key] = stats


resultsNF = pd.DataFrame.from_dict(
    result_dictionary, orient="index", columns=["MAD", "KS", "KS_CV", "CHI", "CHI_CV"]
)

NF_IS_MAD = resultsNF["MAD"]
NF_IS_KS = resultsNF["KS"]
NF_IS_CHI = resultsNF["CHI"]
# T test_IS_ (FRAUD VS NON-FRAUD)#


rp.ttest(F_IS_MAD, NF_IS_MAD)
descriptives, results = rp.ttest(F_IS_MAD, NF_IS_MAD, equal_variances=False)
print(descriptives)
print(results)


rp.ttest(F_IS_KS, NF_IS_KS)
descriptives, results = rp.ttest(F_IS_KS, NF_IS_KS, equal_variances=False)
print(descriptives)
print(results)

rp.ttest(F_IS_CHI, NF_IS_CHI)
descriptives, results = rp.ttest(F_IS_CHI, NF_IS_CHI, equal_variances=False)
print(descriptives)
print(results)


# taking numbers from individual firms-BS


data = pd.read_excel("Fraud_Python upload.xlsx", "F-BS")
data.drop(columns="gvkey", inplace=True)


# list of lists

values_by_company = data.values.tolist()
values_by_company = [x for x in values_by_company if sum(x) != 0]

# create dictionary

company_dict = {}

for i in range(0, len(values_by_company)):
    company_dict[i] = values_by_company[i]


# Do something with each/all companies e.g.

result_dictionary = {}
for key, value in company_dict.items():
    stats = []

    f1d = bf.first_digits(value, digs=1, decimals="infer", show_plot=False)

    chi = list(bf.stats.chi_sq(f1d, 8, 95))
    ks = list(bf.stats.kolmogorov_smirnov(f1d, 95, len(value), verbose=False))
    mad = bf.benford.mad(value, 1, decimals="infer", sign="all", verbose=False)

    stats.append(mad)
    stats.append(ks[0])
    stats.append(ks[1])
    stats.append(chi[0])
    stats.append(chi[1])

    result_dictionary[key] = stats


resultsF = pd.DataFrame.from_dict(
    result_dictionary, orient="index", columns=["MAD", "KS", "KS_CV", "CHI", "CHI_CV"]
)


F_BS_MAD = resultsF["MAD"]
F_BS_KS = resultsF["KS"]
F_BS_CHI = resultsF["CHI"]


# CLEAN

data = pd.read_excel("Clean_Python upload.xlsx", "NF-BS")
data.drop(columns="gvkey", inplace=True)


# list of lists

values_by_company = data.values.tolist()
values_by_company = [x for x in values_by_company if sum(x) != 0]

# create dictionary

company_dict = {}

for i in range(0, len(values_by_company)):
    company_dict[i] = values_by_company[i]
    # Do something with each/all companies e.g.

result_dictionary = {}

for key, value in company_dict.items():
    stats = []

    f1d = bf.first_digits(value, digs=1, decimals="infer", show_plot=False)

    chi = list(bf.stats.chi_sq(f1d, 8, 95))
    ks = list(bf.stats.kolmogorov_smirnov(f1d, 95, len(value), verbose=False))
    mad = bf.benford.mad(value, 1, decimals="infer", sign="all", verbose=False)

    stats.append(mad)
    stats.append(ks[0])
    stats.append(ks[1])
    stats.append(chi[0])
    stats.append(chi[1])

    result_dictionary[key] = stats


resultsNF = pd.DataFrame.from_dict(
    result_dictionary, orient="index", columns=["MAD", "KS", "KS_CV", "CHI", "CHI_CV"]
)

NF_BS_MAD = resultsNF["MAD"]
NF_BS_KS = resultsNF["KS"]
NF_BS_CHI = resultsNF["CHI"]

# T test_BS_(FRAUD VS NON FRAUD)

rp.ttest(F_BS_MAD, NF_BS_MAD)
descriptives, results = rp.ttest(F_BS_MAD, NF_BS_MAD, equal_variances=False)
print(descriptives)
print(results)

rp.ttest(F_BS_KS, NF_BS_KS)
descriptives, results = rp.ttest(F_BS_KS, NF_BS_KS, equal_variances=False)
print(descriptives)
print(results)

rp.ttest(F_BS_CHI, NF_BS_CHI)
descriptives, results = rp.ttest(F_BS_CHI, NF_BS_CHI, equal_variances=False)
print(descriptives)
print(results)


# taking numbers from individual firms-CF


data = pd.read_excel("Fraud_Python upload.xlsx", "F-CF")
data.drop(columns="gvkey", inplace=True)


# list of lists

values_by_company = data.values.tolist()
values_by_company = [x for x in values_by_company if sum(x) != 0]

# create dictionary

company_dict = {}

for i in range(0, len(values_by_company)):
    company_dict[i] = values_by_company[i]


# Do something with each/all companies e.g.

result_dictionary = {}

for key, value in company_dict.items():
    stats = []

    f1d = bf.first_digits(value, digs=1, decimals="infer", show_plot=False)

    chi = list(bf.stats.chi_sq(f1d, 8, 95))
    ks = list(bf.stats.kolmogorov_smirnov(f1d, 95, len(value), verbose=False))
    mad = bf.benford.mad(value, 1, decimals="infer", sign="all", verbose=False)

    stats.append(mad)
    stats.append(ks[0])
    stats.append(ks[1])
    stats.append(chi[0])
    stats.append(chi[1])
result_dictionary[key] = stats


resultsF = pd.DataFrame.from_dict(
    result_dictionary, orient="index", columns=["MAD", "KS", "KS_CV", "CHI", "CHI_CV"]
)


F_CF_MAD = resultsF["MAD"]
F_CF_KS = resultsF["KS"]
F_CF_CHI = resultsF["CHI"]


# CLEAN
data = pd.read_excel("Clean_Python upload.xlsx", "NF-CF")
data.drop(columns="gvkey", inplace=True)


# list of lists

values_by_company = data.values.tolist()
values_by_company = [x for x in values_by_company if sum(x) != 0]

# create dictionary

company_dict = {}

for i in range(0, len(values_by_company)):
    company_dict[i] = values_by_company[i]


# Do something with each/all companies e.g.

result_dictionary = {}

for key, value in company_dict.items():
    stats = []

    f1d = bf.first_digits(value, digs=1, decimals="infer", show_plot=False)

    chi = list(bf.stats.chi_sq(f1d, 8, 95))
    ks = list(bf.stats.kolmogorov_smirnov(f1d, 95, len(value), verbose=False))
    mad = bf.benford.mad(value, 1, decimals="infer", sign="all", verbose=False)

    stats.append(mad)
    stats.append(ks[0])
    stats.append(ks[1])
    stats.append(chi[0])
    stats.append(chi[1])

    result_dictionary[key] = stats


resultsNF = pd.DataFrame.from_dict(
    result_dictionary, orient="index", columns=["MAD", "KS", "KS_CV", "CHI", "CHI_CV"]
)

NF_CF_MAD = resultsNF["MAD"]
NF_CF_KS = resultsNF["KS"]
NF_CF_CHI = resultsNF["CHI"]


# T test_CF_(FRAUD VS NON FRAUD)

rp.ttest(F_CF_MAD, NF_CF_MAD)
descriptives, results = rp.ttest(F_CF_MAD, NF_CF_MAD, equal_variances=False)
print(descriptives)
print(results)

rp.ttest(F_CF_KS, NF_CF_KS)
descriptives, results = rp.ttest(F_CF_KS, NF_CF_KS, equal_variances=False)
print(descriptives)
print(results)

rp.ttest(F_CF_CHI, NF_CF_CHI)
descriptives, results = rp.ttest(F_CF_CHI, NF_CF_CHI, equal_variances=False)
print(descriptives)
print(results)


# taking numbers from individual firms-All


data = pd.read_excel("Fraud_Python upload.xlsx", "All")
data.drop(columns="gvkey", inplace=True)


# list of lists

values_by_company = data.values.tolist()
values_by_company = [x for x in values_by_company if sum(x) != 0]
# create dictionary

company_dict = {}

for i in range(0, len(values_by_company)):
    company_dict[i] = values_by_company[i]


# Do something with each/all companies e.g.

result_dictionary = {}

for key, value in company_dict.items():
    stats = []

    f1d = bf.first_digits(value, digs=1, decimals="infer", show_plot=False)

    chi = list(bf.stats.chi_sq(f1d, 8, 95))
    ks = list(bf.stats.kolmogorov_smirnov(f1d, 95, len(value), verbose=False))
    mad = bf.benford.mad(value, 1, decimals="infer", sign="all", verbose=False)

    stats.append(mad)
    stats.append(ks[0])
    stats.append(ks[1])
    stats.append(chi[0])
    stats.append(chi[1])

    result_dictionary[key] = stats


resultsF = pd.DataFrame.from_dict(
    result_dictionary, orient="index", columns=["MAD", "KS", "KS_CV", "CHI", "CHI_CV"]
)


F_All_MAD = resultsF["MAD"]
F_All_KS = resultsF["KS"]
F_All_CHI = resultsF["CHI"]


# CLEAN
data = pd.read_excel("Clean_Python upload.xlsx", "All")
data.drop(columns="gvkey", inplace=True)
# list of lists

values_by_company = data.values.tolist()
values_by_company = [x for x in values_by_company if sum(x) != 0]

# create dictionary

company_dict = {}

for i in range(0, len(values_by_company)):
    company_dict[i] = values_by_company[i]


# Do something with each/all companies e.g.

result_dictionary = {}

for key, value in company_dict.items():
    stats = []

    f1d = bf.first_digits(value, digs=1, decimals="infer", show_plot=False)

    chi = list(bf.stats.chi_sq(f1d, 8, 95))
    ks = list(bf.stats.kolmogorov_smirnov(f1d, 95, len(value), verbose=False))
    mad = bf.benford.mad(value, 1, decimals="infer", sign="all", verbose=False)

    stats.append(mad)
    stats.append(ks[0])
    stats.append(ks[1])
    stats.append(chi[0])
    stats.append(chi[1])

    result_dictionary[key] = stats


resultsNF = pd.DataFrame.from_dict(
    result_dictionary, orient="index", columns=["MAD", "KS", "KS_CV", "CHI", "CHI_CV"]
)

NF_All_MAD = resultsNF["MAD"]
NF_All_KS = resultsNF["KS"]
NF_All_CHI = resultsNF["CHI"]
# T test_All_(FRAUD VS NON FRAUD)

rp.ttest(F_All_MAD, NF_All_MAD)
descriptives, results = rp.ttest(F_All_MAD, NF_All_MAD, equal_variances=False)
print(descriptives)
print(results)

rp.ttest(F_All_KS, NF_All_KS)
descriptives, results = rp.ttest(F_All_KS, NF_All_KS, equal_variances=False)
print(descriptives)
print(results)

rp.ttest(F_All_CHI, NF_All_CHI)
descriptives, results = rp.ttest(F_All_CHI, NF_All_CHI, equal_variances=False)
print(descriptives)
print(results)


# Account Type-wise Analysis-BS

# Asset

data = pd.read_excel("Fraud_Python upload.xlsx", "F-BS_Assets")
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


# Liability

data = pd.read_excel("Fraud_Python upload.xlsx", "F_BS-EL")
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


# Account Type wise Analysis-IS

# Income

data = pd.read_excel("Fraud_Python upload.xlsx", "F-IS-Income")
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

# Expense

data = pd.read_excel("Fraud_Python upload.xlsx", "F-IS-Expense")
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


##Single company's level checking##

# TOTAL (CLEAN)

data = pd.read_excel("CLEAN_Python upload.xlsx", "Single Company")
data.drop(columns="company name", inplace=True)
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


###Multivariate Analysis:


# Smaller

data = pd.read_excel("Multi variate.xlsx", "Smaller")
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
# Younger

data = pd.read_excel("Multi variate.xlsx", "younger")
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


# Big

data = pd.read_excel("Multi variate.xlsx", "Big")
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


# Stable
data = pd.read_excel("Multi variate.xlsx", "Stable")
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


# More Volatile
data = pd.read_excel("Multi variate.xlsx", "more volatile")
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


# Growing
data = pd.read_excel("Multi variate.xlsx", "growing")
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
# regression:

# Smaller

data = pd.read_excel("Multi variate.xlsx", "Smaller with MAD")


y = data["MAD Score"]
X = data[
    [
        "invt",
        "Dp",
        "lt",
        "at",
        "re",
        "cogs",
        "ebit",
        "rt",
        "xint",
        "xsga",
        "dpc",
        "fincf",
        "ivncf",
        "oancf",
    ]
]
X = sm.add_constant(X)

reg1 = sm.Logit(y, X).fit()
print(reg1.summary())


# Younger

data = pd.read_excel("Multi variate.xlsx", "Younger with MAD")

y = data["MAD Score"]
X = data[
    [
        "invt",
        "Dp",
        "lt",
        "at",
        "re",
        "cogs",
        "ebit",
        "rt",
        "xint",
        "xsga",
        "dpc",
        "fincf",
        "ivncf",
        "oancf",
    ]
]
X = sm.add_constant(X)

reg2 = sm.OLS(y, X).fit()
print(reg1.summary())


# More Volatile

data = pd.read_excel("Multi variate.xlsx", "more volatile with MAD")

y = data["MAD Score"]
X = data[
    [
        "invt",
        "Dp",
        "lt",
        "at",
        "re",
        "cogs",
        "ebit",
        "rt",
        "xint",
        "xsga",
        "dpc",
        "fincf",
        "ivncf",
        "oancf",
    ]
]
X = sm.add_constant(X)

reg3 = sm.OLS(y, X).fit()
print(reg1.summary())
# Growing


data = pd.read_excel("Multi variate.xlsx", "Growing with MAD")

y = data["MAD Score"]
X = data[
    [
        "invt",
        "Dp",
        "lt",
        "at",
        "re",
        "cogs",
        "ebit",
        "rt",
        "xint",
        "xsga",
        "dpc",
        "fincf",
        "ivncf",
        "oancf",
    ]
]
X = sm.add_constant(X)

reg4 = sm.OLS(y, X).fit()
print(reg1.summary())


# BIG

data = pd.read_excel("Multi variate.xlsx", "Big with MAD")

y = data["MAD Score"]
X = data[
    [
        "invt",
        "Dp",
        "lt",
        "at",
        "re",
        "cogs",
        "ebit",
        "rt",
        "xint",
        "xsga",
        "dpc",
        "fincf",
        "ivncf",
        "oancf",
    ]
]
X = sm.add_constant(X)

reg5 = sm.OLS(y, X).fit()
print(reg1.summary())


# STABLE

data = pd.read_excel("Multi variate.xlsx", "Stable with MAD")

y = data["MAD Score"]
X = data[
    [
        "invt",
        "Dp",
        "lt",
        "at",
        "re",
        "cogs",
        "ebit",
        "rt",
        "xint",
        "xsga",
        "dpc",
        "fincf",
        "ivncf",
        "oancf",
    ]
]
X = sm.add_constant(X)

reg6 = sm.OLS(y, X).fit()
print(reg1.summary())
info_dict = {
    "R-squared": lambda x: f"{x.rsquared:.2f}",
    "Observations": lambda x: f"{int(x.nobs):d}",
}


results_table = summary_col(
    results=[reg1, reg2, reg3, reg4, reg5, reg6],
    float_format="%0.3f",
    stars=True,
    model_names=["Smaller", "Younger", "More Volatile", "Growing", "Big", "Stable"],
    info_dict=info_dict,
    regressor_order=[
        "const",
        "invt",
        "Dp",
        "lt",
        "at",
        "re",
        "cogs",
        "ebit",
        "rt",
        "xint",
        "xsga",
        "dpc",
        "fincf",
        "ivncf",
        "oancf ",
    ],
)

results_table.add_title("Regression Table")

print(results_table)

results_text = results_table.as_text()
filename = "output.txt"
with open(filename, "w") as f:
    f.write(results_text)
