# Dockerhub Collector

Dockerhub metadata collector designed to be used with the [MAO-MAO](https://mao-mao-research.github.io/) orchestrator.

It collects metadata for repositories in the Dockerhub library and its first degree 'relatives' and computes basic statistics.

Using it as standalone is also possible:

```
docker run -v </your/data/path>:/usr/src/app/data panosece/dockerhub-collector:<tag>
```

For instructions on using it with the Orchestrator visit its [github page](https://github.com/serviceprototypinglab/mao-orchestrator).

## CLI

The Docker Hub metadata collector can be run without arguments to execute the data acquiring and assessment step one after another.

Or the user might select to execute only one of those two at a time.

```
usage: main.py [-h] [{acquire,assess,all}]

Docker Hub Metadata Collector

positional arguments:
  {acquire,assess,all}  Process step to run. Select single step to "acquire" or "assess" data. Or use "all" to run both steps intertwined (default).

optional arguments:
  -h, --help           show this help message and exit
```