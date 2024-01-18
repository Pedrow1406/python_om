#  Abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log') 

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Sucess: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        with open(LOG_FILE, 'a') as file:
            file.write(f'{msg} ({self.__class__.__name__})\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    
    log_print = LogPrintMixin()
    log_print.log_error('Essa é a mensagem')
    log_print.log_success('Deu Bom Dms')

    log_file = LogFileMixin()
    log_file._log('Tentativa de Login')
    log_file.log_error('Deu Ruim')
    log_file.log_success('Deu Bom')