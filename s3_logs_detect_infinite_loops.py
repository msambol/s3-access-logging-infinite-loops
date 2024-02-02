import boto3 
import networkx as nx


s3 = boto3.client('s3')


def main():
    # directed graph
    G = nx.DiGraph() 

    # get all buckets in the AWS account
    buckets = [bucket.get('Name') for bucket in s3.list_buckets().get('Buckets')]
    
    print('\n--- LOGGING CONFIGURATIONS ---\n')

    for bucket in buckets:
        # get logging configuration
        logging_config = s3.get_bucket_logging(Bucket=bucket)

        # get logging destination bucket, if applicable
        target = logging_config.get('LoggingEnabled', {}).get('TargetBucket', None)

        if target:
            # add nodes and edge to the graph
            G.add_edge(bucket, target)
            print(f'{bucket} --> {target}')

    # find cycles in the graph 
    cycles = list((nx.simple_cycles(G)))
    
    if cycles:
        print('\n--- INFINITE LOOPS DETECTED ---\n')
        [print(cycle) for cycle in cycles]
    else:
        print('\nNo cycles found!')


main()
