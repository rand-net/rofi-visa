from visa import Visa_Status
import pandas as pd
import argparse

pd.set_option("display.max_rows", None)


#  Command line arguments
# ----------------------------------
parser = argparse.ArgumentParser()
parser.add_argument(
    "resident_country", type=str, help="Current Resident Country",
)

parser.add_argument(
    "-s",
    "--selected",
    help="Visa status for selected Countries in config.yaml ",
    dest="visa_sel",
    action="store_true",
)

parser.add_argument(
    "-f",
    "--visa-free",
    help="Countries not requiring visa",
    dest="visa_free",
    action="store_true",
)

parser.add_argument(
    "-r",
    "--visa-required",
    help="Countries requiring Visa",
    dest="visa_required",
    action="store_true",
)

parser.add_argument(
    "-o",
    "--visa-on-arrival",
    help="Countries offering Visa on arrival",
    dest="visa_voa",
    action="store_true",
)

parser.add_argument(
    "-e",
    "--eta",
    help="Countries offering Electronic Travel Authority",
    dest="visa_eta",
    action="store_true",
)

parser.add_argument(
    "-n",
    "--visa-free-days",
    help="Countries offering visa free days",
    dest="visa_free_days",
    action="store_true",
)

args = parser.parse_args()

current_residency = Visa_Status(
    "passport-index-dataset/passport-index-matrix.csv",
    "config.yaml",
    args.resident_country,
)

if args.visa_sel:
    print(current_residency.get_status_sel())

if args.visa_free:
    print(current_residency.get_status_vf())

if args.visa_required:
    print(current_residency.get_status_vr())

if args.visa_voa:
    print(current_residency.get_status_voa())

if args.visa_eta:
    print(current_residency.get_status_eta())

if args.visa_free_days:
    print(current_residency.get_status_vfe())
