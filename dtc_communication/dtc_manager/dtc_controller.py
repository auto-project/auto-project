from argparse import ArgumentParser
from dtc_lib import Diagnostic_Clear_All_DTC
from dtc_lib import Diagnostic_Raise_DTC
from dtc_lib import Diagnostic_Read_All_DTC
from logger import get_logger


def parse_args() -> dict:
    parser = ArgumentParser()
    parser.add_argument('-dc', '--dtc-content')
    return vars(parser.parse_args())


class DtcController:

    def __init__(self):
        self.logger = get_logger()

    def raise_dtc(self, dtc_content: str):
        self.logger.info('Raising a dtc with content: %s' % dtc_content)
        Diagnostic_Raise_DTC(dtc_content)
        self.logger.info('DTC %s raised.' % dtc_content)

    def clear_all_dtc(self):
        self.logger.info('Clearing all DTCs.')
        Diagnostic_Clear_All_DTC()
        self.logger.info('Clearing finished.')

    def read_all_dtc(self):
        self.logger.info('Reading all DTCs')
        result = Diagnostic_Read_All_DTC()
        self.logger.info('Reading finished DTCs')
        return result


if __name__ == '__main__':
    controller = DtcController()
    args = parse_args()
    controller.raise_dtc(**args)
