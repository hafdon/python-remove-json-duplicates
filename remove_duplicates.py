import json
from collections import defaultdict
import sys

def remove_duplicate_pronunciations(pronunciations):
    """
    Remove duplicate pronunciations for each word while preserving order.
    """
    cleaned_pronunciations = {}
    for word, sounds in pronunciations.items():
        seen = set()
        unique_sounds = []
        for sound in sounds:
            if sound not in seen:
                seen.add(sound)
                unique_sounds.append(sound)
        cleaned_pronunciations[word] = unique_sounds
    return cleaned_pronunciations

def remove_duplicate_failed_words(failed_words_pairs):
    """
    Remove duplicate failed word entries, keeping the last occurrence.
    :param failed_words_pairs: List of (word, details) tuples.
    :return: Dictionary with unique failed words.
    """
    failed_words = {}
    for word, details in failed_words_pairs:
        failed_words[word] = details  # Overwrite duplicates, keeping last
    return failed_words

def process_json(data):
    """
    Process the JSON data to remove duplicates in 'pronunciations' and 'failed_words'.
    """
    cleaned_data = {}

    for key, value in data:
        if key == "pronunciations":
            # 'pronunciations' should be a list of key-value pairs
            pronunciations = {}
            for word, sounds in value:
                if word not in pronunciations:
                    pronunciations[word] = []
                pronunciations[word].extend(sounds)
            # Remove duplicate pronunciations
            pronunciations = remove_duplicate_pronunciations(pronunciations)
            cleaned_data["pronunciations"] = pronunciations

        elif key == "failed_words":
            # 'failed_words' should be a list of key-value pairs
            failed_words = remove_duplicate_failed_words(value)
            cleaned_data["failed_words"] = failed_words

        else:
            # For other keys, assume they are unique and assign directly
            cleaned_data[key] = value

    return cleaned_data

def main(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            # Load JSON with object_pairs_hook to capture duplicate keys
            data = json.load(f, object_pairs_hook=lambda pairs: pairs)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        sys.exit(1)

    # Process the data to remove duplicates
    cleaned_data = process_json(data)

    # Write the cleaned data to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

    print(f"Cleaned data has been saved to '{output_file}'.")

if __name__ == "__main__":
    # Example usage: python remove_duplicates.py data.json cleaned_data.json
    if len(sys.argv) != 3:
        print("Usage: python remove_duplicates.py <input_json_file> <output_json_file>")
        sys.exit(1)
    
    input_json_file = sys.argv[1]
    output_json_file = sys.argv[2]
    
    main(input_json_file, output_json_file)
import json
from collections import defaultdict
import sys

def remove_duplicate_pronunciations(pronunciations):
    """
    Remove duplicate pronunciations for each word while preserving order.
    """
    cleaned_pronunciations = {}
    for word, sounds in pronunciations.items():
        seen = set()
        unique_sounds = []
        for sound in sounds:
            if sound not in seen:
                seen.add(sound)
                unique_sounds.append(sound)
        cleaned_pronunciations[word] = unique_sounds
    return cleaned_pronunciations

def remove_duplicate_failed_words(failed_words_pairs):
    """
    Remove duplicate failed word entries, keeping the last occurrence.
    Convert details from list of pairs to dictionary.
    
    :param failed_words_pairs: List of (word, details) tuples.
    :return: Dictionary with unique failed words and their details as dicts.
    """
    failed_words = {}
    for word, details in failed_words_pairs:
        # Convert details from list of pairs to dictionary
        details_dict = dict(details)
        failed_words[word] = details_dict  # Overwrite duplicates, keeping last
    return failed_words

def process_json(data):
    """
    Process the JSON data to remove duplicates in 'pronunciations' and 'failed_words'.
    """
    cleaned_data = {}

    for key, value in data:
        if key == "pronunciations":
            # 'pronunciations' is a list of (word, sounds) tuples
            pronunciations = {}
            for word, sounds in value:
                if word not in pronunciations:
                    pronunciations[word] = []
                pronunciations[word].extend(sounds)
            # Remove duplicate pronunciations
            pronunciations = remove_duplicate_pronunciations(pronunciations)
            cleaned_data["pronunciations"] = pronunciations

        elif key == "failed_words":
            # 'failed_words' is a list of (word, details) tuples
            failed_words = remove_duplicate_failed_words(value)
            cleaned_data["failed_words"] = failed_words

        else:
            # For other keys, assume they are unique and assign directly
            cleaned_data[key] = value

    return cleaned_data

def main(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            # Load JSON with object_pairs_hook to capture duplicate keys
            data = json.load(f, object_pairs_hook=lambda pairs: pairs)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        sys.exit(1)

    # Process the data to remove duplicates
    cleaned_data = process_json(data)

    # Write the cleaned data to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

    print(f"Cleaned data has been saved to '{output_file}'.")

if __name__ == "__main__":
    # Example usage: python remove_duplicates.py data.json cleaned_data.json
    if len(sys.argv) != 3:
        print("Usage: python remove_duplicates.py <input_json_file> <output_json_file>")
        sys.exit(1)
    
    input_json_file = sys.argv[1]
    output_json_file = sys.argv[2]
    
    main(input_json_file, output_json_file)
