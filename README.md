# Atlas AWS Auto-download

A Python tool for automatically downloading sequence data from AWS S3 buckets. Tested and verified to work with BGI sequencing data.

[English](#english) | [中文](#中文说明)

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

## 中文说明

### 描述
这是一个用于从AWS S3存储桶自动下载文件的Python工具。它特别适用于下载序列数据（如BGI测序数据），并具有完善的日志记录系统。

### 环境要求
- Python 3.x
- 所需包：
  - boto3
  - tqdm

### 安装方法
```bash
git clone git@github.com:atlasbioinfo/atlas_aws_autodownload.git
pip install boto3 tqdm
cd atlas_aws_autodownload
```

### 使用方法
```bash
python atlas_aws_autodownload.py -c <配置文件路径> -l <本地保存路径>
```

#### 参数说明：
- `-c, --config`：配置文件路径（必需）
- `-l, --local`：文件下载保存的本地路径（可选，默认为当前目录）

### 配置文件格式
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

### 功能特点
- 自动从AWS S3下载文件
- 显示下载进度条
- 详细的日志记录系统
- 支持嵌套目录结构
- 支持中英文配置文件

```

This README includes:
1. Bilingual descriptions (English and Chinese)
2. Clear installation and usage instructions
3. Configuration file format explanation
4. Main features of the tool
5. Required dependencies
6. Command-line parameters explanation

You may want to customize:
1. The repository URL (replace `yourusername` with your actual GitHub username)
2. Add any specific installation requirements
3. Add examples of usage if needed
4. Add any troubleshooting section if necessary
5. Add a license section if you want to specify a license for your code

Would you like me to modify any part of this README?
