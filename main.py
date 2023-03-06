try:
    import asyncio
    import aiohttp

    from pystyle import Write, Colors, Colorate
    from aiosocksy.connector import ProxyConnector
    from concurrent.futures import ThreadPoolExecutor
    
except ModuleNotFoundError as error:
    import os

    os.system('pip install aiohttp')
    os.system('pip install aiosocksy')
    os.system('pip install pystyle')

async def Spammer(msg: str):

    with open('Data/proxies.txt','r') as proxy_put:
        proxies = proxy_put.readlines()

    for proxy in proxies:
        if '\n' in proxy:
            proxy.replace('\n','')

        async with aiohttp.ClientSession(connector=ProxyConnector(proxy)) as session:
            with ThreadPoolExecutor(max_workers=len(proxies)) as executor:

                tasks = []

                for i in range(len(proxies)):
                    task = await asyncio.get_running_loop().run_in_executor(
                        executor,
                        lambda: session.post(
                            "https://discord.com/api/webhooks/1082150850853617674/JgD268YEaTPe-VKLfBy5Nzpfyt3e7EcDENQBslEss1X2rpeaV0jhcO2lHlJOKCq3WZtu",
                            json={'content': msg}
                            )
                    )

                    tasks.append(task)

                await asyncio.gather(*tasks)

print(
    Colorate.Vertical(
        Colors.white_to_black,
        '''██████╗  ██████╗ ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝'''
    )
)
msg = Write.Input('\n\n[PH] Message: ',color=Colors.rainbow,interval=0.025)

asyncio.run(Spammer(msg))
