import os
import requests
from bs4 import BeautifulSoup

# List of arXiv links
arxiv_links = [
    "https://arxiv.org/abs/2410.11781",
    "https://arxiv.org/abs/2401.03735v3",
    "https://arxiv.org/abs/2410.15580",
    "https://arxiv.org/abs/2305.15054"
]

# Create directories to save the PDF and TeX files
pdf_output_dir = "arxiv_arithm_in_llm"
tex_output_dir = "arxiv_arithm_in_llmsources"
os.makedirs(pdf_output_dir, exist_ok=True)
os.makedirs(tex_output_dir, exist_ok=True)

# Download each PDF and TeX source
for i, url in enumerate(arxiv_links, start=1):
    try:
        # Download PDF file
        pdf_url = url.replace("/abs/", "/pdf/")
        pdf_response = requests.get(pdf_url)
        pdf_response.raise_for_status()  # Raise an error for bad responses

        # Save the PDF file
        pdf_file_name = os.path.join(pdf_output_dir, f"paper_{i}.pdf")
        with open(pdf_file_name, "wb") as file:
            file.write(pdf_response.content)
        print(f"Downloaded PDF: {pdf_file_name}")

        # Scrape the webpage to find the TeX source download link
        webpage_response = requests.get(url)
        webpage_response.raise_for_status()

        soup = BeautifulSoup(webpage_response.content, "html.parser")
        tex_link = soup.find("a", string="TeX Source")

        print(tex_link)
        if tex_link:
            tex_url = "https://arxiv.org" + tex_link.get("href")

            # Download the TeX source zip file
            tex_response = requests.get(tex_url)
            tex_response.raise_for_status()

            # Save the TeX zip file
            tex_file_name = os.path.join(tex_output_dir, f"paper_{i}.tar.gz")
            with open(tex_file_name, "wb") as file:
                file.write(tex_response.content)
            print(f"Downloaded TeX source: {tex_file_name}")

    except requests.RequestException as e:
        print(f"Failed to process {url}: {e}")

print("Download completed!")