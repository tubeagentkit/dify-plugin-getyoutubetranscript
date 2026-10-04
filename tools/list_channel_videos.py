from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from gyt_api import get


class ListChannelVideosTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        continuation = tool_parameters.get("continuation")
        if not continuation and not tool_parameters.get("channel"):
            raise ValueError("Provide a channel for the first page, or a continuation token for later pages.")
        data = get(
            self.runtime.credentials["api_key"],
            "/channel/videos",
            # The API takes either a channel (first page) or a continuation token (later pages).
            {"continuation": continuation} if continuation else {"channel": tool_parameters.get("channel")},
        )
        yield self.create_json_message(data)
