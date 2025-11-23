import logging
import os


class ClientFileService:
    def __init__(self):
        pass

    def save_file_to_disk(self, path_to_save_to, file_name, file_contents):
        os.makedirs(path_to_save_to, exist_ok=True)
        with open(os.path.join(path_to_save_to, file_name), "wb") as file:
            logging.debug(f"Writing file {file_name} to {path_to_save_to} on the disk.")
            file.write(file_contents)
        logging.debug(f"File {file_name} written to {path_to_save_to} on the disk.")


    def read_file_from_disk(self, full_file_path):
        with open(full_file_path, "rb") as file:
            file_contents = file.read(-1)
        return file_contents