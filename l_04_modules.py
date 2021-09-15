from tabulate import tabulate
from utils.create_utils import create_devices

# ------- MAIN PROGRAM -------
if __name__ == '__main__':

    devices = create_devices(num_devices=5, num_subnets=1)
    print("\n", tabulate(devices, headers="keys"))
