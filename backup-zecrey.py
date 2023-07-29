import subprocess
from loguru import logger

ADB_CMD = 'adb.exe'

class Zecrey():
    package_id = 'com.zecrey.app'
    profile_code = None
    

    def __init__(self) -> None:
        pass

    def backup(self, output_file):
        # force close app
        logger.debug("Close app ...")
        proc1 = subprocess.Popen([ADB_CMD, "shell", 'am force-stop com.zecrey.app'], stdout=subprocess.PIPE)
        stdout1 = proc1.communicate()[0]
        print(stdout1)

        logger.debug("Backup app ...")
        cmd = f"su -c 'tar -czf /sdcard/Download/zecrey.tar.gz /data/data/{self.package_id} --exclude=lib --exclude=cache --exclude=code_cache'"
        proc2 = subprocess.Popen([ADB_CMD, "shell", cmd], stdout=subprocess.PIPE)
        stdout2 = proc2.communicate()[0]
        print(stdout2)

        logger.debug("Download profile ...")
        cmd3 = f"pull /sdcard/Download/zecrey.tar.gz"
        proc3 = subprocess.Popen([ADB_CMD, "shell", cmd3], stdout=subprocess.PIPE)
        stdout3 = proc3.communicate()[0]
        print(stdout3)

        logger.debug("Remove temp file ...")
        cmd4 = f"rm -f /sdcard/Download/zecrey.tar.gz"
        proc4 = subprocess.Popen([ADB_CMD, "shell", cmd4], stdout=subprocess.PIPE)
        stdout4 = proc4.communicate()[0]
        print(stdout4)

        logger.debug('Finish')


        pass

    def restore(self, input_file):
        cmd = "su -c 'tar -xf /sdcard/Download/zecrey.tar.gz'"
        proc = subprocess.Popen([ADB_CMD, "shell", cmd], stdout=subprocess.PIPE)
        stdout = proc.communicate()[0]
        print(stdout)
        pass
    
    def reset_app(self):
        cmd = f'shell pm clear {self.package_id}'

if __name__ == '__main__':
    zecrey_obj = Zecrey()
    # zecrey_obj.backup("abc.tar.gz")
    zecrey_obj.restore("111")

    
    print('DONE')
