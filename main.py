import shutil
import logging
from pathlib import Path
from datetime import datetime
from time import perf_counter

def main():
    # Change here
    source = r"C:/Source"  
    destination = (
        "D:/",
        "E:/",
    )  

    logging.basicConfig(
        filename="./logs/backup.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    for dest in destination:
        backup_folder = Path(dest) / f"backup_{datetime.now():%Y_%m_%d}"

        print(f"Starting backup => {backup_folder}...")
        start = perf_counter()

        logging.info(
            f"event=backup_started | source={source} | target={backup_folder}"
        )

        try:
            shutil.copytree(
                source,
                backup_folder,
                dirs_exist_ok=True
            )

            duration = perf_counter() - start

            logging.info(
                f"event=backup_finished | target={backup_folder} | time={duration:.2f}s"
            )
            print(f"Finished backup successfully! ({duration:.2f}s)")
        except shutil.Error as e:
            for src_name, dst_name, error in e.args[0]:
                logging.error(
                    f"event=copy_failed | src={src_name} | dest={dst_name} | error={error}"
                )
        except Exception as e:
            logging.error(f"event=copy_failed | error={e}")
            print("Backup failed.")

if __name__ == "__main__":
    main()