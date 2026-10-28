import os
from pathlib import Path

from azure.identity import AzureCliCredential
from fabric_cicd import FabricWorkspace, change_log_level, publish_all_items

change_log_level("DEBUG")

target_workspace = FabricWorkspace(
    workspace_id=os.environ["FABRIC_WORKSPACE_ID"],
    repository_directory=str(Path(__file__).resolve().parents[1] / "fabric1"),
    item_type_in_scope=["DataPipeline"],
    token_credential=AzureCliCredential(),
)

publish_all_items(target_workspace)
