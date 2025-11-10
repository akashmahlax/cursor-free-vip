import configparser
import os
from utils import get_user_documents_path

# Get config path
config_path = os.path.join(get_user_documents_path(), '.cursor-free-vip', 'config.ini')
print(f"Config file: {config_path}")

# Read config
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

# Update cursor path
new_cursor_path = r'C:\Program Files\cursor\resources\app'
config.set('WindowsPaths', 'cursor_path', new_cursor_path)

# Save config
with open(config_path, 'w', encoding='utf-8') as f:
    config.write(f)

print(f"✅ Updated cursor_path to: {new_cursor_path}")
print(f"✅ Config file saved!")
