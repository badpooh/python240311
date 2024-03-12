import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 대상 폴더 경로
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 폴더 생성 함수
def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# 폴더 생성
create_folder(image_folder)
create_folder(data_folder)
create_folder(docs_folder)
create_folder(archive_folder)

# 파일 이동 함수
def move_files(source_folder, destination_folder, extensions):
    for filename in os.listdir(source_folder):
        if filename.endswith(extensions):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)

# 이미지 파일 이동 (*.jpg, *.jpeg)
move_files(download_folder, image_folder, ('.jpg', '.jpeg'))

# 데이터 파일 이동 (*.csv, *.xlsx)
move_files(download_folder, data_folder, ('.csv', '.xlsx'))

# 문서 파일 이동 (*.txt, *.doc, *.pdf)
move_files(download_folder, docs_folder, ('.txt', '.doc', '.pdf'))

# 압축 파일 이동 (*.zip)
move_files(download_folder, archive_folder, ('.zip'))

print("파일을 이동했습니다.")
