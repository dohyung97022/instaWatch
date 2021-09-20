class InternetSetting:
    location: str = r'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings'
    proxy_enable: int = 0
    proxy_server: str = 'socks=localhost:4444'

    @classmethod
    def set_proxy_enable_cmd(cls, on: bool) -> list[str]:
        cls.proxy_enable = int(on)
        return ['REG', 'ADD', cls.location, '/v', 'proxyEnable', '/t', 'REG_DWORD', '/d', str(cls.proxy_enable), '/f']

    @classmethod
    def set_proxy_server_cmd(cls) -> list[str]:
        return ['REG', 'ADD', cls.location, '/v', 'proxyServer', '/t', 'REG_SZ', '/d', cls.proxy_server, '/f']
