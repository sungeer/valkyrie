import httpx2 as httpx

BASE_URL = 'http://127.0.0.1:8848'


def list_users(limit: int = 10):
    url = f'{BASE_URL}/users.list'

    data = {
        'limit': limit
    }

    resp = httpx.post(url, json=data, timeout=5.0, verify=False)
    data = resp.json()

    return data


def main():
    data = list_users(5)
    return data


if __name__ == '__main__':
    ret = main()
    print(ret)
