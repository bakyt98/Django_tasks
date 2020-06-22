from rest_framework.exceptions import ValidationError
from utils import constants


def validate_image_size(file):
    if file.file.size > constants.MAX_FILE_SIZE:
        raise ValidationError('maximum size of file can be {}MB'.format(
            constants.MAX_FILE_SIZE/(1024*1024)))

def validate_image_extension(file):
    print(file.file)
    print(file.file.path)
    ext = file.file.path.split('.')[1]
    print(ext)
    if ext not in ['jpg', 'png']:
        raise ValidationError('Allowed extensions are *.jpg, *.png')
