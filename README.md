# node-runner
 Parallel execution of shell commands across multiple nodes over SSH.


### Installing

```
git clone https://github.com/defendant602/node-runner.git
cd node-runner
pip install .
```


### Getting started
#### Usage

```
$node-runner -h execute

Usage: node-runner [--core-opts] execute [--options] [other tasks here ...]

Docstring:
  Parallel execution of commands across multiple nodes.

Options:
  -c STRING, --cmd=STRING         command to run on each host/node
  -h STRING, --host-list=STRING   comma seperated hostnames or TSV FILE containing hostnames in the first column
  -i STRING, --hide=STRING        hide output of command, stderr/stdout/both[None]
```

#### Example
```
$node-runner execute -c 'sleep $((RANDOM % 3)) && hostname' -h cu07,cu08,cu09
cu08
cu09
cu07
[WARNING]: cu08 execution completed.
[WARNING]: cu09 execution completed.
[WARNING]: cu07 execution completed.
```