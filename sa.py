import yaml
import os

# Load the YAML file at the start of your application
with open('options/train/train_HAT_SRx2_from_scratch.yml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# Access the 'resume_state' variable from the loaded data
resume_state = data['path']['resume_state']

# You can use 'resume_state' in your code
state_files = os.listdir('experiments/train_HAT_SRx2_from_scratch/training_states/')
if len(state_files)!=0:
    latest_state = max(state_files, key=lambda f: int(f.split('.')[0]))

    folder_path = "experiments/train_HAT_SRx2_from_scratch/training_states/"

    latest_state = folder_path + latest_state
# If you want to change the 'resume_state' variable at runtime, simply update it in the 'data' structure
    data['path']['resume_state'] = latest_state
else:
   data['path']['resume_state'] = "~"

# Your code will now use the updated value

# If necessary, you can save the updated data back to the YAML file
with open('options/train/train_HAT_SRx2_from_scratch.yml', 'w') as file:
    yaml.dump(data, file)
