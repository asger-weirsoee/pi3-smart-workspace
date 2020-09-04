from i3ipc import connection, Connection
import logging
import sys
from pprint import pprint
import pynput
import re
import asyncio

"""import argparse
"""

logger = logging.getLogger(__name__)


class WorkSpacer:

    def __init__(self, args):
        self.i3 = None
        self.args = args
        self.workspaces_on_outputs = None
        self.workspaces = None
        self.outputs = None

        self.mouse = pynput.mouse.Controller()

        self.mouse_position = None
        self.current_output_name = None

    def _connect(self):
        try:
            self.i3 = Connection()
            re.compile(r'')
            self.workspaces_on_outputs = [ws for ws in self.i3.get_config().__dict__['config'].split('\n') if ws]
        except Exception as exc:
            logger.error(f"Could not load i3: {exc}", exc_info=exc)
            sys.exit(1)
        self.workspaces = [workspaces for workspaces in  self.i3.get_workspaces()]
        outputs =  self.i3.get_outputs()
        #pprint(outputs[1].__dict__)
        self.outputs = [output for output in outputs if output.__dict__["active"] is True]

    def run(self):
        self._connect()
        self.mouse_position = self.mouse.position
        self.current_output_name = self._get_workspace_from_courser_position()

    def _get_workspace_from_courser_position(self):
        for output in self.outputs:
            width = output.__dict__["rect"].__dict__["width"]
            height = output.__dict__["rect"].__dict__["height"]
            x_offset = output.__dict__["rect"].__dict__["x"]
            y_offset = output.__dict__["rect"].__dict__["y"]

            if x_offset == 0 and y_offset == 0:
                if x_offset <= self.mouse_position[0] <= x_offset + width and y_offset <= self.mouse_position[1] <= y_offset + height:
                    return output.__dict__["name"]
            elif x_offset == 0:
                if x_offset <= self.mouse_position[0] <= x_offset + width and y_offset < self.mouse_position[1] <= y_offset + height:
                    return output.__dict__["name"]
            elif y_offset == 0:
                if x_offset < self.mouse_position[0] <= x_offset + width and y_offset <= self.mouse_position[1] <= y_offset + height:
                    return output.__dict__["name"]
            else:
                if x_offset < self.mouse_position[0] <= x_offset + width and y_offset < self.mouse_position[1] <= y_offset + height:
                    return output.__dict__["name"]

    def _get_workspaces_for_output(self, output):
        return [workspace for workspace in self.workspaces if workspace.__dict__['output'] == output]


def tst():
    ws = WorkSpacer('')
    ws.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tst()


