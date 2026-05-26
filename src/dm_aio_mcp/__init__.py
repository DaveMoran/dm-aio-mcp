"""dm-aio-mcp package.

An MCP server for my dashboard api
"""

from __future__ import annotations

from dm_aio_mcp._internal.cli import get_parser, main

__all__: list[str] = ["get_parser", "main"]
