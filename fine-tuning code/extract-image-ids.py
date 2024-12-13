import csv


def extract_image_ids(csv_file, label_name, n):
    image_ids = []
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Loop through each row in the CSV
        for row in reader:
            # Check if the label name in the row matches the specified label name
            if row[2] == label_name:
                image_ids.append(row[0])  # Append only the image ID
                # Stop if we reach the desired number of appearances
                if len(image_ids) == n:
                    break

    return image_ids


# Usage example
csv_file = '/Users/harisz/Desktop/detections.csv'
label_name = '/m/050k8'
n = 15
image_ids = extract_image_ids(csv_file, label_name, n)

# Display the result
print("Extracted Image IDs:", image_ids)

# csv_file = '/Users/harisz/Desktop/detections.csv'
# label_name = '/m/050k8'