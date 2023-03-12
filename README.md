# Dev Exercises

## Excercise 1
Write a simple C# console application to query a web-api route "https://dev.nexbe.nz/api/devices". Assume the response will be a collection of device objects e.g.

```
[
{
   "id": "....",
   "name": "....",
   "location": {
       "lat": 12.121,
       "lng": 112.55
   } 
}]
```

Write the properties of each device to the screen.

## Exercise 2
Create a function to efficiently persist the time series data to a POSTGRES database table named "data" assuming the input is:

```
{
    "Records": [
        {
            "MessageId": null,
            "ReceiptHandle": null,
            "Body": "...",
            "Md5OfBody": null,
            "Md5OfMessageAttributes": null,
            "EventSourceArn": null,
            "EventSource": null,
            "AwsRegion": null,
            "Attributes": null,
            "MessageAttributes": null
        }
    ]
}
```

and the body contains:
```
{
    "clientId": "1",
    "recs": [
        {"x": 1.003, "i": 1.090},
        {"x": 1.101, "i": 1.090}
        {"x": 1.023, "i": 1.090}
        {"x": 1.000, "i": 1.090}
        {"x": 1.066, "i": 1.090}
        {"x": 1.111, "i": 1.090}
        {"x": 1.901, "i": 1.085}
        {"x": 1.443, "i": 1.090}
        {"x": 1.126, "i": 1.090}
        {"x": 1.091, "i": 1.090}
        {"x": 1.761, "i": 1.071}
        {"x": 1.333, "i": 1.090}
        {"x": 1.334, "i": 1.090}
        {"x": 1.001, "i": 1.088}    
    ]
}
```

HINT: Lambdas are billed on execution time. If you are not familiar with Postres, please describe the type of techinique you would use to insert the data.

## Excercise 3
Using react, write a simple application that can display a list of products in a scroll view. Product list should be taken using an API call to https://dummyjson.com/products . Use React Functional Components approach. Display title, description, price and a small thumb for each product.

## Excercise 4
The file ex1.py contains an extract of a lambda function built in Python. As is indicated in the comments, the event which triggers it may contain multiple physical messages, and each may contain many logical messages. 

Your task is to add effective error handling. Assume that the outcome should be that an API will be invoked with the signature being something like:

```
create_datadog_event(
    title="The IOT publish lambda has failed", 
    desc="One or more messages failed to publish", 
    alert_type=AlertType.Error)
```

HINT: Beyond try/except, inspect the code and look to identify minor design issues which will allow you to simplify the exception handling.

## Exercise 5
You have been asked to deploy a new lambda function to AWS which will be invoked when a batch of messages is available (via event source mapping / lambda polling). The lambda function needs to write the data to a time-series database (ElasticSearch), and then write metrics to DynamobDB. 

The storage of the time-series data is critical, and the metrics will be used to help generate billing statements - so they must also be stored successfully.

Describe the issue you will face in creating this lambda and one or more ways of solving that issue.

