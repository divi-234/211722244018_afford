import httpx

API_URLS = {
    'p': "http://20.244.56.144/evaluation-service/primes",
    'f': "http://20.244.56.144/evaluation-service/fibo",
    'e': "http://20.244.56.144/evaluation-service/even",
    'r': "http://20.244.56.144/evaluation-service/rand"
}

FALLBACK_DATA = {
    'p': [2, 3, 5, 7],
    'f': [0, 1, 1, 2],
    'e': [2, 4, 6, 8],
    'r': [13, 27, 31, 44]
}

async def fetch_numbers(number_type: str):
    url = API_URLS.get(number_type)
    if not url:
        print(f"[ERROR] Invalid number type: {number_type}")
        return []

    try:
        async with httpx.AsyncClient(timeout=0.5) as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get("numbers", [])
    except Exception as e:
        print(f"[WARNING] Failed to fetch from real API: {e}")
        return FALLBACK_DATA.get(number_type, [])
