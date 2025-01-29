import os
import importlib.util

def execute_get_supported_devices(directory):
    results = {}
    for file_name in os.listdir(directory):
        if file_name.endswith(".py") and file_name != os.path.basename(__file__):
            file_path = os.path.join(directory, file_name)
            module_name = os.path.splitext(file_name)[0]

            # Dynamically load the module
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                print(f"Executing getSupportedDevices for {file_name}")

                # Check if the method exists and call it
                if hasattr(module, "getSupportedDevices"):
                    try:
                        result = module.getSupportedDevices()
                        results[file_name] = result
                    except Exception as e:
                        results[file_name] = f"Error: {e}"
    return results


# Specify the directory containing the Python scripts
script_directory = "./rom_connectors"

# Execute and print results
outputs = execute_get_supported_devices(script_directory)
for script, output in outputs.items():
    print(f"{script}: {output}")
    
# output to a file
with open("supported_devices.txt", "w") as f:
    for script, output in outputs.items():
        f.write(f"{script}: {output}\n")