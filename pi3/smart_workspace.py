from i3ipc import Connection
import sys
import pynput
import re
import argparse
import pprint
import subprocess


def get_active_outputs():
    ps = subprocess.Popen(('xrandr', '--listmonitors'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('awk', "{print $4}"), stdin=ps.stdout)
    ps.wait()
    return [x for x in output.decode('UTF-8').split('\n') if x is not None and x != '']


names_for_outputs = r'(' + '|'.join(get_active_outputs()) + ')'


class WorkSpacer:

    def __init__(self, args):
        self.i3 = None
        self.args = args
        self.workspaces_on_outputs = {}
        self.workspaces = None
        self.outputs = None
        self.config = None
        self.mouse = pynput.mouse.Controller()
        self.mouse_position = None
        self.current_output_name = None

    def _connect(self):
        self.print_if_debug('All available outputs on device')
        self.print_if_debug(names_for_outputs)
        try:
            self.i3 = Connection()
            self.config = self.i3.get_config().__dict__['config']
            config_outputs = {}
            for matchNo, match in enumerate(
                    re.finditer(r'set (\$[a-zA-Z]+) (' +
                                names_for_outputs + ')', self.config, re.MULTILINE), start=1
            ):
                config_outputs[match.group(1)] = match.group(2)
            self.print_if_debug('All outputs listed in the config, matched on available configs')
            self.print_if_debug(config_outputs)
            config_workspace_names = {}
            for matchNum, match in enumerate(
                    re.finditer(r'set (\$.*) (\d.*)', self.config, re.MULTILINE)
            ):
                config_workspace_names[match.group(1)] = match.group(2)
            self.print_if_debug('All config_workspaces_names')
            self.print_if_debug(config_workspace_names)

            for matchNum, match in enumerate(
                    re.finditer(r'workspace (\$.*) output (\$.*)', self.config, re.MULTILINE)
            ):
                if not config_outputs.keys().__contains__(match.group(2)):
                    continue  # Not an active display, skip it
                if not self.workspaces_on_outputs.keys().__contains__(config_outputs[match.group(2)]):
                    self.workspaces_on_outputs[config_outputs[match.group(2)]] = []
                self.workspaces_on_outputs[config_outputs[match.group(2)]].append(
                    config_workspace_names[match.group(1)])
            self.print_if_debug("All workspaces with outputs")
            self.print_if_debug(self.workspaces_on_outputs)

        except Exception as exc:
            if self.args.debug:
                raise exc
            sys.exit(1)
        self.workspaces = [workspaces for workspaces in self.i3.get_workspaces()]
        outputs = self.i3.get_outputs()
        self.outputs = [output for output in outputs if output.__dict__["active"] is True]

    def run(self):
        self._connect()
        self.mouse_position = self.mouse.position
        self.current_output_name = self._get_workspace_from_courser_position()

        if self.args.shift:
            self.i3.command(
                f'move container to workspace {self.workspaces_on_outputs[self.current_output_name][self.args.index - 1]}')
            if not self.args.keep_with_it:
                return
        self.i3.command(f'workspace {self.workspaces_on_outputs[self.current_output_name][self.args.index - 1]}')

    def _get_workspace_from_courser_position(self):
        for output in self.outputs:
            width = output.__dict__["rect"].__dict__["width"]
            height = output.__dict__["rect"].__dict__["height"]
            x_offset = output.__dict__["rect"].__dict__["x"]
            y_offset = output.__dict__["rect"].__dict__["y"]

            if x_offset == 0 and y_offset == 0:
                if x_offset <= self.mouse_position[0] <= x_offset + width and y_offset <= \
                        self.mouse_position[1] <= y_offset + height:
                    return output.__dict__["name"]
            elif x_offset == 0:
                if x_offset <= self.mouse_position[0] <= x_offset + width and y_offset < \
                        self.mouse_position[1] <= y_offset + height:
                    return output.__dict__["name"]
            elif y_offset == 0:
                if x_offset < self.mouse_position[0] <= x_offset + width and y_offset <= \
                        self.mouse_position[1] <= y_offset + height:
                    return output.__dict__["name"]
            else:
                if x_offset < self.mouse_position[0] <= x_offset + width and y_offset < \
                        self.mouse_position[1] <= y_offset + height:
                    return output.__dict__["name"]

    def _get_workspaces_for_output(self, output):
        return [workspace for workspace in self.workspaces if workspace.__dict__['output'] == output]

    def print_if_debug(self, to_print):
        if self.args.debug:
            pprint.pprint(to_print)


def main():
    parser = argparse.ArgumentParser(
        description="Changes the workspace, based on what output your cursor is on."
    )
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Turn on debug mode.')

    required_group = parser.add_argument_group('Required', '')
    required_group.add_argument("-i", "--index", type=int, required=True,
                                help="The indexed workspace for the output where the cursor is currently located")

    shift_group = parser.add_argument_group('Shift', 'manipulate the active window')
    shift_group.add_argument("-s", "--shift", action='store_true',
                             help="Moves the active window to the index workspace")
    shift_group.add_argument('-k', '--keep-with-it', action='store_true',
                             help='Moves the active window to the index workspace, and moves with it')
    # pprint.pprint(parser.parse_args().__dict__)
    WorkSpacer(parser.parse_args()).run()


if __name__ == '__main__':
    main()
