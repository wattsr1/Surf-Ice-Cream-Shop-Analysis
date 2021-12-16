# Surfs Up! Weather Analysis using SQLite

## Overview

This project is targeted to assess the potential for a proposal to start a surf/ice cream shop on an island in Hawaii.  On of the key factors for the success of this type of business is the weather conditions where the business will be operating.  To validate the business plan, an analysis of the weather data for the area was completed using a database containing the temperature and precipitation data for the area.  To do this analysis an SQLite database was used due to its lightweight structure and ability to be analyized in using Python.  To determine the success of the business plan the analysis will evaluate the temperatures and rainfall between the years 2010 and 2017 to see if the weather trends throughout the year are favorable for the business as it will require warmer temperatures and limited rainy days to ensure consistant revenue from locals and tourists that frequent the beach.

# Results

## Temperature Data

From the analysis completed using the [SQL database]"hawaii.sqlite" which contains the database that contains the relevant data for the area.  Data was extracted from the database using [code]"SurfsUp_Challenge.ipynb" compiled on Jupyter Labs using the SQLalcemy module in Python to conduct queries on the local SQLite database to extract the temperature data for the months of June and December to observed trends over the years.  The query data was converted to a DataFrame that was used to tablulate the data and allow a statistical analysis of the data for June and December which showed the descriptive statistics for both months over the years.  As seen below the analysis of the temperature statistics from the database are shown.

| June Temperature Descriptive Stats | Dec Temperature Descriptive Stats |
|:-------------------------:|:-------------------------:|
| ![June Statistics](/Resources/june_temp_stats.png "June stats") |  ![Dec Statistics](/Resources/dec_temp_stats.png "Dec stats") |



weather data analysis using SQLite for business proposal
