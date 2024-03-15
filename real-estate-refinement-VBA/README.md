# Real Estate Data Refinement with Excel VBA
## Development Background

During my tenure as a research assistant in university, I contributed to a project aimed at exploring the relationship between housing prices and luxury tax. The technical challenge of this project revolved around processing and cleansing massive datasets derived from two distinct sources: "The Specifically Selected Goods and Services Tax (Luxury Tax)" data from Ministry of Finance and "Actual Price Registration of Real Estate Transactions" data from Ministry of the Interior. These datasets encompassed over a million transaction records, distributed across 440 Excel files from earlier versions, each containing multiple worksheets.

Working with the Excel 97–2003 format (.xls) introduced specific challenges, primarily due to its limitations in handling large datasets. One significant issue was the row limit of 65,536, which proved inadequate for modern data storage needs. Additionally, the slower read and write speeds inherent to these older versions further compounded the difficulty in processing and analyzing the data efficiently.

Without being directed to use any specific programming language or tool, I self-taught Excel VBA and successfully completed the data cleansing and preprocessing task, integrating all data into a single Stata data file for further analysis.

## Introduction

The essence of this project lies in the efficient data cleansing and organization work carried out through Excel VBA. The VBA scripts were designed to autonomously perform multiple tasks, including data filtering, column insertion and modification, worksheet and workbook merging, and saving the cleansed data in new formats. This automation was crucial for overcoming the project's most challenging and significant hurdle: processing the 440 disparate Excel files. The scripts utilize advanced VBA features and functions, such as loop constructs for iterating over arrays of files and worksheets, conditionals for data validation and cleansing. By employing these VBA techniques, I was able to perform the intricate task of merging data from multiple sources. The automation of these processes not only saved invaluable time but also significantly reduced the margin for error in manual handling.

> ***Due to the sensitive and somewhat confidential nature of this governmental data, coupled with the increasingly stringent restrictions on data usage following incidents of data breaches in recent years, I am unable to provide direct access to either the original or any processed datasets. In fact, upon the conclusion of the project, there was a mandate to delete all such data. Therefore, in this project, I can only share the Excel VBA modules that were developed and utilized for data processing.***
## About Data

The project dealt with data from two primary sources:

1. **The Specifically Selected Goods and Services Tax (Luxury Tax)**: This dataset contained tax information on specific goods and services and was integral to studying the relationship between housing prices and luxury tax.
2. **Actual Price Registration of Real Estate Transactions**: Offering detailed records of real estate transactions, including prices, locations, and dates, this dataset served as a vital resource for analyzing fluctuations in housing prices.

The pivotal element in merging these datasets for an in-depth analysis was the utilization of a primary key, specifically the "Land Registry ID". Given the early collection of data and the original data quality issues, the data cleansing work in this project was crucial. It involved not just solving format and quality issues but also accurately integrating data from diverse sources.