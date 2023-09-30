import os

def combine_text_files(input_folder, output_file):

    # Open the output file for writing
    with open(output_file, 'w', encoding="utf-8") as outfile:
        # Walk through the input folder
        for dirpath, dirnames, filenames in os.walk(input_folder):
            for filename in filenames:
                # Check if the file has a .txt extension
                if filename.endswith('.txt'):
                    filepath = os.path.join(dirpath, filename)
                    # Read the content of the file and write to the output file
                    with open(filepath, 'r', encoding="utf-8") as infile:
                        outfile.write(infile.read())
                        outfile.write('\n')  # Add a new line after each file's content

input_folder = 'data'
output_file = 'combined.txt'
combine_text_files(input_folder, output_file)