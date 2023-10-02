# 随缘居 Web Scraping
### Introduction
This code scrapes **the number of users** who are currently online (as the information is provided by the website) from [随缘居](http://www.mtslash.me/forum.php) using selenium and serverless webdriver. 
The reason why I used selenium is because the website has a loading page. I have to wait a few seconds after request is make to the url to scrape the actual content from the website. The code is then uploaded to AWS Lambda so it's executed every hour. The data is then stored in DynamoDB. 

In this documentation, we will build this code from scratch. By the end of the documentation, you will learn how to web scrape using selenium and webdriver. You will also learn how to upload your web scraping code to AWS Lambda, how to run the code at the interval of your preference, and how to store the web scraping data in AWS DynamoDB.

### Steps
1. Watch [this](https://youtu.be/ijyeE-pXFk0?list=PL_GcZFQb3yYjwt-rg7mHob-9ujdsN6B6R) video to create your AWS account, IAM, lambda function and DynamoDB.
2. Follow [this](https://dev.to/awscommunity-asean/creating-an-api-that-runs-selenium-via-aws-lambda-3ck3) document to download selenium and serverless webdriver and upload them as layers on AWS Lambda. Here are a few notes:
    * It's extremely important to do exactly what the instructions do.
    * When creating AWS Lambda function, select the runtime to be python 3.6 or python 3.7. Newer versions of python won't work. 
    * When you creating a layer for AWS Lambda, make sure you selected **the corresponding python runtime**, which is python 3.7 or python 3.6. 
    * If AWS Lambda runs into problem when importing selenium package, make sure your zip file's path is correct, which is selenium/python/lib/<your python runtime version as you have selected on AWS Lambda>/site-packages
    * If you need some extra help at this step, please watch [this](https://youtu.be/FcW-AXsirBE?list=PL_GcZFQb3yYjwt-rg7mHob-9ujdsN6B6R) youtube video.
3. Watch [this](https://youtu.be/Vj_rAWg4UdY?list=PL_GcZFQb3yYjwt-rg7mHob-9ujdsN6B6R) video to learn how to use selenium and write your code on AWS Lambda.
4. Finally, follow [this](https://youtu.be/-8L4OxotXlE?list=PLD_RqipW0-9s-u1HXTglYV8Aam-5P3XLi) video to set up the time inverval to run your lambda function serverlessly.

### Congratulations! You've just used selenium and serverless webdriver on AWS Lambda! 

### Discussion
After data processing, the graph of visitors online / time for SuiYuanJu is here: 
![alt text](https://github.com/b991/SuiYuanJuScraping/blob/main/SuiYuanJuGraph.png)

This graph suggests that at midnight Chinese Standard Time, Sui Yuan Ju website gets the most amount of visitor. Therefore, the best time to publish/update your novel is after 8:00 pm and before midnight in Chinese Standard Time. 

There are also more visitors in Summer (August) than in September, possibly due the start of shcool for students. 

However, the difference between Aug and Sept visitors is much more drastic in Qing Hua Yu (link to see data analysis is [here](https://github.com/b991/QingHuaYuSraping)) than Sui Yuan Ju. This signifies that a nontrivial amount of visitors to Sui Yuan Ju have stable internet access even when school starts. These visitors could be college students as well as professionals in the workforce.

Details for data processing and method discussion can be found in [this](https://github.com/b991/SuiYuanJuScraping/blob/main/SuiYuanJuDataProcess.ipynb) Jupyter Notebook. 


