try:
    import asyncio
    import aiohttp

    from pystyle import Write, Colors, Colorate
    from aiosocksy.connector import ProxyConnector
    from concurrent.futures import ThreadPoolExecutor
except ModuleNotFoundError:
    import os

    os.system('pip install aiohttp')
    os.system('pip install aiosocksy')
    os.system('pip install pystyle')

    import asyncio
    import aiohttp

    from pystyle import Write, Colors, Colorate
    from aiosocksy.connector import ProxyConnector
    from concurrent.futures import ThreadPoolExecutor

async def ProxyGen(Amount:int):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={}&country=all'.format(Amount)) as resp:
            text = await resp.text()

            proxies = text.split()
            proxies = [f'http://{proxy}' for proxy in proxies]
            valid_proxies = []

            for proxy in proxies:
                try:
                    async with session.head(proxy) as proxy_test:
                        if proxy_test.status in [502,400]:
                            pass
                        else:
                            valid_proxies.append(proxy)
                except:
                    pass

            with open('Data/proxies.txt','w') as f:
                f.write('\n'.join(valid_proxies))

            Write.Print('Generated {} valids!'.format(len(valid_proxies)), color=Colors.rainbow,interval=0.025)
            await asyncio.sleep(5)

amt = Write.Input('[A-P] Amount Of Proxies: ',color=Colors.rainbow,interval=0.025)

asyncio.run(ProxyGen(int(amt)))