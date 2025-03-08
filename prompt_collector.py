#!/usr/bin/env python3
import os
import glob

def main():
    # Get user input for filename
    output_filename = input("Enter a name for the output file: ")
    
    # Make sure the output filename has a .txt extension
    if not output_filename.endswith('.txt'):
        output_filename += '.txt'
    
    # Ensure output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create output file path
    output_path = os.path.join(output_dir, output_filename)
    
    # Get all text files from STORY directory
    prompt_files = glob.glob("STORY/*.txt")
    
    # Sort files to ensure they are processed in order
    prompt_files.sort()
    
    if not prompt_files:
        print("No prompt files found in the STORY directory.")
        return
    
    # Open output file for writing
    with open(output_path, "w") as output_file:
        for i, file_path in enumerate(prompt_files):
            # Read content from prompt file
            with open(file_path, "r") as prompt_file:
                content = prompt_file.read().strip()
                
            # Write content to output file
            output_file.write(content)
            
            # Add newline if not the last file
            if i < len(prompt_files) - 1:
                output_file.write("\n")
    
    # Display success message
    print(f"Success! All prompts have been copied to {output_path}")
    print("You can now delete the contents of the STORY directory and add new prompt files to start again.")

if __name__ == "__main__":
    main()
