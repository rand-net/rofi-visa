import pandas as pd
import yaml


class Visa_Status:
    def __init__(self, index_file_path, yaml_file_path, resident_country):
        self.index_file_path = index_file_path
        self.yaml_file_path = yaml_file_path
        self.resident_country = resident_country

        # Generate Country dataframe
        # --------------------------
        passport_df = pd.read_csv(self.index_file_path)

        # Transpose the selected data
        country_data_df = passport_df[
            passport_df["Passport"] == resident_country
        ].transpose()  # Select
        country_data_df = country_data_df.iloc[1:]  # Delete first two rows

        # Reset the index and rename the column names
        country_data_df = country_data_df.reset_index()
        country_data_df.columns = ["Country", "Status"]
        self.country_data_df = country_data_df

    def get_status_sel(self):
        """Get Visa requirements for  different Countries"""

        # Read Countries from config.yaml
        with open(self.yaml_file_path, "r") as stream:
            try:
                countries_list = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print("No countries.yaml to read!")

        # Filter results based on the Countries in config.yaml
        countries_list = countries_list["Countries"]
        result_df = self.country_data_df[
            self.country_data_df["Country"].isin(countries_list)
        ]
        return result_df

    def get_status_vf(self):
        """Get Countries that doesn't need a Visa """

        visa_free_df = self.country_data_df[
            self.country_data_df["Status"] == "visa free"
        ]
        return visa_free_df

    def get_status_vr(self):
        """Get Countries that needs a Visa"""

        visa_required_df = self.country_data_df[
            self.country_data_df["Status"] == "visa required"
        ]
        return visa_required_df

    def get_status_voa(self):
        """Get Countries that permits Visa On Arrival"""

        visa_on_arrival_df = self.country_data_df[
            self.country_data_df["Status"] == "visa on arrival"
        ]
        return visa_on_arrival_df

    def get_status_eta(self):
        """Get Countries offering Electronic Travel Authority"""

        # eta - electronic travel authority
        visa_eta_df = self.country_data_df[self.country_data_df["Status"] == "e-visa"]
        return visa_eta_df

    def get_status_vfe(self):
        """Get Countries offering Visa Free Days """

        visa_free_days_df = self.country_data_df[
            pd.to_numeric(self.country_data_df["Status"], errors="coerce").notnull()
        ]
        return visa_free_days_df
