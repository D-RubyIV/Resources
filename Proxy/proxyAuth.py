import os
import zipfile




def getpluginfilezip(name, proxy: str) -> os.path:
    PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS = proxy.split(":")
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """% (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
    if not os.path.exists("proxyzip"): os.mkdir("proxyzip")
    cwd = os.getcwd()
    pluginfile = os.path.join(cwd+"\\proxyzip", name+'proxy.zip')
    
    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    return pluginfile
def getpluginfolder(name, proxy: str) -> os.path:
    cwd = os.getcwd()
    path = os.path.join(cwd+"\\proxyzip", name+"proxy")
    with zipfile.ZipFile(getpluginfilezip(name, proxy), 'r') as zip_ref:
        zip_ref.extractall(path)
        zip_ref.close()
    return path
