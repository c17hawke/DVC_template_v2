from collections import namedtuple

## update entity as per your requirements
DataIngestionConfig = namedtuple("DataIngestionConfig", [
    "root_dir",
    "source_URL",
    "local_data_file",
    "unzip_dir"
])
