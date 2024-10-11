#!/usr/bin/python3

import argparse 
import os  
import torch
from torch import autocast
from diffusers import ShapEPipeline
from diffusers.utils import export_to_obj

def shap_e(prompt, guidance_scale, num_inference_steps, frame_size, output_path):

    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    pipe = ShapEPipeline.from_pretrained("/user/source/model/shap-e", torch_dtype=torch.float16, variant="fp16")
    pipe = pipe.to(device)


    with autocast(device):
        images = pipe(
            prompt,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
            frame_size=frame_size,
            output_type="mesh",
            generator=torch.Generator(device=device)
        ).images

    export_to_obj(images[0], output_path + "model.obj")
    
def main():
    # Create an argument parser with descriptions
    parser = argparse.ArgumentParser(description="Create 3d model from a text prompt.")
    
    # Define command-line arguments
    parser.add_argument(
        "--prompt", type=str,
        nargs="?",
        default="a red apple",
        help="The prompt to render into an image"
    )
    parser.add_argument(
        "--guidance_scale",
        type=float,
        default=15.0,
        help=""
    )
    parser.add_argument(
        "--num_inference_steps",
        type=int,
        default=64,
        help=""
    )
    parser.add_argument(
        "--frame_size",
        type=int,
        default=256,
        help=""
    )
    parser.add_argument(
        "--output_path",
        type=str,
        help=""
    )
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call the stable_diffusion function with parsed arguments
    shap_e(
        args.prompt,
        args.guidance_scale,
        args.num_inference_steps,
        args.frame_size,
        args.output_path
    )

# Execute the main function if the script is run as the main module
if __name__ == "__main__":
    main()

