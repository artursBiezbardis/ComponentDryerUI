import subprocess
from dotenv import load_dotenv, set_key
import os


class UpdateTpsysCarrierTimeService:

    UPDATE_TIMER_AFTER_DRYING_PATH = "C:\\Users\\arturs.biezbardis\\PycharmProjects\\ComponentDryerUI\\scripts\\run_update_timer_after_drying.sh"  # "../../scripts/run_update_timer_after_drying.sh"
    ENV_UPDATE_CARRIER_ID_PATH = "C:\\Users\\arturs.biezbardis\\PycharmProjects\\ComponentDryerUI\\scripts\\run_env_update_carrierid.sh"  # "../../scripts/run_env_update_carrierid.sh"
    ENV_FILE_PATH = "C:\\Users\\arturs.biezbardis\\PycharmProjects\\ComponentDryerUI\\remote_config\\.env"  # "../../remote_config/.env"
    ENV_KEY = 'CARRIER_ID'

    def __init__(self, carrier_id):

        self.carrier_id = carrier_id[1:]

    def main(self):
        carrier_id_result = self.update_env_carrier_id(self.carrier_id)
        update_result = False
        if carrier_id_result:
            update_result = self. update_carrier_in_remote_db()
        self.update_env_carrier_id('000000')
        return update_result



    def update_env_carrier_id(self, carrier_id):
        set_key(self.ENV_FILE_PATH, self.ENV_KEY, carrier_id)
        load_dotenv(self.ENV_FILE_PATH)
        new_carrier_id = os.getenv('CARRIER_ID')
        if new_carrier_id == carrier_id:
            return True
        else:
            return False

    def update_carrier_in_remote_db(self):
        env_update_result = self.update_script(self.ENV_UPDATE_CARRIER_ID_PATH)
        result = env_update_result
        if env_update_result:
            time_update_result = self.update_script(self.UPDATE_TIMER_AFTER_DRYING_PATH)
            result = time_update_result
        return result

    @staticmethod
    def update_script(path):

        update_done = True
        try:
            result = subprocess.run(
                ["bash", path],
                check=True,
                capture_output=True,
                text=True)
            print("Script output:")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")
            print(f"Script stderr: {e.stderr}")
        else:
            return False

        return update_done
