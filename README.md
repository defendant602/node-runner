# node-runner
 Parallel execution of commands across multiple nodes.


### Installing

```
git clone https://github.com/defendant602/node-runner.git
cd node-runner
pip install .
```


### Getting started

```
$node-runner -h execute

Usage: node-runner [--core-opts] execute [--options] [other tasks here ...]

Docstring:
  Parallel execution of command across multiple nodes.

Options:
  -c STRING, --cmd=STRING         command to run on each host/node
  -h STRING, --host-list=STRING   comma seperated hostnames or TSV FILE containing hostnames in the first column
  -i STRING, --hide=STRING        hide output of command, stderr/stdout/both[None]
```