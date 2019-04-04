import os
import unittest
import argparse
from common.ConfigParserUtils import ConfigParserUtils


def execute(caseID):
    suite = unittest.TestLoader().loadTestsFromName(
        'testcase.' + caseID + '.' + caseID)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, help='device serial')
    parser.add_argument('--caseID', type=str, help='caseID')
    args = parser.parse_args()
    config = ConfigParserUtils()
    config.update_value_by_section_and_key(
        'device_config',
        'deviceid',
        args.device)
    config.update_value_by_section_and_key(
        'device_config',
        'caseid',
        args.caseID)
    execute(args.caseID)
    pass
