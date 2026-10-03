from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from gyt_api import get


class GetTranscriptTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        data = get(
            self.runtime.credentials["api_key"],
            "/transcript",
            {
                "v": tool_parameters.get("video"),
                "language": tool_parameters.get("language"),
                "timestamps": "true" if tool_parameters.get("timestamps") else None,
            },
        )
        yield self.create_text_message(data.get("transcript") or "")
        yield self.create_json_message(data)
