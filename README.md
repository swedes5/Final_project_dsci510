# DSCI510 Final Project: How to get the Best Deal on a Ferrari
### In this project, I was hoping to solve a fun question using data and see if the results made sense.  Using a linear regression, could I determine what aspects of a Ferrari devalued the car and which aspects added value in order to "build the best value car". 

## The Data:
  I gathered my own data by scraping the website: [Autotrader](https://autotrader.com) and also by downloading a comparison dataset from [Kaggle](https://www.kaggle.com/datasets/hellbuoy/car-price-prediction).  My goal was to see how my data compared to a known usable dataset that many people have used successfully for a similar usage goal.  I used the BeautifulSoup4 library in Python to scrape the autotrader website for about 2000 cars before cleaning and converting the data to a csv, which was very easy to compare to the downloadable csv from Kaggle.  Initially, I had wanted to scrape more car samples and a wider variety, but the web scraping process is very time consuming and even scraping 2000 could take over 30 minutes.  Another issue I came across was that not every element on a website is scrapable.  Some items were not scrapable using the standard techniques and were locked behind JavaScript objects.  Because of this challenge, in my timeframe, I scraped fewer unique values from the web pages than I hoped for. 
 I had to try and be creative using my outside knowledge to create a few extra variables.  For example, I know that the vast majority of Ferraris are rear wheel drive (rwd), but there are a few models that are all wheel drive (awd).  Using this knowledge, if I could scrape the model name, then I also knew the drivetrain of the car as well and could use it as another feature.   

## My Analysis:
  To determine which characteristics of a car would be costly or cheap, I decided to try  using a linear regression using the price as the dependent variable and other characteristics as independent variables.  My hope was that if I can break down each individual contribution of a characteristic, then I may be able to determine what I want to search for when I filter my results.  For example, if I know a few characteristics, can I use my model's results to search for the best Ferrari for me? EX: I just need any Ferrari, the cheapest possible: what combination of paint, seat color, model, etc will best match my needs? 
  My findings were that the model name is the most important variable typically, some older models such as a 360 Modena lowered the value in the model's eyes.  However some "rare" models, such as a 360 Modena Challenge Stradale, with only about 1200 models made, were very expensive and this model name increases value heavily.  However, when comparing my data for a brand such as Ferrari to the more regular data for standard car brands from Kaggle, I saw that the linear model values different categories.  In the normal car data, it appears that a high value independent variable is actually the brand.  For example, 'isBMW == True' contributes a high gain to value.  This leads me to believe that the categorical variable of brand or model name is very important to price.  Another potentially interesting analysis could be to split up each dataset by brand, and even more by model as well if a person cares more about more mechanical things instead of name branding.  My conclusion is that the most important features from my Ferrari dataset were typically model names, which makes sense because from my outside knowledge of Ferraris, there are some models that are extremely rare and highly exclusive which drive up a high price and there are some models that are produced more heavily as an "entry level Ferrari" with a lower exclusivity and value.  Compared to the standard car dataset, there are more "mundane" important variables such as curb weight, fuel type, and number of cylinders.

## My Visualizations:
  I made a few easy to interpret visualizations displaying the top 10 features that contribute to low value Ferraris and as well for the high value Ferraris.  The bar plots are very straight to the point with the x axis as the linear regression coefficient names and the y axis as the value that each of those coefficients has and when combined with the intercept will sum to the car's predicted price.  I also included the regression line using Matplotlibs regplot function which shows the predicted test points and the regression line that best follows those plot points. To further explain the linear model, I used SHAP values which try to explain each variables individual contribution to the model's prediction by emphasizing importance of each variable.

## My Conclusion:
  My conclusion after comparing the two independent datasets is that there are some common themes but they are very different products.  One dataset contains high value luxury commodities and the other has a mix of regular middle value commodities.  Keeping in mind the goal of my project was to try and get a good deal on a car, my strategy would follow some of those themes in each of the datasets.  Based on my findings in the expensive Ferrari dataset, if I was searching for the best Ferrari for my needs, then I would first narrow my search by model name since that is the most important feature, then down the list of features until I am left with a small subset of choices to buy.  In the standard dataset, I would choose a less desired car brand, then a less desired model from there.  It looks like the crucial aspect to choosing an economic car in either dataset is selecting the correct model first.
  <details>
  <summary>Spoiler warning</summary>
  
  The Cheapest Ferrari Build:  
    
  Ferrari California  
  Year as low as possible  
  Mileage as high as possible  
  Color  
  8-Speed Automatic Transmission  
  8-Cylinder Turbo Gas Engine  
  Bordeaux Leather Seats  
  Used
  Nero Exterior
  
  
</details>

## Project Skill Goals:
  The main purpose of this project was to strengthen my web scraping and visualization skills.  Through Python, there are many ways to gather specific data for projects, in this class we discussed using APIs, web scraping, and the classic downloading data.  I personally like the concept of web scraping and I have used it before but it is very tricky because websites change and a web scraping script that worked months ago may not even run later.  I took this project as an opportunity to cement my ability to scrape a website and gather specific data that I need to answer a question that I am curious about.  
