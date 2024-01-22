from conf import settings
name = settings.NAME
url = settings.MAIN_URL

from utils import create_url
result = create_url.create_url(name, url)

print(result)