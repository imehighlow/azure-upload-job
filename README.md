# Azure Upload Job

A simple, minimalistic script that uploads `.tar.gz` files to Azure Blob Storage and sends Telegram notifications. Runs weekly on Thursdays at 23:00.

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/imehighlow/azure-upload-job.git /home/$USER/dev/azure-upload-job
cd /home/$USER/dev/azure-upload-job
```

### 2. Setup Python environment
```bash
# Create virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Create environment file
```bash
cp env.example .env
vim .env
```

Edit the `.env` file with your actual configuration values.

### 4. Schedule weekly execution (Thursday 23:00)
```bash
crontab -e
```

Add this line:
```
0 23 * * 4 cd /home/$USER/dev/azure-upload-job && /home/$USER/dev/azure-upload-job/venv/bin/python main.py
```

### 5. Test the script
```bash
# Manual test
cd /home/$USER/dev/azure-upload-job
./venv/bin/python main.py
```

## Configuration

- Edit `dirs_to_upload.txt` to specify which directories to monitor
- Only `.tar.gz` files will be uploaded
- Files already existing in Azure Blob Storage will be skipped
- Telegram notifications sent after each run

## Files

- `main.py` - Main upload script
- `dirs_to_upload.txt` - List of directories to monitor
- `requirements.txt` - Python dependencies
- `env.example` - Environment variables template
- `.env` - Environment variables (create from template)
