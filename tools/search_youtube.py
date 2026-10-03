from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from gyt_api import get


class SearchYoutubeTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        data = get(
            self.runtime.credentials["api_key"],
            "/search",
            {
                "q": tool_parameters.get("query"),
                "type": tool_parameters.get("type"),
                "page_token": tool_parameters.get("page_token"),
            },
        )
        yield self.create_json_message(data)
