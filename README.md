# locust-openfaas

Locust load-testing tool on OpenFaaS

## What is Locust?

> [Locust](https://docs.locust.io/en/latest/what-is-locust.html) is an easy-to-use, distributed, user load testing tool. It is intended for load-testing web sites (or other systems) and figuring out how many concurrent users a system can handle.
> The idea is that during a test, a swarm of locusts will attack your website. The behavior of each locust (or test user if you will) is defined by you and the swarming process is monitored from a web UI in real-time. This will help you battle test and identify bottlenecks in your code before letting real users in.

## How do you use it with OpenFaaS? 

This example function shows that it's possible to run a locust load-test through OpenFaaS.

Usage:

```
$ faas-cli build
$ faas-cli deploy
$ echo -n https://requestb.in/uhphaiuh | \
  faas-cli invoke locust > results.csv && \
  cat results.csv
```

This will take several seconds to build up to the full load and will return the whole output to your client when done as a CSV result file in plain-text.

```
"Method","Name","# requests","# failures","Median response time","Average response time","Min response time","Max response time","Average Content Size","Requests/s"
"GET","/uhphaiuh",1099,0,340,702,141,5702,2,213.43
"None","Total",1099,0,340,702,141,5702,2,213.43
```

You will also need to up the timeouts on your OpenFaaS gateway.
