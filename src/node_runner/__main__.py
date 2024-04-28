from invoke import Collection, Program
from node_runner import subcommands, __version__

program = Program(namespace=Collection.from_module(subcommands), version=__version__)
