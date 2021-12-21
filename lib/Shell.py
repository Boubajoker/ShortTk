# ShortTk DownlaodRealeses shell lib Copyright (c) Boubajoker 2021. All right reserved. Project under MIT License.

from typing import Any

class Messages:
    main_msg = "Buildit-in shell for ShortTk Copyright (c) Boubajoker 2021. All right reserved. Project under MIT License. type h for get help about commands"
    downlaod_msg = "[INFO]: Downlaoding last stable realese of short_tk module from \'https://boubajoker.github.io/ShortTk/\'..."
    setup_info = "the setup command is for setup the requied tools to update short_tk. You may restart the shell for waiting the setup is completly downlaoded and installed after typed \'setup --setup\'"

class Commands:
    get_help = "h"
    get_online_help = "h --online"
    update_module = "short_tk --update"
    setup_shell = "setup --setup"
    get_setup_info = "setup --info"
    quit_command = "quit"
    get_path = "get --path"
    whoami = "whoami"

class Components:
    doc_url = "https://boubajoker.github.io/ShortTk/"
    install_requests_command = "pip install requests"
    cd_command = "cd"

def Error503(self) -> Any:
    self.error_503_msg = print("[ERROR]: 503: Not implemented")

def Error404(self) -> Any:
    self.error_404_msg = print("[ERROR]404, file not found")

def Downlaod_Module(self) -> Any:
    import requests

    downloadUrl = 'https://boubajoker.github.io/ShortTk/assets/others/short_tk.zip'

    req = requests.get(downloadUrl)
    filename = req.url[downloadUrl.rfind('/')+1:]

    with open(filename, 'wb') as f:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    def download_file(url, filename=''):
        try:
            if filename:
                pass            
            else:
                filename = req.url[downloadUrl.rfind('/')+1:]

            with requests.get(url) as req:
                with open(filename, 'wb') as f:
                    for chunk in req.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                return filename
        except Exception as e:
            print(e)
            return None