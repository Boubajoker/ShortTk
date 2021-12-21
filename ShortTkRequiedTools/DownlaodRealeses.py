# ShortTk DownlaodRealeses shell Copyright (c) Boubajoker 2021. All right reserved. Project under MIT License.

import sys
from typing import Any, NoReturn
import os
import webbrowser
from lib import Shell

help_msg = """<!--Buildit-in update shell for short_tk--!>

This is a simple shell for downlaod last realeses of short_tk.
                        Here are the commands:
/*-------------------------------------------------------------*/
h: to get help about this shell (the command that you're typed one second ago.)\n
h --online: Get redirected to the web documentation of short_tk.\n
short_tk --update: for update to the last stable realese.\n
get --path: get actual path.\n
quit: quit the shell.\n
setup --setup: setup the requied tools to download updates.\n
setup --info: get infos about how the update shell works.
/*-------------------------------------------------------------*/
"""
class Update(object):
    def __init__(self) -> Any:
        super(object).__init__()
        self.running = True
        print(Shell.Messages.main_msg)
        
        while self.running:
            self.command_entry = input(f"{os.system(Shell.Components.cd_command)} ~{sys.platform}->")

            if self.command_entry == Shell.Commands.get_help:
                print(help_msg)
            
            elif self.command_entry == Shell.Commands.get_online_help:
                webbrowser.open_new_tab(Shell.Components.doc_url)
            
            elif self.command_entry == Shell.Commands.update_module:
                print(Shell.Messages.downlaod_msg)
                Shell.Downlaod_Module(self)

            elif self.command_entry == Shell.Commands.setup_shell:
                os.system(Shell.Components.install_requests_command)
            
            elif self.command_entry == Shell.Commands.get_setup_info:
                print(Shell.Messages.setup_info)

            elif self.command_entry == Shell.Commands.quit_command:
                self.running = False
            
            elif self.command_entry == Shell.Commands.get_path:
                os.system(Shell.Components.cd_command)
        
            elif self.command_entry == Shell.Commands.whoami:
                os.system(Shell.Commands.whoami)

            else:
                print(f"[ERROR]:\'{self.command_entry}\' is not defined.")


__version__ = "0.0.1 Alpha A-1"
__all__ = [
    "Shell",
    "Downlaod",
    "Realeses",
    "Downlaod Realeses"
]

if __name__ == '__main__':
    Update()