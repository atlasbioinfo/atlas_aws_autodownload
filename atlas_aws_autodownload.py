import argparse
import os,boto3,tqdm,logging

def aws_download(config_file, local_path):

    
    aws_access_key_id = ''
    aws_secret_access_key = ''
    region_name = ''
    bucket_name=''
    folder_path=''
    

    with open(config_file, "r", encoding='utf-8') as f:
        for line in f:
            if (line.find("：")!=-1):
                line = line.replace("：", ":")
            if line.startswith("Aws_access_key_id"):
                aws_access_key_id = line.split(":")[1].strip()
            if line.startswith("Aws_secret_access_key"):
                aws_secret_access_key = line.split(":")[1].strip()
            if line.startswith("Region"):
                region_name = line.split(":")[1].strip()
            if line.find("s3://") !=-1:
                line=line.strip().split("s3://")[1]
                bucket_name = line.split("/")[0].strip()
                folder_path = line.split("/")[1].strip()

    # return aws_access_key_id, aws_secret_access_key, region_name, bucket_name, folder_path

    print(f'Configuration file: {config_file}')
    print(f'Region: {region_name}')
    print(f'Local path: {local_path}')
    print(f'Bucket name: {bucket_name}')
    print(f'Folder path: {folder_path}')
    print(f'AWS Access Key ID: ${aws_access_key_id}$')
    
    local_path = os.path.join(local_path, folder_path)
    os.makedirs(local_path, exist_ok=True)

    logging.basicConfig(filename=os.path.join(local_path,folder_path+'.aws.log'), level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.info(f'Configuration file: {config_file}')
    logging.info(f'Local path: {local_path}')
    logging.info(f'Bucket name: {bucket_name}')
    logging.info(f'Folder path: {folder_path}')

    s3 = boto3.client('s3', 
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    region_name=region_name)
    
    
    objects = s3.list_objects(Bucket=bucket_name, Prefix=folder_path)
    logging.info(f'Objects: {objects}')

    for obj in tqdm.tqdm(objects['Contents']):
        key = obj['Key']
        if not key.endswith('/'):
            local_file_path = os.path.join(local_path, os.path.relpath(key, folder_path))
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            logging.info(f'Downloading: {key}')
            s3.download_file(bucket_name, key, local_file_path)
            logging.info(f'Downloaded: {local_file_path}')

    logging.info('Download completed')

if __name__ == "__main__":

    logo = r'''   

          _   _             ____  _       _        __
     /\  | | | |           |  _ \(_)     (_)      / _|
    /  \ | |_| | __ _ ___  | |_) |_  ___  _ _ __ | |_ ___
   / /\ \| __| |/ _` / __| |  _ <| |/ _ \| | '_ \|  _/ _ \
  / ____ \ |_| | (_| \__ \ | |_) | | (_) | | | | | || (_) |
 /_/    \_\__|_|\__,_|___/ |____/|_|\___/|_|_| |_|_| \___/

        `-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"
        `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/
            y==/        y==/        y==/        y==/
        ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.
        ,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_
                    
    '''


    description_text = '''{} 
        This script is used to download files from AWS S3 bucket.
        The configuration file should be in the following format:
            Project:***
            Alias ID:***
            S3 Bucket:***
            Account:***
            Password:***
            Region:***
            Aws_access_key_id:***
            Aws_secret_access_key:***
        .'''.format(logo)
    
    parser = argparse.ArgumentParser(description=description_text, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-c", "--config", help="Configuration file path", required=True)
    parser.add_argument("-l", "--local", help="Local path to save the downloaded files", default='./')

    args = parser.parse_args()

    config_file = args.config
    local_path = args.local

    aws_download(config_file, local_path)