import os
import logging
from invoke import task
import fabric
from fabric import ThreadingGroup


logging.basicConfig(
    format='[%(levelname)s]: %(message)s',
)
LOG = logging.getLogger(__name__)


@task(help={
    "host_list": "comma seperated hostnames or TSV FILE containing hostnames in the first column",
    "cmd": "command to run on each host/node",
    "hide": "hide output of command, stderr/stdout/both[None]"
})
def execute(c, host_list, cmd, hide=None):
    """
    Parallel execution of command across multiple nodes.
    """

    if os.path.exists(host_list):
        with open(host_list, "r") as f:
            hosts = [line.strip().split('\t')[0].strip() for line in f]
    else:
        hosts = host_list.split(",")

    pool = ThreadingGroup(*hosts)

    try:
        res = pool.run(cmd, hide=hide)
    except fabric.exceptions.GroupException as e:
        res = e.result

    for host, result in res.items():
        if isinstance(result, fabric.runners.Result):
            success = result.ok
            error = result.stderr
        else:
            success = False
            error = result
        status = 'completed.' if success else f'failed. ERROR: {error}'
        LOG.warning(f"{host.host} execution {status}" )

    
