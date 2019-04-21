import schedule
from distutils.dir_util import copy_tree


# про distutils.dir_util нашла здесь https://docs.python.org/3/distutils/apiref.html#distutils.dir_util.copy_tree

def reserve_copy():
    # если директории не существует, выдается ошибка DistutilsFileError
    from_directory = "C:/Users/Lue/Documents/some_files"

    # если директории не существует, создается автоматически
    to_directory = "C:/Users/Lue/Pictures/some_files_reserved"

    copy_tree(from_directory, to_directory)


schedule.every(5).seconds.do(reserve_copy)
# schedule.every().day.at("00:10").do(reserve_copy)

while True:
    schedule.run_pending()
