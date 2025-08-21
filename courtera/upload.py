from huggingface_hub import HfApi

api = HfApi()

# Upload model
api.upload_file(
    path_or_fileobj="bert_model.h5",
    path_in_repo="bert_model.h5",
    repo_id="EyadAmgad/bert_h5_tokenizer"
)

# Upload tokenizer folder
api.upload_folder(
    folder_path="bert_tokenizer",
    repo_id="EyadAmgad/bert_h5_tokenizer"
)
