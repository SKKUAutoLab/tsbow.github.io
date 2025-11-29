from huggingface_hub import HfApi

api = HfApi()

# LOCAL
DATA_DIRECTORY = "/media/ngochdm/Projects/HUGGING_FACE/TSBOW/"

# HUGGING FACE
REPO_ID     = "SKKUAutoLab/TSBOW"
REPO_TYPE   = "dataset"

# FOLDER & FILES
FILE_NAME = "README.md"
FOLDER_NAME = "images/"

# To upload a single file
api.upload_file(
    path_or_fileobj=f"{DATA_DIRECTORY}{FILE_NAME}",
    path_in_repo=FILE_NAME,  # Desired path in the repository
    repo_id=REPO_ID,
    repo_type=REPO_TYPE, 
    commit_message=f"Add new {FILE_NAME}"
)

# To upload an entire folder
api.upload_folder(
    folder_path=f"{DATA_DIRECTORY}{FOLDER_NAME}",
    path_in_repo=FOLDER_NAME, 
    repo_id=REPO_ID,
    repo_type=REPO_TYPE,
    commit_message=f"Upload folder {FOLDER_NAME}"
)