import yaml

def read_yaml(file, path='../path_to_data/'):
    with open(f'{path}{file}', encoding="utf8") as f:
        file_content = yaml.full_load(f)
        f.close()
        return file_content