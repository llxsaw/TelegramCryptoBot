import aiohttp


async def get_coin_link(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            homepage_list = data['links'].get('homepage', [])
            homepage = homepage_list[0] if homepage_list and homepage_list[0] else "– пока что нету ссылки"

            twitter_username = data['links'].get('twitter_screen_name')
            twitter = f"https://twitter.com/{twitter_username}" if twitter_username else "– пока что нету ссылки"

            reddit = data['links'].get('subreddit_url') or "– пока что нету ссылки"

            github_list = data['links']['repos_url'].get('github')
            github = github_list[0] if github_list and github_list[0] else "– пока что нету ссылки"

            return homepage, twitter, reddit, github


async def get_price(coin_id: str = 'bitcoin'):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': coin_id,
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()

            if coin_id in data:
                price = data[coin_id]['usd']
                change_24h = round(data[coin_id]['usd_24h_change'], 2)
                return price, change_24h
            else:
                return None, None


async def get_top_gainers_and_losers():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'price_change_percentage': '7d'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            coins = [c for c in data if c.get('price_change_percentage_7d_in_currency') is not None]
            gainers = sorted(coins, key=lambda x: x['price_change_percentage_7d_in_currency'], reverse=True)[:10]
            losers = sorted(coins, key=lambda x: x['price_change_percentage_7d_in_currency'])[:10]
            return gainers, losers
