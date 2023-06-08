import os
from platformdirs import user_documents_dir

if os.name == "nt":
    WSM_FOLDER_PATH = os.path.join(user_documents_dir(), "Sennheiser", "Wireless Systems Manager", "Configuration", "")
    WWB_FOLDER_PATH = os.path.join(user_documents_dir(), "Shure", "Inventory", "")
elif os.name == "posix":
    WSM_FOLDER_PATH = os.path.join(user_documents_dir(), "WSM", "Configuration", "")
    WWB_FOLDER_PATH = os.path.join(user_documents_dir(), "Shure", "Inventory", "")
else:
    raise OSError

OUTPUT_FOLDER_PATH = WSM_FOLDER_PATH
