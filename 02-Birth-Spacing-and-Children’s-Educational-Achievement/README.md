# Birth Spacing and Children’s Educational Achievement

## Development Background

This project was conceived during the preparation of my academic paper for submission in 2023. While organizing numerous Stata do-files and adjusting models for my research, I realized the potential of utilizing Python as a tool to assist in organizing regression models and validating the results of quantitative analysis. To leverage Python's machine learning methods (specifically supervised learning) and implement econometric models, I transitioned the statistical and econometric analysis from Stata to Python execution.

## Introduction

My research focuses on the impact of birth spacing on educational achievement. To overcome the limitations of Ordinary Least Squares (OLS) due to endogeneity, this study adopts the Two-Stage Least Squares (2SLS) approach, utilizing twins as an instrumental variable(IV). This method effectively isolates unobservable factors, offering a robust strategy to uncover the genuine effects of birth intervals on educational attainment. 

For more details, please refer to my paper, which has been accepted for publication in *Journal of Social Sciences and Philosophy* and is currently pending release. The original version of the paper is provided here: [Birth Spacing and Children’s Educational Achievement](https://drive.google.com/file/d/1kTNJ33ZTdj0Zj6vdMKC4sJSGzak1uHRs/view?usp=sharing)
In my research, there are two primary explanatory variables: `gap` (birth spacing) and `spacedclose` (whether gap is less than or equal to two years). Given the similarity in regression outcomes between these variables, and to enhance the readability and comprehension of the code, I've chosen to focus exclusively on the `gap` variable in this presentation.

## 2SLS Model

#### **Y: Years of Education**
```math
\begin{align*}

&Gap_i = \alpha_0 + \alpha_1 Multibirth_i + X_s \Gamma + W_i \Phi + Interaction_{is} \Psi + v_{is} \tag{First-Stage}\\

&Educ_{is} = \beta_0 + \beta_1 \hat{Gap_i} + X_s \Lambda + W_i \Sigma + Interaction_{is} \Omega + u_{is} \tag{Second-Stage}

\end{align*}
```

#### **Y: College**
```math
\begin{align*}

    &Gap_i = \alpha_0 + \alpha_1 Multibirth_i + X_s \Gamma + W_i \Phi + Interaction_{is} \Psi + v_{is} \tag{First-Stage}\\

    &College_{is} = \beta_0 + \beta_1 \hat{Gap_i} + X_s \Lambda + W_i \Sigma + Interaction_{is} \Omega + u_{is} \tag{Second-Stage}

\end{align*}
```

$Educ_{is}$ : the dependent variable, where subscript i denotes the ith pair of siblings, and s represents the older or younger sibling within a pair

$College_{is}$ : the dependent variable, whether one has a college degree

$Gap_i$ : the age gap

$\hat{Gap_i}$ : predicted value of ${Gap_i}$ obtained through the first-stage regression

${Multibirth_i}$ : whether being a part of multiple births

$X_s$ : the individual characteristics of sibling s

$W_i$ : the common family characteristics of the ith pair of siblings

$Interaction_{is}$ : interaction terms

$u_{is}$ : error term

$v_{is}$ : error term in the first-stage regression

## About Data

The original data for this study belongs to Academia Sinica. Instead, I provide a version of the data that I have cleaned and prepared for analysis. For those interested in accessing the original data, you can find the procedure and permissions required at [here](https://srda.sinica.edu.tw/browsingbydatatype_result.php?category=surveymethod&type=2&csid=5)

## Analysis Structure

Given the extensive number of regression models analyzed (with older and younger siblings examined separately), and due to their similar structural forms, the provided code focuses solely on the segment pertaining to older siblings.

#### PART 1: OLS Models (Y: Years of Education)

1. **Simple OLS** 
2. **Multiple OLS**
3. **Multiple OLS with Interaction Terms** 

#### PART 2: OLS Models (Y: College)

1. **Simple OLS** 
2. **Multiple OLS**
3. **Multiple OLS with Interaction Terms** 

#### PART 3: 2SLS Models

1. **Y: Years of Education, Multiple** 
2. **Y: College, Multiple** 

## Packages Used

- **Pandas**: Utilized for reading Stata (.dta) files, enabling the initial loading and preliminary handling of the dataset.
- **Statsmodels**: Employed for conducting Ordinary Least Squares (OLS) regression and organizing regression results. This package provides robust statistical methods that facilitate detailed econometric analysis.
- **Linearmodels**: Applied specifically for Two-Stage Least Squares (2SLS) analysis. This package offers advanced econometric techniques, crucial for addressing the endogeneity issues present in this study.