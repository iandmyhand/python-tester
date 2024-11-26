import json


def beautify_json(input_file, output_file=None):
    """
    Beautifies the given JSON file.

    :param input_file: Path to the input JSON file.
    :param output_file: Path to save the beautified JSON file.
                        If None, overwrites the input file.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        output_file = output_file or input_file

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, sort_keys=True)

        print(f"Beautified JSON saved to: {output_file}")

    except Exception as e:
        print(f"Error beautifying JSON: {e}")


# Replace with the path to your JSON file
input_file_path = "temp/input.json"
# Replace with your desired output path or None to overwrite
output_file_path = "temp/output.json"

beautify_json(input_file_path, output_file_path)
