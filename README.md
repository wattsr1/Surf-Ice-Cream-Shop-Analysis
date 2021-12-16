# Surfs Up! Weather Analysis using SQLite

## Overview

This project is targeted to assess the potential for a proposal to start a surf/ice cream shop on an island in Hawaii.  One of the key factors for the success of this type of business is the weather conditions where the business will be operating.  To validate the business plan, an analysis of the weather data for the area was completed using a database containing the temperature and precipitation data for the area.  To do this analysis an SQLite database was used due to its lightweight structure and ability to be analyzed in using Python.  To determine the success of the business plan, the analysis will evaluate the temperatures and rainfall between the years 2010 and 2017 to see if the weather trends throughout the year are favorable for the business as it will require warmer temperatures and limited rainy days to ensure consistent revenue from locals and tourists that frequent the beach.

---

# Results

## Temperature Data

From the analysis completed using the [SQL database]("hawaii.sqlite") which contains the database that contains the relevant data for the area.  Data was extracted from the database using [code]("SurfsUp_Challenge.ipynb") compiled on Jupyter Labs using the SQLalcemy module in Python to conduct queries on the local SQLite database to extract the temperature data for the months of June and December to observed trends over the years.  The query data was converted to a DataFrame that was used to tabulate the data and allow a statistical analysis of the data for June and December which showed the descriptive statistics for both months over the years.  As seen below the analysis of the temperature statistics from the database are shown.

| June Temperature Descriptive Stats | Dec Temperature Descriptive Stats |
|:-------------------------:|:-------------------------:|
| ![June Statistics](/Resources/june_temp_stats.png "June stats") |  ![Dec Statistics](/Resources/dec_temp_stats.png "Dec stats") |

From the descriptive statistics obtain for the temperatures in June and December the following observations can be made:
1. Little variation of the temperatures between June and Dec
  - only a 3.9-degree F variation in the means of between the months.  
2. Similar standard deviations of the temperatures
  - June having a SD of 3.25 degrees F 
  - December having a SD of 3.75. 
3. December showed a lower minimum temperature of 59 degrees 
  - Maximum temperatures seen in both months are similar
    - 83 degrees F for Dec and 85 degrees F for June. 

This suggests that there are minimal differences between the temperatures in June and December.  To further visualize this a graphical representation of average temperatures for June and December are shown below. It should be noted that the data from December 2017 is missing in the database.

<img src="/Resources/june_dec_ave_temps.png" width="600" height="400">

To illustrate the yearly trends in the temperatures in the area, the average temperatures per month between 2010 and 2017 were extracted from the database.  From that a dataframe and graph showing the average temperature by month was created to show the yearly tends in temperatures.

<img src="/Resources/monthly_avg_temp.png" width="600" height="400">
  
From this graph we can see that the peak temperatures are in July and August and the coolest month is January, however there is minimal variation to the overall temperature in the area.

## Precipitation Data

As mentioned earlier, the precipitation in the area will also have an impact on the volume of business that can be expected to use the surf/ice cream business model.  Like the analysis done on the temperature for the area, the precipitation for the area was also analysed to see if there will be an impact on the business.  Below are the descriptive statistics for the rainfall in June and December for the area.  

| June Precipitation Descriptive Stats | Dec Precipitation Descriptive Stats |
|:-------------------------:|:-------------------------:|
| ![June Statistics](/Resources/prcp_june_stats.png "June stats") |  ![Dec Statistics](/Resources/prcp_dec_stats.png "Dec stats") |

From the descriptive statistics obtain for the precipitation in June and December the following observations can be made:
1. Little variation of the precipitation between June and Dec
  - only a 0.08-inch difference in mean rainfall between the months.  
2. The Dec standard deviation higher for precipitation
  - June having a SD of 0.33 inches. 
  - December having a SD of 0.54 inches. 
3. December showed a higher maximum rainfall of 6.42 inches vs 4.43 inches in June 59. 
  - Based on the low mean for both months these high rainfall events are rare
    - Minimal variation between the rainfall data for these months

From the analysis above it suggests that there is generally little variation between the precipitation observed in June and December.  To further illustrate this a graph showing the average rainfall in June and December in the years ranging from 2010 to 2017 is shown in the graph below.  It should be noted that the rainfall in December of 2010 was significantly higher that that observed in the other years and that there is no recorded data for the rainfall in December of 2017.

<img src="/Resources/june_dec_avg_rainfall.png" width="600" height="400">

To illustrate the yearly trends in the rainfall in the area, the average amount of rain per month in inches for the year 2010 and 2017 were extracted from the database.  This data was used to create a dataframe and graph showing the average precipitation by month was created to show the yearly tends of the rainfall in the area.

<img src="/Resources/prcp_avg_monthly.png" width="600" height="400">

---

# Summary

The weather data analysed from database gives us a clear view of the temperature and rainfall for the area where the business planning to operate.  Based on the finding there is a strong case that the weather will have minimal impact on the success of the business.  The area has minimal variation in temperatures and rainfall observed over the 8 years of data analyzed.  As with weather data anywhere there is evidence of extreme events which is seen in the minimum and maximum values, however the similar standard deviations and means observed in the statistics presented suggest that these events are the exception not the rule.  Looking at the overall yearly trending data for rainfall and temperatures, the trends for higher temperatures between the months in June and October are evident however the rainfall is generally consistent over the year with March and December having the highest average rainfall throughout the year.  It should be noted however the at variations between the warmest and coolest months is minimal with a 7.7-degree difference in the average temperatures of the hottest month (Aug) and the coolest month (Jan).  Similarly, there is only a difference of 0.08 inches in rainfall between the wettest month (Dec) and the driest month (June).  This shows the consistency in the weather in the area and will have minimal impact on volume of the business that would utilize the services offered at the surf/ice cream shop.

---
