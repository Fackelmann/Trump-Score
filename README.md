# Trump Score

Machine Learning model trained using TensorFlow and Keras that predicts if a tweet belongs to Trump. A RESTful API has been implemented around it to provide a "Trump Score", this is, the likelihood that a tweet belongs to Trump.

## ML Model

This model used ~80k tweets: ~25k Trump tweets pre-2017 [1], ~25k random user tweets [2], ~8k Obama tweets[3], and ~30k Tweets made by Democrat politicians during the last presidential election cycle[4].

(The original model only used Trump and random user tweets, but any tweet mentioning politics or America ended up beign assigned a "Trump Score" close to 1)

The feature in this case consist on the invidual words of the tweets. These words were obtained using sklearn and CountVectorizer and converted to label based encoding from the original one hot encoding. The top 10k most used words were selected. In addition to this, all links and Twitter mentions were pre-processed and converted to special word tokens.

This features were then used to train a Deep Neural Network using TensorFlow and the Keras API [5]. This neural network consists on one input embedding layer, 16 hidden layers, and one ouput layer.

The vectorizer for the input text and the ML model can be found under ./web/model_data.

## API

The current specification only provides one API call. This will POST the tweet to be analyzed, and the response will be a status message (200), and the likelihood that it belongs to Trump

### URL

0.0.0.0:5000/request

### Method

POST

### Data Params

 {"tweet": "<body of the tweet"}

### Success Response:

<What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!>

{ "status": 200 
  "msg":"<Trump Score>"}
  
### Example

API call:
{
	"tweet":"Thousands of people are already lined up in Orlando, some two days before tomorrow nights big Rally. Large Screens and food trucks will be there for those that can’t get into the 25,000 capacity arena. It will be a very exciting evening! Make America Great Again!"
}

API response:
{
    "msg": 0.9852935671806335,
    "status": 200
}



## Installation

Docker configuration is provided. Simply download the repo and run 
- docker-compose build
- docker-compose up

Service is available at 0.0.0.0:5000

## To do
- Expand API. Current version is just a raw Proof of Concept without any error handling.
- Deploy API in AWS
- Provide Jupyter notebooks used to train the model
- Implement twitter bot to provide results on Twitter when requested. You can know how "Trumpy" you and your friends are!

## Future development ideas
- Obtain the bi-gram features and see how accuracy is affected. My prediction is that it should improve, as combination such as "Make America" should are more likely to be made by Trump that by other users/politicians.

## References
[1] http://trumptwitterarchive.com
[2] Z. Cheng, J. Caverlee, and K. Lee. You Are Where You Tweet: A Content-Based Approach to Geo-locating Twitter Users. In Proceeding of the 19th ACM Conference on Information and Knowledge Management (CIKM), Toronto, Oct 2010. https://archive.org/details/twitter_cikm_2010
[3] https://community.periscopedata.com/t/x1fy7p/barack-obamas-tweet-history
[4] https://www.kaggle.com/kapastor/democratvsrepublicantweets
[5] https://www.tensorflow.org/tutorials/keras/basic_text_classification
