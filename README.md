# Coel Coding Challenge

Thanks you for attending the Coel Coding Challenge. We are looking forward to see your achievement.

## Problem Definition
A company is selling products to customers. They do a lot of activities such as visiting customers, sending emails, hosting events and so on and so on to close deals. They want to utilize their data to

- predict the probability of closing deals with each customer
- evaluate the activities they have done to close deals with customers.

They have two types of dataset, activity data and target data.

## Dataset
### Activity data
Activity data is a record of activities they have done to each customer. You can refer to the activity.csv for all activity data they have at the moment.

|column name|description|
|----|----|
|data|date when the activity has been done|
|customer|customer id to whom activity has been made|
|activity_type|type of the activity. There are 25 types, {a-y} at the moment.|
|activity_count|number of times the activity has been made on that date.|

Note that activity types are obfuscated for security reason.

### Target data
Target data is a record of closed deals. Each record represents the date a deal has been closed with a customer. You can refer to the target.csv for all target data they have at the moment.

|column name|description|
|----|----|
|customer|customer id with whom the deal has been closed|
|date|date when a deal has been closed with the customer|

## Task Assignment
You are asked to work on two topics, activity contribution and prediction.

### Schedule

- Due date: **6pm, June 13th, 2021**
- Submission: **github pull-request**

### Github repository
Create a private repository using your github account, and invite **<hsuzuki@coel.run>** as a contributor so that we can access the repository.

Create a feature/assignment branch and put everything there. Once you are done with the assignment, create a pull-request and set a reviewer to **<hsuzuki@coel.run>**.

### Activity Contribution
As you can observe from the dataset, the company has done 904772 activities to 139556 customers from 9-1-2020 through 5-23-2021. And as the result of these activites, the company has closed 4356 deals with 4356 unique cosutmers. The company would like to evaluate the activities they have done to understand how much each activity has contributed to those closed deals.

You need to save 3 files in the repository.
- source code (python)
- csv file (see below for the detail)
- readme.md (see below for the detail)

The result should be saved in a csv file with the following format.

|column name|description|
|---|---|
|activity_type|type of the activity. There are 25 types, {a-y} at the moment.|
|contribution|contribution value (0,1)|

You also need to create a readme.md file in the repository, where you are supposed to explain your algorithm, observations/findings and ideas to improve the performance. Any additional comments are always welcome.

### Prediction
For this task, you don't need to do a real prediction but describe how you will do to get better prediction with the given dataset. Follwoing is the list of things, but not limited, you are expeceted to describe in the document.

- Prediction algorithm overview.
- Why did you choose the algorithm?
- What are missing information, what do we need to get more from the company?
