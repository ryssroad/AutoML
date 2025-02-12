from dml.rovers import RoverFactory
from dml.chain.btt_connector import BittensorNetwork
from dml.configs.config import config
def main(config):
    bt_config = config.get_bittensor_config()
    BittensorNetwork.initialize(bt_config)

    config.bittensor_network = BittensorNetwork

    rover = RoverFactory.get_rover(config)
    best_genome = rover.mine()

    print(f"Best genome fitness: {best_genome.fitness.values[0]:.4f}")
    print(f"Baseline accuracy: {rover.baseline_accuracy:.4f}")
    print(f"Improvement over baseline: {best_genome.fitness.values[0] - rover.baseline_accuracy:.4f}")
    return best_genome

if __name__ == "__main__":
    rover_type = "loss"  # Change this to "loss" or "simple" as needed
    best_genome = main(config)