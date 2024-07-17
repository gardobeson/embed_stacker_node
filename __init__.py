from .node import embed_stacker_node

NODE_CLASS_MAPPINGS = {"embed_stacker_node": embed_stacker_node}
NODE_DISPLAY_NAME_MAPPINGS = {"embed_stacker_node": "Embed Stacker"}

# ------------------------ Remove copied web extension -------------------------
from pathlib import Path

node_dir = Path(__file__).resolve().parent
comfy_dir = node_dir.parent.parent
destination_dir = comfy_dir / "web" / "extensions" / "tropfchen"
destination_path = destination_dir / "epQuickNodes.js"

if destination_path.exists():
    destination_path.unlink()

# --------------------------- Install web extension ----------------------------
WEB_DIRECTORY = "./js"
__all__ = ["WEB_DIRECTORY"]
