# Atlas AWS Auto-download

A Python tool for automatically downloading sequence data from AWS S3 buckets. Tested and verified to work with BGI sequencing data.

[English](#english) | [中文](#chinese)

## English

### Description
This tool helps you automatically download files from AWS S3 buckets using configuration files. It's particularly useful for downloading sequence data and maintaining a proper logging system.

### Requirements
- Python 3.x
- Required packages:
  - boto3
  - tqdm

### Installation
```bash
git clone git@github.com:atlasbioinfo/atlas_aws_autodownload.git
pip install boto3 tqdm
cd atlas_aws_autodownload
```

### Usage
```bash
python atlas_aws_autodownload.py -c <config_file> -l <local_path>
```

#### Parameters:
- `-c, --config`: Configuration file path (required)
- `-l, --local`: Local path to save the downloaded files (optional, default: current directory)

### Configuration File Format
```plaintext
Project:***
Alias ID:***
S3 Bucket:s3://your-bucket-name/folder-path
Account:***
Password:***
Region:***
Aws_access_key_id:***
Aws_secret_access_key:***
```

### Features
- Automatic file download from AWS S3
- Progress bar display
- Detailed logging system
- Support for nested directory structures
- Handles both Chinese and English configuration files

