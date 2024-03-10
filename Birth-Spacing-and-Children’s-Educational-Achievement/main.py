import pandas as pd
import statsmodels.formula.api as smf
from linearmodels.iv import IV2SLS
from statsmodels.iolib.summary2 import summary_col

# Load the dataset from a Stata file
file_path = 'dataset_2024.dta'
data = pd.read_stata(file_path)

print(data.head())
print(data.shape)

'''
PART1 OLS model 
Y: Years of Education
X: gap
'''
# Simple OLS (Y: Years of Education)
ols_simple_model = smf.ols('educ_old ~ gap', data=data).fit(cov_type='cluster', cov_kwds={'groups': data['id']})

# Multiple OLS (Y: Years of Education)
formula_1 = '''
educ_old ~ gap + female_old + eduyear_f + eduyear_m + Aborigine + Hokkien + Hakka
+ C(birth_old) + C(order_old) + C(familysize) + pregage_old + pregage_oldsq
'''
# Clustered standard errors are used, with 'id' as the clustering variable
ols_multiple_model = smf.ols(formula=formula_1, data=data).fit(cov_type='cluster', cov_kwds={'groups': data['id']})

# Multiple OLS with interaction terms for control variables (Y: Years of Education)
formula_2 = '''
educ_old ~ gap + female_old + eduyear_f + eduyear_m + Aborigine + Hokkien + Hakka
+ C(birth_old) + C(order_old) + C(familysize) + pregage_old + pregage_oldsq
+ female_old:Aborigine + female_old:Hokkien + female_old:Hakka + female_old:C(familysize)
+ female_old:C(order_old) + C(order_old):C(familysize) + C(order_old):eduyear_f + C(order_old):eduyear_m
'''
# Clustered standard errors are used, with 'id' as the clustering variable
ols_multiple_interaction_model = smf.ols(formula=formula_2, data=data).fit(cov_type='cluster',
                                                                           cov_kwds={'groups': data['id']})

# Combine the results of the three models into a single summary table
results_part1 = summary_col([ols_simple_model, ols_multiple_model, ols_multiple_interaction_model],
                            stars=True,
                            float_format='%0.4f',
                            model_names=['Simple OLS', 'Multiple OLS', 'Multiple OLS w/ Interactions'],
                            info_dict={'R2': lambda x: f"{x.rsquared:.2f}", 'N': lambda x: f"{int(x.nobs):d}"},
                            regressor_order=['gap', 'female_old', 'eduyear_f', 'eduyear_m', 'Aborigine', 'Hokkien',
                                             'Hakka', 'pregage_old'])
print(results_part1)

'''
PART2 OLS model 
Y: Years of Education
X: gap
'''
# Simple OLS (Y: College)
c_ols_simple_model = smf.ols('college_old ~ gap', data=data).fit(cov_type='cluster', cov_kwds={'groups': data['id']})

# Multiple OLS (Y: College)
formula_3 = '''
college_old ~ gap + female_old + eduyear_f + eduyear_m + Aborigine + Hokkien + Hakka
+ C(birth_old) + C(order_old) + C(familysize) + pregage_old + pregage_oldsq
'''
c_ols_multiple_model = smf.ols(formula=formula_3, data=data).fit(cov_type='cluster', cov_kwds={'groups': data['id']})

# Multiple OLS with interaction terms for control variables (Y: College)
formula_4 = '''
college_old ~ gap + female_old + eduyear_f + eduyear_m + Aborigine + Hokkien + Hakka 
+ C(birth_old) + C(order_old) + C(familysize) + pregage_old + pregage_oldsq
+ female_old:Aborigine + female_old:Hokkien + female_old:Hakka + female_old:C(familysize)
+ female_old:C(order_old) + C(order_old):C(familysize) + C(order_old):eduyear_f + C(order_old):eduyear_m
'''
c_ols_multiple_interaction_model = smf.ols(formula=formula_4, data=data).fit(cov_type='cluster',
                                                                             cov_kwds={'groups': data['id']})

# Combine the results of the three models into a single summary table
results_part2 = summary_col([c_ols_simple_model, c_ols_multiple_model, c_ols_multiple_interaction_model],
                            stars=True,
                            float_format='%0.4f',
                            model_names=['Simple OLS', 'Multiple OLS', 'Multiple OLS w/ Interactions'],
                            info_dict={'R2': lambda x: f"{x.rsquared:.2f}", 'N': lambda x: f"{int(x.nobs):d}"},
                            regressor_order=['gap', 'female_old', 'eduyear_f', 'eduyear_m', 'Aborigine', 'Hokkien',
                                             'Hakka', 'pregage_old'])
print(results_part2)


'''
PART3
2SLS model 
X: Gap
IV: Multiple Birth
'''
# 2SLS (Y: Years of Education)
formula_5 = '''
educ_old ~ [gap ~ multibirths] + female_old + eduyear_f + eduyear_m + Aborigine + Hokkien + Hakka
+ C(birth_old) + C(order_old) + C(familysize) + pregage_old + pregage_oldsq
'''
iv_formula_5 = IV2SLS.from_formula(formula=formula_5, data=data)
# Clustered standard errors are used, with 'id' as the clustering variable
tsls_multiple_model = iv_formula_5.fit(cov_type='clustered', clusters=[data["id"]])
# Output model summary
print(tsls_multiple_model.summary)

# 2SLS (Y: College)
formula_6 = '''
college_old ~ [gap ~ multibirths] + female_old + eduyear_f + eduyear_m + Aborigine + Hokkien + Hakka
+ C(birth_old) + C(order_old) + C(familysize) + pregage_old + pregage_oldsq
'''
iv_formula_6 = IV2SLS.from_formula(formula=formula_6, data=data)
# Clustered standard errors are used, with 'id' as the clustering variable
c_tsls_multiple_model = iv_formula_6.fit(cov_type='clustered', clusters=[data["id"]])
# Output model summary
print(c_tsls_multiple_model.summary)
