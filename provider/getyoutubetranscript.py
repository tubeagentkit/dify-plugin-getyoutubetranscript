from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from gyt_api import get


class GetyoutubetranscriptProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            # /credits costs no credits, so validating a key is free.
            get(credentials.get("api_key", ""), "/credits")
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
