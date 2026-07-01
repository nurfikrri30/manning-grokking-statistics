import os
import re


def bump_file_numbers(directory=".", prefix="4", threshold=9):
    """
    Bumps the numbering of files matching the pattern {prefix}_{number}_*.

    Args:
        directory (str): The path to the folder containing the files.
        prefix (str): The prefix before the incrementing number (e.g., '4').
        threshold (int): The starting number to bump (e.g., 9 bumps 9 and above).
    """

    # Regex to capture the prefix, the number, and the rest of the filename
    # Example match: "4_9_cdf_plot.png" -> group 1: "9", group 2: "cdf_plot.png"
    pattern = re.compile(rf'^{prefix}_(\d+)_(.*)$')

    files = os.listdir(directory)
    files_to_rename = []

    # 1. Identify and filter target files
    for filename in files:
        match = pattern.match(filename)
        if match:
            current_num = int(match.group(1))
            if current_num >= threshold:
                files_to_rename.append((filename, current_num, match.group(2)))

    # 2. Sort files in descending order by the number to prevent overwriting
    files_to_rename.sort(key=lambda x: x[1], reverse=True)

    if not files_to_rename:
        print("No files found that match the criteria.")
        return

    # 3. Rename the files
    print("--- Starting File Rename ---")
    for original_name, current_num, rest_of_name in files_to_rename:
        new_num = current_num + 1
        new_name = f"{prefix}_{new_num}_{rest_of_name}"

        old_path = os.path.join(directory, original_name)
        new_path = os.path.join(directory, new_name)

        print(f"Renaming: {original_name} -> {new_name}")

        # Uncomment the line below to actually perform the rename operation
        os.rename(old_path, new_path)

    print("--- Finished ---")
    print("NOTE: This was a dry run. Uncomment 'os.rename(old_path, new_path)' to apply changes.")


# Run the function in the current directory
if __name__ == "__main__":
    # Change "." to your folder path if the script is not in the same directory as the images
    bump_file_numbers(directory=".", prefix="4", threshold=9)