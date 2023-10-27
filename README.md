# Phase_4_project
NLP Model For Sentiment Analysis

![image info](images/WordCloud.png)


Table of Contents

* [***Project Overview:***](#project-overview)

* [***Visualisations using Stills:***](#visualisations-using-stills) 

* [***Conclusion:***](#conclusion)

* [***Notebooks:***](#notebooks)


## Project Overview
The subject of our Twitter/ X data centers at the 2013 SXSW conference here
South by Southwest (SXSW) is a multi-conference event of interactive media, music, and film that occurs in Austin, Texas each year in March. Each tweet in our data mentions either Apple products, Google products, or both as well as specific products under those brands.


# Dataset Description
Number of Instances: 9,093


Link to the Data's source
* [dataset](https://data.world/crowdflower/brands-and-product-emotions) 



![image info](Images)



![image info](Images/.png)



![image info](Images/.png)



## Conclusion
Our model was unbalanced with 7% negative, 58% positive and 35% who had no emotion or couldn’t tell their feelings from the tweet. We tried modeling with Countvector and TF-IDF, we tried to balance our data with smote and embedding techniques to reduce dimension, such as negative matrix factorization, Turnicated SVD and LatentDirichletAllocation embedding techniques unfortunately our data was not enough and dimension reduction couldn’t help our models performance. Although we did get pretty balanced across all metrics with logistic regression and LatentDirichletAllocation, the best performer given the amount of data was Logistic regression with TF-IDF. Model performance across all models had a weakness of predicting negative emotion with certain data splits having no instance of tweet corpus with negative emotion. 
![image info](model_performance.png)


## Recommendations 
* Applying unicode.normalize helps address texts that couldn't be converted with the encoding used when loading data
* Results were better with TF-IDF across all models
* Embedding techniques such as LatentDirichletAllocation helps create a balanced result across all classes but more data or deploying a deep learning model would be needed

## Next Steps
* Collect more data
* Deploy deep learning algorithms
  
### Notebooks
* [Notebooks]([]()) 

* [FinalNotebook](https://github.com/Danayt09/Phase_4_project/blob/main/Modeling_ver03.ipynb)

  


## Linkedin
Gavin Martin <a href = "https://github.com/GitHbGav"><img src='https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png' width = '25' height='25'></a><a href="https://www.linkedin.com/in/gavin-martin-/"><img src='https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg' width = '25' height='25'></a>  
Claire Sarraillé <a href = "https://github.com/clairesarraille"><img src='https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png' width = '25' height='25'></a><a href="https://www.linkedin.com/in/claire-sarraille/"><img src='https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg' width = '25' height='25'></a>  
Deniz Emre <a href = "https://github.com/DenizzEmre"><img src='https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png' width = '25' height='25'></a><a href="https://www.linkedin.com/in/demre/"><img src='https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg' width = '25' height='25'></a>  
Danayt Aman <a href = "https://github.com/Danayt09"><img src='https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png' width = '25' height='25'></a><a href="https://www.linkedin.com/in/danayt-aman/"><img src='https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg' width = '25' height='25'></a>  

## References
[twitterImage](https://unsplash.com/photos/blue-and-white-heart-illustration-k1xf2D7jWUs)
