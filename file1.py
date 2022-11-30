import yaml

# Read file (It has a single document)
fp = "example1.yml"

with open(fp, "r") as file:
    config = yaml.load(file, Loader=yaml.loader.SafeLoader)

print(config)


# Save data
obj = {
    "flex": {"name": "Steven Daniels", "role": "Data Scientist", "experience": "2 years"},
}

with open("person.yaml", "w") as file:
    yaml.dump(obj, file, default_flow_style=False)


# Read File with multi documents
fp = "example2.yml"
with open(fp, "r") as file:
	config1 = yaml.load_all(file, Loader=yaml.loader.SafeLoader)

	for file in config1:
		print(file)
