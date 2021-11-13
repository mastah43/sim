# Simulation Experiment
This to be evolved simulation experiment is subject to be used 
with producing lots of output streaming data. 
It is planned to be run in Amazon EKS.

## Next steps in development
- include AWS IaC for ECS cluster, tasks definitions
- use a sufficiently complex simulation
- use reinforcement learning with agents
- run multiple worlds in cluster
- run a distributed single large simulation in cluster using Elastic Cache
- forward AWS temporary access credentials to docker container on startup
- send streaming events (see also https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
- receive streaming events with Kinesis and send to S3
- process streaming event with Kinesis data streams