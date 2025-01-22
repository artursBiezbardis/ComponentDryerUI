import subprocess


class GetTpsysDataService:

    def __init__(self):
        self.get_carrier_data_script_path = 'scripts/run_get_carrier_data.sh'

    def get_data(self):
        try:
            result = subprocess.run(["bash", self.get_carrier_data_script_path], check=True, capture_output=True, text=True)
            print("Script output:")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")
            print(f"Script stderr: {e.stderr}")
