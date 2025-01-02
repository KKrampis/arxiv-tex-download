import os
import requests

# List of arXiv links
arxiv_links = [
    "https://arxiv.org/pdf/1902.10186",
    "https://arxiv.org/pdf/2005.02670",
    "https://arxiv.org/pdf/2006.11543",
    "https://arxiv.org/pdf/1907.01893",
    "https://arxiv.org/pdf/2006.11436",
    "https://arxiv.org/pdf/1904.05656",
    "https://arxiv.org/pdf/2006.11111",
    "https://arxiv.org/pdf/2007.03283",
    "https://arxiv.org/pdf/1906.08878",
    "https://arxiv.org/pdf/2007.03184",
    "https://arxiv.org/pdf/2006.11541",
    "https://arxiv.org/pdf/1907.01623",
    "https://arxiv.org/pdf/2006.11540",
    "https://arxiv.org/pdf/1907.01892",
    "https://arxiv.org/pdf/2006.11542",
    "https://arxiv.org/pdf/2007.03185",
    "https://arxiv.org/pdf/1906.08877",
    "https://arxiv.org/pdf/2007.03282",
    "https://arxiv.org/pdf/2006.11544",
    "https://arxiv.org/pdf/2005.02671"
]

# Create a directory to save the downloaded PDFs
output_dir = "arxiv_papers"
os.makedirs(output_dir, exist_ok=True)

# Download each PDF
for i, url in enumerate(arxiv_links, start=1):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Save the PDF file
        file_name = os.path.join(output_dir, f"paper_{i}a.pdf")
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

print("Download completed!")