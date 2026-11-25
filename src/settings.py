import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy.engine import URL

VERSION = '26.1125.1741'

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = BASE_DIR / '.env'
if dotenv_path.exists():
    load_dotenv(dotenv_path)

ENVIRONMENTS = ('development', 'testing', 'production')
ENVIRONMENT = os.getenv('ENVIRONMENT')
if ENVIRONMENT not in ENVIRONMENTS:
    raise ValueError(f'Invalid ENVIRONMENT: {ENVIRONMENT}')

# LOG_FILE = BASE_DIR / 'logs/valkyrie.log'
LOG_DIR = Path(os.getenv('LOG_DIR', default=str(BASE_DIR / 'logs')))

# 慢请求告警阈值 毫秒
SLOW_REQUEST_MS = int(os.getenv('SLOW_REQUEST_MS', default='500'))

JWT_ALGORITHM = 'HS256'  # 加密算法

# 访问令牌有效期 600分钟
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv('JWT_ACCESS_TOKEN_EXPIRE_MINUTES', default='600')
)

AUTH_KEY = os.getenv('AUTH_KEY')  # HMAC 签名密钥 'openssl rand -hex 32'
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')  # JWT 签名密钥

# CORS 允许的来源 逗号分隔
ORIGINS = os.getenv('ORIGINS').split(',')

DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT', default='3306'))
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

DB_URL = URL.create(
    drivername='postgresql+psycopg',
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

LLM_MODEL = os.environ.get('LLM_MODEL', 'deepseek-flash')
LLM_URL = os.environ.get('LLM_URL')
LLM_KEY = os.environ.get('LLM_KEY')
