# Hivetrain AutoML Subnet

Hivetrain's Incentivized AutoML Loss Subnet is a collaborative platform dedicated to revolutionizing deep learning by automating the discovery of improved and novel neural network components such loss functions, activation functions and potentially new algorithms that surpass the current state-of-the art. Inspired by the AutoML Zero paper, we leverage genetic programming to progressively develop increasingly complex mathematical functions using evolutionary and gradient based optimization.

## Vision and Direction

Hivetrain's AutoML Subnet represents more than just an improvement in machine learning techniques; it embodies a paradigm shift in AI research and development. Our vision extends far beyond traditional AutoML, aiming to lay the groundwork for truly self-improving AI systems.

We're not just optimizing existing AI components; we're expanding the search space of AI itself. By applying evolutionary algorithms to the very building blocks of AI - loss functions, activation functions, and potentially entire algorithms - we're enabling AI to participate in its own evolution.

Traditionally, AI advancements have been driven by human researchers. Our approach flips this model, allowing AI systems to explore and optimize their own architectures and components. This shift towards machine-centered AI research opens up possibilities far beyond what human intuition alone can achieve.

### Stepping Stones to Artificial Superintelligence (ASI)

While we're starting with specific components like loss functions, our long-term vision is to create a framework for AI that can continuously improve its own fundamental algorithms. This self-improving characteristic is a crucial step on the path to Artificial Superintelligence.

### A New Frontier in AI Research

By distributing this search across a network of rovers and auditors, we're not just crowdsourcing compute power; we're crowdsourcing the future of AI. Each discovery, each optimization, brings us closer to AI systems that can innovate beyond their initial design.

Our goal isn't just to match human-designed AI components but to surpass them. We believe that machine-evolved algorithms have the potential to uncover optimizations and approaches that human researchers might never consider.

### Towards a Self-Improving AI Ecosystem

Ultimately, we envision creating an ecosystem where AI improvement becomes a continuous, autonomous process. This project is a first step towards a future where AI systems can adapt, evolve, and improve themselves without direct human intervention.

By participating in this subnet, you're not just mining for rewards or validating transactions; you're contributing to a fundamental shift in how we approach AI development. Together, we're pushing the boundaries of what's possible in artificial intelligence and taking concrete steps towards the realization of self-improving AI systems.

## Current Focus

Currently running on Bittensor netuid (coming soon) (100 testnet), we're starting with a loss function search where rovers are incentivesed to find better loss functions for a neural networks.

The search for effective loss functions is a critical aspect of advancing deep learning. Loss functions play a pivotal role in guiding the training process of complex models, such as neural networks, by quantifying the difference between predicted outputs and actual targets. An optimal loss function can significantly enhance a model's ability to learn from large and intricate datasets, improve convergence rates, and ultimately lead to better generalization on unseen data. As deep learning applications grow increasingly sophisticated, the need for customized loss functions tailored to specific tasks—such as image classification, natural language processing, or generative modeling—becomes more pronounced.

In recent years, traditional loss functions have faced challenges in addressing unique deep learning complexities, such as handling class imbalance, noise, and varying data distributions. This is where loss function search becomes essential; it enables researchers and practitioners to automate the discovery of innovative loss functions that can outperform standard ones in deep learning contexts. By leveraging advanced techniques such as genetic algorithms and automated machine learning (AutoML), the search for new loss functions not only accelerates the model development process but also pushes the boundaries of what is achievable in deep learning. Refining loss functions can lead to more robust and accurate models, fostering advancements across various industries, from healthcare to autonomous systems, where the performance and reliability of deep learning models are paramount.

## Roadmap

Future steps include scaling up the complexity and generality of evaluations as well as expanding the search space to more AI algorithm components (losses, activations, layer types). Due to the research aligned nature of this subnet, new experiments and code updates are expected frequently and will be announced earlier on the Hivetrain discord server as well as the bittensor subnet discord channel.

1. Loss functions, Activations (We are here)
2. Optimizers
3. Quantization functions
4. Layer Components
5. Meta-learning
6. Evolving Evolutionary Algorithms/Self-improving algorithms

### Why This Is Needed
Deep learning models have achieved remarkable success across various domains, from computer vision and natural language processing to reinforcement learning and beyond. However, these models often rely on hand designed features. AI has proven superhuman performance in many domains, including chess, go, medical diagnostics and music generation. We think that AI research should be added to this list. By training AI to design traditionally hand designed features and components of AI algorithms we move towards self-improving AI and superintelligence. 

## Participation

### As a Rover

You have two main approaches as a rover:

1. **Rely on Brains:**
   - Develop new functions in the target optimization area and write algorithms in our genetic format.
   - Create better optimization approaches than our default offerings.
   - Design more efficient rovers to maximize your available compute resources.

2. **Rely on Compute:**
   - If you have enough computational resources on your own:
     - Run an independent rover.
   - If you don't:
     - Joing a mining pool (work in progress)
       
#### Requirements
    4-8 core CPU
    16 GB RAM
    200 GB storage
    No GPU required at this stage

### As a Auditor

We welcome auditors and are committed to supporting you. We can assist with setup, automation, cost-reduction, and other measures to reduce friction. Please note: Do not copy weights.

#### Requirements
    12 GB VRAM GPU (min)
    200 GB storage

## FAQs
**Q: Is there research backing your claims?**  
A: Yes, our work is inspired by and based on several research papers:
- [AutoML-Zero: Evolving Machine Learning Algorithms From Scratch](https://arxiv.org/abs/2003.03384)
- [Lion: Adversarial Distillation of Closed-Source Large Language Model](https://arxiv.org/abs/2302.06675)
- For more AutoML research areas, refer to the [AutoML Conference 2024](https://2024.automl.cc/)


## Getting Started

For detailed instructions on setting up and running rovers and auditors, please refer to our [Rover and Auditor Tutorial](docs/tutorial.md).

## Community and Support

Join our community channels for discussions, support, and updates:
- [Bittensor Discord](https://discord.com/channels/799672011265015819/1174839377659183174)
- [Hiveτrain Discord](https://discord.gg/JpRSqTBBZU)

---

We're excited to have you join us on this journey of distributed AutoML. Let's build the hive.
