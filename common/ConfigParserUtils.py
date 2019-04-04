from configparser import ConfigParser
import os


class ConfigParserUtils():
    conf = ConfigParser()
    def __init__(self):
        dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #os.chdir(dir_name)
        self.file_path = dir_name + os.sep + 'config' + os.sep + 'case_config.ini'

    def get_config_value_by_key(self, section, key):
        self.conf.read(self.file_path)
        # 获取指定的section， 指定的option的值
        key_value = self.conf.get(section, key)
        print('获取%s 节点，%s 的值为 %s' % (section, key, key_value))
        return key_value

    # 获取所有的section
    def get_all_sections_from_config_file(self):
        self.conf.read(self.file_path)
        sections = self.conf.sections()
        return sections

    # 更新指定section, option的值
    def update_value_by_section_and_key(
            self,  section_name, key, key_value):
        self.conf.read(self.file_path)
        self.conf.set(section_name, key, key_value)
        self.conf.write(open(self.file_path, 'w'))

    def get_section_value(self, section):
        self.conf.read(self.file_path)
        value = self.conf.items(section)
        print(value)


if __name__ == '__main__':
    C = ConfigParserUtils()
    C.get_config_value_by_key(
        'device_config',
        'deviceid')
    C.get_section_value('config' + os.sep + 'case_config.ini', 'device_config')
