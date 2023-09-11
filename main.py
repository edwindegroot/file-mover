from pathlib import Path
import yaml


def include_file(file_name, valid_suffices):
    if file_name is None:
        return False
    if '.' not in file_name:
        return False
    return file_name.split('.')[-1] in valid_suffices


def move_files(the_files, target):
    for f in the_files:
        f.rename(target + f.name)


if __name__ == '__main__':
    config = yaml.safe_load(open('config/config.yml'))
    pics = config['images']
    docs = config['documents']
    videos_suffices = config['videos']
    music_suffices = config['music']
    path = Path(config['source-folder']).glob('*')

    all_files = [f for f in path]
    files = [f for f in all_files if include_file(f.name, docs)]
    images = [f for f in all_files if include_file(f.name, pics)]
    videos = [f for f in all_files if include_file(f.name, videos_suffices)]
    music = [f for f in all_files if include_file(f.name, music_suffices)]

    move_files(files, config['documents-target'])
    move_files(images, config['images-target'])
    move_files(videos, config['videos-target'])
    move_files(music, config['music-target'])

