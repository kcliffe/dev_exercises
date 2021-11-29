# Dev Exercises

## Excercise One
Ex1.py contains an extract of a lambda function built in Python. As is indicated in the comments, the event which triggers it may contain multiple physical messages, and each may contain many logical messages. 

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
...
