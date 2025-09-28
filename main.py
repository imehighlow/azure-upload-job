from simple_logger import setup_logger
from azure_blob_storage_wrapper import AzureBlobStorageWrapper
from telegram_notifier import TelegramNotifier
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    logger = setup_logger()
    telegram = TelegramNotifier(
        token=os.getenv("TELEGRAM_BOT_TOKEN"), 
        chat_id=os.getenv("TELEGRAM_CHAT_ID"), 
        service_name="Azure Upload Job"
    )
    azure = AzureBlobStorageWrapper(
        account_name=os.getenv("AZURE_BLOB_STORAGE_ACCOUNT_NAME"),
        container_name=os.getenv("AZURE_BLOB_STORAGE_CONTAINER_NAME"),
        logger=logger
    )
    
    with open("dirs_to_upload.txt") as f:
        directories = f.read().splitlines()
    
    uploaded = []
    
    for directory in directories:
        for file in os.listdir(directory):
            if not file.endswith(".tar.gz"):
                continue
            file_path = os.path.join(directory, file)
            if not azure.exists(file):
                azure.upload(file_path, file)
                logger.info(f"Uploaded {file}")
                uploaded.append(file)
    
    message = f"Uploaded: {uploaded}" if uploaded else "No new files uploaded to Azure"
    telegram.send_message(message)

if __name__ == "__main__":
    main()
