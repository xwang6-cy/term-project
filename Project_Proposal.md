# Project Proposal 

## 1. **The Big Idea:** What is the main idea of your project? What topics will you explore and what will you accomplish? Describe your minimum viable product (MVP) and your stretch goal.

The main idea of my project is to help the user build an investment portfolio with different stocks and projected growth yield. We will explore various different topics we have covered in class such as Flask, loops, and dictionaries. We hope to create a meaningful website that allows users to build a portfolio with ease. The MVP project will be an web application that allows the user to look at different types of stocks or search a stock by its name. With each stock, it will provide a description of the company and shows a growth graph and a button that allows the user to add that stock into their portfolio. Ultimately, the user will be able to submit their portfolio and will be able to see an overview of the portfolio as well as possible projected growth. With a limited amount of time and knowledge, the website will be simplified and the primary stock API we will be focusing on is Yahoo Finance. The amount of data accessible is limited with free public API, the the MVP will be limited with the viable displays and stock information. Our overall stretch goal is to be able to build a functional website with more than just the description and growth. Perhaps we can add diversification evaluation and the overall risk of the portfolio. We can also add other valuations such as P/E or even both short time and long term investments. 

## 2. **Learning Objectives:** Since this is a team project, you may want to articulate both shared and individual learning goals.

Our learning objective is to explore more of different python libraries and methods for stock analysis and graph building. We also wish to get ourselves acquainted with html and API data. The overall objective is to be able to create a fully functional website that we can put in our resume and demonstrate our knowledge and skills that we have learn throughout the course. We want to be able to use these skills and adapt them into our final project. We also believe that it is necessary to use python in our financial field and career. By learning and exploring this field, we will be able to use our python skills in the financial career. 

## 3. **Implementation Plan:** This part may be somewhat ambiguous initially. You might have identified a library or a framework that you believe would be helpful for your project at this early stage. If you're uncertain about executing your project plan, provide a rough plan describing how you'll investigate this information further.

To implement our plan, we first want to explore the possible APIs. One in particular is Yahoo finance API, which has information about most stocks within the past 5-10 years. We want to explore what kind of data will be returned after requesting the API and how can we analyze and store the mass amount of data. Our initial idea is to have the user input the stock ticker symbol and then show a bunch of information of the stock. However, as we have mentioned in class, we are amusing not all users can use the website properly, so we are thinking about having a dropdown menu for all the possible stocks when typing in the letters individually. After the user has inputted the data, we will then send an API request to the data source and pull the information about the stock. The information will then be displayed to the user and if the user wishes to add it to the portfolio, there will be a button that will store such data in a dictionary or using pickling methods. With the given information about the stocks, we will run it through different python libraries for stock analysis. Then we will incorprate those finds as a overall review or summary presented to our users. We will be using presenting the findings through html and our website. We will continue to improve our websites after we have implemented the basic functions and making sure that the program is fully functional. 

## 4. **Project Schedule:** You have 6 weeks (roughly) to finish the project. Draft a general timeline for your project. Depending on your project, you might be able to provide a detailed schedule or only an overview. Preparation of a longer project is also accompanied by present uncertainty, and this schedule will likely require revisions as the project progresses.

4.6 Project Proposal Due 

4.8 Find and experiment with API Keys

4.12 Define the helper functions

4.15 Set up Flask 

4.17 Write HTML 

4.20 Data Storage

4.22 Website test

4.23 Port Forwarding or Make website permanent 

4.24 Project Write-up 

4/25 In class Demo Due 

4.28 Review over final Project before submission 

4.29 Final Submission Due 

## 5. **Collaboration Plan:** How will you collaborate with your teammates on this project? Will you divide tasks and then incorporate them separately? Will you undertake a comprehensive pair program? Explain how you'll ensure effective team collaboration. This may also entail information on any software development methodologies you anticipate using (e.g. agile development). Be sure to clarify why you've picked this specific organizational structure.

We will divide the tasks based on individual strength and preference. Agile development methodology will be used in which we break our project into smaller and manageable tasks in that this approach ensures the flexibility and adaptability of our project and will help complete our project more efficiently and traceable. On the one hand,  Jason will look for the appropriate API keys and build helpers function to import the stock data to display the description of the company. Jason will also be responsible for designing the user interface by using HTML. On the other hand, Jake will be in charge of Setting up the Flask application and defining routes for handling HTTP requests. Jake will also implement data processing and analysis using Python libraries such as Pandas and NumPy. We will undertake a pair programming method to develop algorithms for recommending stocks and creating investment portfolios based on user preferences and risk tolerance. We will also work together to figure out how to store our data by using pickling modules. In order to ensure the efficiency of our work, we will meet regularly every week to catch up with each other and set the deadline for our tasks assigned. We will also take advantage of communication tools such as Slack, Wechat to exchange ideas and solve bottlenecks together. 


## 6. **Risks and Limitations:** What do you believe is the most significant threat to this project's success?

In terms of the risk and limitation, we believe that although API keys will greatly help our project, it also comes with limitations and potential  drawbacks. Most API keys limit the times of request in the given period of time and some APIs have restrictions on the types of data that can be accessed using an API key, which will probably disrupt our workflow. Some API keys might also change for the access. Therefore, it’s necessary for us to test our API keys for its usability before we actually adopt them in our project.

## 7. **Additional Course Content:** What topics do you believe will be beneficial to your project?

We believe we can take advantage of the pickling module as our database to help us store the data of stock information and the record of stock picking process, which will greatly help us to analyze decision-making process and thus optimize our website to improve the user experience. In addition, we’ll utilize the pandas library to import stock data from various sources, such as CSV files or APIs, and perform various calculations and analysis on it. Last but not least, we might use the Yahoo finance API or Alpha vantage API to help us download the historical and real-time stock data. Admittedly, these are just initial ideas of what additional course content can be used to help us to finish this project. We believe more ideas of additional course content will come up as the project starts to progress.







