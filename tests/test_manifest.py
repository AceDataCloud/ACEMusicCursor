import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PluginContract(unittest.TestCase):
    def test_service_and_credential_binding(self):
        manifest = json.loads((ROOT / ".cursor-plugin/plugin.json").read_text())
        config = json.loads((ROOT / manifest["mcpServers"]).read_text())
        server = config["mcpServers"]["acemusic"]
        self.assertEqual(server["headers"], {"Authorization": "Bearer ${ACEDATACLOUD_API_TOKEN}"})
        self.assertTrue((ROOT / manifest["logo"]).is_file())
        self.assertEqual(server['url'], "https://acemusic.mcp.acedata.cloud/mcp")
