# Prediction

As a prediction algorithm, we can think of two types of possible cases which can be used for this dataset.

1. **Frequent Pattern Mining:** Algorithms like *Apriori, FP (Frequent Pattern) Growth* and other pattern mining algorithms are very good at finding out frequent pattern sequences. For example, in our dataset, there are 4356 closed deals. We can compare *target.csv* and *activity.csv* and find out the sequence of activities done for each closed deal. From those sequences, we can find out the frequently occurring patterns and provide a prediction on which activity to perform next so that the deal gets closed.

2. **Sequence Classification using Machine Learning:** This algorithm will require machine learning algorithms like *LSTM, GRUs, and Transformers for binary sequence classification*. To organize the dataset for training we have 4356 closed deals as positive samples. We can track other customers where the deals were not closed and use the sequence of activities with those customers as negative samples. 

Given the dataset, I will start with Frequent Pattern Mining algorithms as an initial baseline. It will not provide a perfect prediction but we can get an assumption from that method. However, finally, we need to get to sequence classification methods to get into a robust working model. <br/>

To ensure that our sequence classification methods work, we need more information from the company. Following is the list of information required from the company:

- Analyzing the data it can be clearly seen that there are ***221 closed deals with no record of activity***. First of all, we need the full exhaustive information about the closed deals. When did the deal start and what activities were done in sequence till the closure of the deals. It is clear that some deals started before 9-1-2020. We need the data about the closed deals to build the positive sequence samples for our machine learning model.

- To build the negative example, it would be best if we could get the full exhaustive information about the deals that are not closed from the start. But, even if we get the starting date of all the deals in the *activity.csv* dataset, we can certainly build a huge sum of negative sequence samples.