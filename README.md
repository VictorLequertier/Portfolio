# Projects Portfolio

### In this portfolio you can find the code I worked on for the following projects:

#### - Master Thesis - Wnowledge Graphs for fake news detection on social media - Msc DAAI EDHEC Business School 2022

From the Master Thesis's abstract:
_The last decade has been strongly marked by the emergence of social media, a new vector of information allowing them to spread faster and wider. This new era have seen the emergence of a new challenge for researchers and data scientists: Detecting fake news before they wildly spread.  Since then, multiple techniques of Natural Language Processing and Natural Language Understanding were put to the test with a measured success rate. On the edge of the NLP domain stands a particular text representation: Knowledge Graphs. Most specifically, in this research I’ll focus on a particular document representation method: Subject-Predicate-Object triplets forming. Even though some recent studies starts using KG to perform classification of fake news [13], most of them rely on using on the usage of existing knowledge bases. That study aims to build an ad-hoc KG from fake news labelled dataset to addressing the issue of extracting valuable data from the KG characteristics and use them to classify the reliability of news._

The complete documented code is available in a nodebook. Through this thesis I used various NLP and Knowledge Graphs python techniques from the Stanford NLP Stanza pipeline to the python Networkx library.
The original dataset can be found on Kaggle : https://www.kaggle.com/datasets/shivkumarganesh/politifact-factcheck-data
The intermediate "checkpoints datasets", extracted fom the python code make it possible to run parts of the code only. These datasets are available in this github inside the _politifact_data_ folder 


#### - Business Data Management EDHEC course project - 2022

The first goal of this project was to perform clustering on the SMCP group (Sandro, Maje, Claudie Pierlot and Fursac clothing brands) items regarding their characterstics. In a second time, we used this clustering and previous sales informations to perform sales forecasting predictions.

For this project we used snowflake for all data management and most of the data preparation process and python code for the data analysis and machine learning.



#### - Data Science project for business EDHEC course project - 2022

In this project, we studied the political extreme voting tendency relationship with European Social Survey (ESS) answers. The goal was to cluster if the respondent were likely or not to vote for an extreme political party in the 2022 elections regarding their answers to this survey. Most importantly, the goal was to make a consistent statistical analysis of the variables and models to ensure their statistical reliability.


#### - Data Mining for EDHEC final assignement - 2021

This notebook is the final assignment of Data Mining which covers multiple areas of data mining such as constrained optimisation (scipy), outliers detection, principal components analysis, prediction and cross validation techniques


### All other projects I worked on are subject to confidenciality so I can't report the code from those. Nonetheless, here is a written description of these projects: 


#### - Detection of Fake News on Twitter using Knowledge graphs - EDHEC Msc DA & AI Master thesis (I will likely upload the code by the end of June)
The aim of this master thesis is to perform fake news detection on social medias, and especially on Twitter. 
I am using Knowledge Graphs built on fake news posts corpus to cluster suspicious news on social media. Research entirely done in Python using NLP and Nodes embedding pipelines. The graphs' embedded outputs are then sent through machine learning algorithms to perform classification. 


#### - Web Scrapping of various clothing brands websites - Freelance mission
Building different Scrapy spiders to scrap items from different clothing brands websites and marketplaces

#### Creation of a “Natixis Payment Observatory” (30B€ transactions monitoring) on power BI - Natixis Payments 
Constitution of the data model and analysis of more than 30 billion € of BPCE group’s financial transactions.Dynamic analysis and visualizations to allow a top management monitoring and to enhance the commercial opportunities of Natixis partner subsidiaries.

#### Constrained optimization of the BPCE group’s property portfolio relocation process - BPCE Group
Within a team of 5 people. This one week Datathon aimed at optimizing the relocation path of BPCE teams to the new real estate portfolio while minimizing the carbon footprint and the logistic and manpower disturbances.Two ML different approaches tried: Constrained linear optimization model and reinforcement learning.

#### ML scoring of BPCE clients appetency to delegate their financial portfolio management - Natixis Investment Managers 
Realization of a scoring in python to measure BPCE customers appetency of delegating the management of their active savings portfolio to a BCPE manager.
Building ML model from a brute 14M rows dataset of clients banking informations

####  Building a Microsoft Azure ELT pipeline to perform real-time analysis on payments flows - Course Croisière EDHEC 

This project aimed to analyse in real time 200k€ cashless payments from the Course Croisière EDHEC 1-week event, to extract business insights and boost the performances of the event.
Bulding from scratch an ELT architecture on Microsoft Azure, using Azure Data Factory and Azure Analysis Services.

#### Development of a click and collect web application - Course Croisière EDHEC

Development of a click and collect application allowing Course Croisière EDHEC participants to order snacks and beverages from their phone. 
Search for fundings, design of the specifications and of the UX model (on Adobe XD) and supervision of the development in collaboration with 3 consultant developers.

#### Cellular automata in Python - Modelling propagation of epidemics in cities - TIPE of CPGE MP Stanislas Cannes 

Modelling the spread of epidemics in urban areas using a custom Cellular Automata. Creation of the python model  from scratch. Demonstrating the impact of people behaviours on clusters creation and on the epidemic spread.

The goal of the model is to re-create peoples deplacements in a city and to highlight the impact of "contaminations nests" such as work places for parents or schools for children. I built a cellular automata which consist of a large NxN grid in which poeples (represented as class objects) move according to their status. The simulation runs for a certain amount of time in which people encounters other in some cells of the cellular automata. During these encounters, each has a probability to contaminate other people in the cell.
At the end of the day, I monitored the evolution of contamination rates given some entry data (contamination rates, starting number of sick people, incubation rates.... etc) and tried to highlight the differences between random movements and high frequented places. 
At the end of the project, I founded the peoples behaviours in the simulation to be significantly changing the contamination quickness. 

This was my first project in python. I had only a few monthes of experience on the topic and have had only python "algorithmic" classes at this time. Thus the code for this project is not at all optimized and clumsy, still, it worked perfectly and awarded me a grade of 18/20 to the TIPE for the engineering schools entrance exams.
Should I have a bit of time someday to update it with my new programming skills :).



