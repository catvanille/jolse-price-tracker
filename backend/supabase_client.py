from supabase import create_client, Client
from dotenv import load_dotenv
import os

# load env variable
load_dotenv()

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_ANON_KEY')

supabase: Client = create_client(url, key)