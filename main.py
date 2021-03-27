import csv
from SharedLibrary.env_utils import get_env_parameters
from SharedLibrary.csv_reader_utils import csv_to_dataframe
from SharedLibrary.qrcode_utils import get_qrcode


def main() -> None:
    qrcode_folder, csv_path = get_env_parameters()
    df = csv_to_dataframe(csv_path)
    for index, row in df.iterrows():
        get_qrcode(qrcode_folder, row['URL'], row['Category'])


if __name__ == '__main__':
    main()
