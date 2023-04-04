from main_classes.loop_step import Loop_Step, Loop_Step_Config

from utility.add_remove_table import AddRemoveTable
from utility import variables_handling

class Set_Variables(Loop_Step):
    def __init__(self, name='', parent_step=None, step_info=None, **kwargs):
        super().__init__(name, parent_step, step_info, **kwargs)
        self.step_type = 'Set Variables'
        if step_info is None:
            step_info = {}
        self.variables_values = step_info['variables_values'] if 'variables_values' in step_info else {'Variable': [], 'Value': []}

    def get_protocol_string(self, n_tabs=1):
        """If `wait_for_set` is True, then after setting, bps.wait for
        the set group is called."""
        tabs = '\t' * n_tabs
        protocol_string = super().get_protocol_string(n_tabs)
        for i, variable in enumerate(self.variables_values['Variable']):
            val = variables_handling.get_write_from_data_type(self.variables_values['Value'][i])
            protocol_string += f'{tabs}{variable} = eva.eval({val})\n'
            protocol_string += f'{tabs}namespace["{variable}"] = {variable}\n'
        return protocol_string

    def get_protocol_short_string(self, n_tabs=0):
        short_string = super().get_protocol_short_string(n_tabs)
        short_string = f'{short_string[:-1]} - {self.variables_values}\n'
        return short_string


class Set_Variables_Config(Loop_Step_Config):
    def __init__(self, loop_step:Set_Variables, parent=None):
        super().__init__(parent, loop_step)
        self.variables_table = AddRemoveTable(tableData=loop_step.variables_values,
                                              checkstrings=[1])
        self.layout().addWidget(self.variables_table, 1, 0, 1, 5)

    def update_step_config(self):
        super().update_step_config()
        self.loop_step.variables_values = self.variables_table.update_table_data()
