# Dockerhub Collector

Dockerhub metadata collector designed to be used with the [MAO-MAO](https://mao-mao-research.github.io/) orchestrator.

It collects metadata for repositories in the Dockerhub library and its first degree 'relatives' and computes basic statistics.

Using it as standalone is also possible:

```
docker run -v /your/data/path:/usr/src/app/data panosece/dockerhub-collector:<tag>
```

For instructions on using it with the Orchestrator visit its [github page](https://github.com/serviceprototypinglab/mao-orchestrator).
