import arxiv

# Define your search query and parameters
query = "attention and transformers explained"  # Replace with your search topic
max_results = 10  # Limit the number of results to download

# Search for papers on arXiv
search = arxiv.Search(
    query=query,
    max_results=max_results,
    sort_by=arxiv.SortCriterion.SubmittedDate,
)

# Download PDFs and save metadata
for result in search.results():
    print(f"Title: {result.title}")
    print(f"Authors: {', '.join([author.name for author in result.authors])}")
    print(f"Published: {result.published}")
    print(f"PDF URL: {result.pdf_url}")
    
    # Download the PDF
    pdf_filename = f"{result.entry_id.split('/')[-1]}.pdf"
    print(f"Downloading: {pdf_filename}")
    result.download_pdf(dirpath="./pdf-downloads", filename=pdf_filename)
    print("Downloaded successfully!\n")