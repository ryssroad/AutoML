import argparse
import logging

from dml.auditors import AuditorFactory
from dml.chain.btt_connector import BittensorNetwork
from dml.chain.chain_manager import ChainManager
from dml.chain.hf_manager import HFManager
from dml.configs.config import config


def setup_logging(log_file="auditor.log"):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main(config):
    # Initialize Bittensor Network
    setup_logging()
    logging.info(f"Starting auditor of type: {config.Auditor.auditor_type}")
    bt_config = config.get_bittensor_config()
    BittensorNetwork.initialize(bt_config)

    config.bittensor_network = BittensorNetwork

    # Initialize Chain Manager and HF Manager
    config.chain_manager = ChainManager(
        subtensor=BittensorNetwork.subtensor,
        subnet_uid=bt_config.netuid,
        wallet=BittensorNetwork.wallet,
    )

    # Create and start auditor
    auditor = AuditorFactory.get_auditor(config)
    logging.info("Starting periodic validation")
    auditor.start_periodic_validation()


if __name__ == "__main__":
    auditor_type = "loss"  # Change this to "loss" as needed
    main(config)
