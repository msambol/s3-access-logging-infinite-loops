# s3-access-logging-infinite-loops

* [Detect Infinite Loops in Amazon S3 Access Logging](https://medium.com/p/bd389efdc55f)

## Run

Set your [AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) 
and run the following:

```bash
❯ pip install -r requirements.txt

❯ python s3_logs_detect_infinite_loops.py

--- LOGGING CONFIGURATIONS ---

BucketA --> BucketA
BucketB --> BucketC
BucketC --> BucketB

--- INFINITE LOOPS DETECTED ---

['BucketA']
['BucketB', 'BucketC']
```
