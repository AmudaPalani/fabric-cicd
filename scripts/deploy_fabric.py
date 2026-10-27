import os
from pathlib import Path

from azure.identity import AzureCliCredential
from fabric_cicd import FabricWorkspace, publish_all_items

workspace_id = os.environ["FABRIC_WORKSPACE_ID"]
repository_directory = Path(__file__).resolve().parents[1] / "fabric1"

target_workspace = FabricWorkspace(
    workspace_id=workspace_id,
    repository_directory=str(repository_directory),
    item_type_in_scope=["Lakehouse", "Notebook"],
    token_credential=AzureCliCredential(),
)

publish_all_items(target_workspace)
