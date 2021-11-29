# Dev Exercises

## Excercise One
ex1.py contains an extract of a lambda function built in Python. As is indicated in the comments, the event which triggers it may contain multiple physical messages, and each may contain many logical messages. 

Your task is to add effective error handling. Assume that the outcome should be that an API will be invoked with the signature being something like:

```
create_datadog_event(
    title="The IOT publish lambda has failed", 
    desc="One or more messages failed to publish", 
    alert_type=AlertType.Error)
```

HINT: Beyond try/except, inspect the code and look to identify minor design issues which will allow you to simplify the exception handling.

## Exercise Two
You have been asked to deploy a new lambda function to AWS which will be invoked when a batch of messages is available (via event source mapping / lambda polling). The lambda function needs to write the data to a time-series database (ElasticSearch), and then write metrics to DynamobDB. 

The storage of the time-series data is critical, and the metrics will be used to help generate billing statements - so they must also be stored successfully.

Describe the issue you will face in creating this lambda and one or more ways of solving that issue.

## Exercise Three
Create a lambda (any language you like) to efficiently persist the time series data to a POSTGRES database table named "data" assuming the input is:

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

