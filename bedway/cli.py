import asyncio
from functools import wraps

import click
import uvicorn

from .app import app


@click.command()
@click.option("--host", type=click.STRING, default="0.0.0.0")
@click.option("--port", type=click.INT, default=8192)
def start(host, port):
    """
    Start the server.
    """
    uvicorn.run(app, host=host, port=port)
