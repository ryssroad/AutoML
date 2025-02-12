import argparse
import bittensor as bt
import json
import subprocess
from dml.configs.config import config
from rover import main as rover_main
from auditor import main as auditor_main
import multiprocessing

def run_node(node_type, wallet_info, config):
    if node_type == "rover":
        config.Bittensor.wallet_name = wallet_info['coldkey_name']
        config.Bittensor.wallet_hotkey = wallet_info['hotkey_name']
        config.gene_repo = "mekaneeky/"+wallet_info['hf_repo']
        rover_main(config)
         
    elif node_type == "auditor":
        
        config.Bittensor.wallet_name = wallet_info['coldkey_name']
        config.Bittensor.wallet_hotkey =  wallet_info['hotkey_name']
        config.gene_repo = "mekaneeky/"+wallet_info['hf_repo']
        auditor_main(config)
        
    else:
        raise ValueError(f"Invalid node type: {node_type}")


def load_wallet_info(file_path):
    with open(file_path, 'r') as file:
        wallet_data = json.load(file)
    return wallet_data

def main():
    parser = argparse.ArgumentParser(description='Script to launch multiple rovers and auditors.')
    parser.add_argument('--wallet_info_file', required=True, help='Path to the wallet info JSON file')
    parser.add_argument('--n_rovers', type=int, default=5, help='Number of rovers to launch')
    parser.add_argument('--n_auditors', type=int, default=1, help='Number of auditors to launch')

    args = parser.parse_args()
    rover_count = 0
    auditor_count = 0
    # Load wallet info
    wallet_info_list = load_wallet_info(args.wallet_info_file)

    processes = []

    if args.n_rovers > 0:
        rover_wallet_info = wallet_info_list[:args.n_rovers]
        for rover_wallet in rover_wallet_info:
            config_node = config()
            config_node.metrics_file = f"rover_{rover_count}.csv"
            rover_count += 1
            p = multiprocessing.Process(target=run_node, args=("rover", rover_wallet, config_node))
            p.start()
            processes.append(p)

    if args.n_auditors > 0:
        auditor_wallet_info = wallet_info_list[89:89 + args.n_auditors]
        for auditor_wallet in auditor_wallet_info:
            config_node = config()
            config_node.metrics_file = f"auditor_{auditor_count}.csv"
            auditor_count += 1
            p = multiprocessing.Process(target=run_node, args=("auditor", auditor_wallet, config_node))
            p.start()
            processes.append(p)

if __name__ == '__main__':
    main()