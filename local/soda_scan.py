import os
from soda.scan import Scan

for f in os.listdir("soda-checks"):
    s = Scan()
    s.add_configuration_yaml_file(file_path="soda-config/config.yaml")
    dataset = f.split(".")[0]
    s.set_data_source_name(dataset)
    s.add_sodacl_yaml_file(f"soda-checks/{f}")
    s.execute()

    print(scan.get_scan_results())