import logging
import subprocess

LOGGER = logging.getLogger(__name__)


class Command():
    @staticmethod
    def run(cmd, cwd: str = None) -> iter:
        LOGGER.info(f"Running command '{cmd}'...")
        proc = subprocess.Popen(
            cmd, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
        lines = iter(proc.stdout.readline, '')
        return map(Command.to_html, lines)

    @staticmethod
    def to_html(line: str) -> str:
        return '<br/>'.join(line.splitlines() + [''])
