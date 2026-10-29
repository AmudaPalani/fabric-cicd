import os
import re
from pathlib import Path

from azure.identity import AzureCliCredential
from fabric_cicd import FabricWorkspace, change_log_level, publish_all_items

change_log_level("DEBUG")

pipeline_name = os.environ.get("PIPELINE_NAME", "Palani_Pipeline_2_Graph")

target_workspace = FabricWorkspace(
    workspace_id=os.environ["FABRIC_WORKSPACE_ID"],
    repository_directory=str(Path(__file__).resolve().parents[1] / "fabric1"),
    item_type_in_scope=["DataPipeline"],
    token_credential=AzureCliCredential(),
)

# Publish only the Graph-based pipeline so the Outlook pipeline (Pain 2 demo) is left as is.
publish_all_items(
    target_workspace,
    item_name_exclude_regex=rf"^(?!{re.escape(pipeline_name)}$).*$",
)
