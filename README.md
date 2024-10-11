
# ShapE-TextTo3D-HPC

This project is a text-to-3D model containerized using Singularity and is optimized for execution on high-performance computing (HPC) systems. The model generates 3D shapes based on text prompts and uses GPU acceleration for efficient processing. The project has been successfully tested on the HPC system at [Erlangen National High Performance Computing Center](https://hpc.fau.de/).


This project builds upon the [Shap-E model by OpenAI](https://huggingface.co/openai/shap-e), providing a streamlined way to run text-to-3D conversions within a containerized environment on an HPC platform.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Prerequisites

- Python 3.8+
- GPU with support for CUDA (tested with A100)
- Singularity for container management
- SLURM for job scheduling (optional, but recommended)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/NavidKhezrian/ShapE-TextTo3D-HPC.git
   cd ShapE-TextTo3D-HPC
   ```

2. **Prepare Singularity Container:**

   The project uses a Singularity container defined in `singularity.def`. Build the container using:

   ```bash
   singularity build shap_e.sif singularity.def
   ```

## Usage

### Running the Model

The project can be run using the provided SLURM script (`job.sh`). To submit a job, use the following command:

```bash
sbatch job.sh <output_directory> "<prompt>"
```

- `<output_directory>`: The directory where the generated output will be saved.
- `<prompt>`: The prompt string to be passed to the model.

Example:

```bash
sbatch job.sh 1 "apple"
```

This command will create the `results` directory inside the `output` folder and save the generated output there.

### Running Locally

If you do not wish to use SLURM, you can run the model directly with Singularity:

```bash
singularity run --bind ./output:/user/source/output/ shap_e.sif --prompt "Your prompt here" --output_path /user/source/output/output_directory/
```

Replace `Your prompt here` with the desired input, and `output_directory` with the desired output location.

## File Structure

- `main.py`: The main script for running the model.
- `job.sh`: A SLURM script for job submission.
- `requirements.txt`: Python dependencies.
- `singularity.def`: Singularity container definition file.
- `output/`: Directory where model outputs will be stored.
