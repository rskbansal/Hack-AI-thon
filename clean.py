import os

# Set the path to the 'data' folder
data_folder_path = './data'

# Iterate over each file in the 'data' folder
for filename in os.listdir(data_folder_path):
    # Create the full path to the file
    filepath = os.path.join(data_folder_path, filename)
    
    # Check if the file has a '.txt' extension and its size is 0 KB
    if filename.endswith('.txt') and os.path.getsize(filepath) == 0:
        print(f"Removing {filename}...")
        os.remove(filepath)

print("Completed!")
