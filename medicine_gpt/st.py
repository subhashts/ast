import os

# Define the corrected folder and file structure
structure = {
    "medicine_mgmt": {
        "app": {
            "files": ["__init__.py", "models.py"],
            "routes": ["auth.py", "admin.py", "worker.py"],
            "templates": {
                "files": ["layout.html"],
                "auth": ["home.html", "login.html", "admin_signup.html"],
                "admin": [
                    "dashboard.html", "inventory.html", "buy.html", "sell.html",
                    "transactions.html", "workers.html"
                ],
                "worker": [
                    "dashboard.html", "inventory.html", "sell.html", "transactions.html"
                ]
            },
            "static": {
                "css": ["style.css"]
            }
        },
        "files": ["run.py", "config.py", "requirements.txt"]
    }
}

# Function to create directories and files
def create_structure(base_path, structure):
    for folder, content in structure.items():
        base_folder = os.path.join(base_path, folder)
        os.makedirs(base_folder, exist_ok=True)

        if isinstance(content, dict):
            for subfolder, items in content.items():
                if subfolder == "files":
                    for file in items:
                        file_path = os.path.join(base_folder, file)
                        with open(file_path, "w") as f:
                            f.write("")  # Create an empty file
                else:
                    dir_path = os.path.join(base_folder, subfolder)
                    os.makedirs(dir_path, exist_ok=True)
                    if isinstance(items, list):
                        for file in items:
                            file_path = os.path.join(dir_path, file)
                            with open(file_path, "w") as f:
                                f.write("")  # Create an empty file
                    elif isinstance(items, dict):
                        create_structure(dir_path, items)
        elif isinstance(content, list):
            for file in content:
                file_path = os.path.join(base_folder, file)
                with open(file_path, "w") as f:
                    f.write("")  # Create an empty file

# Run the script
create_structure(".", structure)
print("Directory structure created successfully.")
