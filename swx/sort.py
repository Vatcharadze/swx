from swx.extension_dict import EXTENSION_MAP


def organize_files(file_list, base_directory):
    for file_path in file_list:
        ext = file_path.suffix.lower()
        folder_name = EXTENSION_MAP.get(ext, 'Others')
        target_folder = base_directory / folder_name

        target_folder.mkdir(exist_ok=True)
        destination = target_folder / file_path.name
        file_path.rename(destination)