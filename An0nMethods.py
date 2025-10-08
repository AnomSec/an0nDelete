from pathlib import Path
import os
class An0n:
    @staticmethod
    def isFile(path: str) -> bool:
        return Path(path).is_file()
    @staticmethod
    def isDir(path: str) -> bool:
        return Path(path).is_dir()
    @staticmethod
    def deleteFile(path: str, passes = 3):
        print(f"deleting {path}...")
        file_size = os.path.getsize(path)
        for pass_num in range(passes):
            random_data = os.urandom(file_size)
            with open(path, 'wb') as f:
                f.write(random_data)
            print(f" - {pass_num + 1}/{passes} completed.")
        os.remove(path)

    def deleteDir(self,path,passes=3):
        directory = Path(path)
        for item in directory.glob("*"):
            self.deleteFile(str(item),passes)
        os.rmdir(path)