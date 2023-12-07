# DSCI510 Final Project:  What Combination of Characteristics of a Ferrari will Allow me to Purchase at the Best Price?
### In this project, I was hoping to solve a fun question using data and see if the results made sense.  Using a linear regression, could I determine what aspects of a Ferrari devalued the car and which aspects added value in order to "build the best value car". 

## Dependencies:  
Make sure to double check the requirements.txt file to import all libraries needed.  You may need to pip install some libraries before they can be imported.  I had to do this with regex.  However, once you solve any installation problems, all the libraries simply are imported and their functions used.  I used Python version 3.9.7 as well as these libraries:
<ul>
  <li>pandas==1.3.4</li>
  <li>seaborn==0.11.2</li>
  <li>scikit-learn==0.24.2</li>
  <li>regex==2021.8.3</li>
  <li>requests==2.26.0</li>
  <li>numpy==1.20.3</li>
  <li>matplotlib==3.4.3</li>
  <li>matplotlib-inline==0.1.2</li>
  <li>beautifulsoup4==4.10.0</li>
  <li>shap==0.11.2</li>
</ul>  

  If Attempting to run my code to obtain the exact same results:  
  Run files in this order:  
  <ol>
    <li>get_clean_data.py **Be aware that this web scraping may take 30 minutes** </li>
    <li>dsci510_final_analysis_submitted.ipynb</li>
  </ol>
  OR
  <ol>
    <li>download clean_data.csv and downloaded_car_dataset.csv</li>
    <li>dsci510_final_analysis_submitted.ipynb</li>
  </ol>

## Project Layout:  
The project layout follows this structure:  
- README.md  *The README*
- requirements.txt  *This is the list of all dependencies needed to run my code*
- data
  - processed
    - clean_data.csv  *This is my scraped data csv containing cleaned data that is used in the dsci510_final_analysis_submitted.ipynb file*
    - downloaded_car_dataset.csv  *This is the comparison data csv containing cleaned data that is used in the dsci510_final_analysis_submitted.ipynb file*
  - raw
    - noncleaned_data.csv  *This is the raw scraped data that I scraped directly before transforming it to its cleaned version*
- results
  - DSCI510 Final Project Write Up Updated.pdf  *This is my final write up explaining my processes/analysis/visualizations a little bit more deeply than below in the read me*
- src
  - dsci510_final_analysis_submitted.ipynb  *This is my ran Jupyter Notebook containing the analysis and visualization code, it created the base images that I use in my Final Project Write Up* 
  - get_clean_data.py  *This is my Python script that I used to gather all my data for the clean_data.csv*


## The Data:
  I gathered my own data by scraping the website: [Autotrader](https://autotrader.com)  and also by downloading a comparison dataset from [Kaggle](https://www.kaggle.com/datasets/hellbuoy/car-price-prediction).[^1]  My goal was to see how my data compared to a known usable dataset that many people have used successfully for a similar usage goal.  I used the BeautifulSoup4 library in Python to scrape the autotrader website for about 2000 cars before cleaning and converting the data to a csv, which was very easy to compare to the downloadable csv from Kaggle.  Initially, I had wanted to scrape more car samples and a wider variety, but the web scraping process is very time consuming and even scraping 2000 could take over 30 minutes.  Another issue I came across was that not every element on a website is scrapable.  Some items were not scrapable using the standard techniques and were locked behind JavaScript objects.  Because of this challenge, in my timeframe, I scraped fewer unique values from the web pages than I hoped for. 
 I had to try and be creative using my outside knowledge to create a few extra variables.  For example, I know that the vast majority of Ferraris are rear wheel drive (rwd), but there are a few models that are all wheel drive (awd).  Using this knowledge, if I could scrape the model name, then I also knew the drivetrain of the car as well and could use it as another feature.   


## My Conclusion:
❗❗ For the Full Conclusion Make Sure to Read DSCI510 Final Project Write Up Updated ❗❗
  
  My conclusion after comparing the two independent datasets is that there are some common themes but they are very different products.  One dataset contains high value luxury commodities and the other has a mix of regular middle value commodities.  Keeping in mind the goal of my project was to try and get a good deal on a car, my strategy would follow some of those themes in each of the datasets.  Based on my findings in the expensive Ferrari dataset, if I was searching for the best Ferrari for my needs, then I would first narrow my search by model name since that is the most important feature, then down the list of features until I am left with a small subset of choices to buy.  In the standard dataset, I would choose a less desired car brand, then a less desired model from there.  It looks like the crucial aspect to choosing an economic car in either dataset is selecting the correct model first.
  <details>
  <summary>The Potential Cheapest Ferrari</summary>
    
<ul>
  <li>Ferrari California</li>  
  <li>Year as low as possible</li>  
  <li>Mileage as high as possible</li>  
  <li>Color</li>  
  <li>8-Speed Automatic Transmission</li>  
  <li>8-Cylinder Turbo Gas Engine</li>  
  <li>Bordeaux Leather Seats</li>  
  <li>Used</li>
  <li>Nero Exterior</li>
</ul>
  
</details>

## Project Skill Goals:
  The main purpose of this project was to strengthen my web scraping and visualization skills.  Through Python, there are many ways to gather specific data for projects, in this class we discussed using APIs, web scraping, and the classic downloading data.  I personally like the concept of web scraping and I have used it before but it is very tricky because websites change and a web scraping script that worked months ago may not even run later.  I took this project as an opportunity to cement my ability to scrape a website and gather specific data that I need to answer a question that I am curious about.  

[^1]: Credit to Manish Kumar's Car Price Prediction Multiple Linear Regression dataset from Kaggle, it was a nice dataset to work with and decently clean data.
