import arxiv

def download_arxiv_papers(query, max_results):
    try:
        # Search for papers on arXiv
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
        )

        # Display paper metadata and prompt user for download confirmation
        for result in search.results():
            print(f"Title: {result.title}")
            print(f"Authors: {', '.join([author.name for author in result.authors])}")
            print(f"Published: {result.published}")
            print(f"Abstract: {result.summary}\n")

            # Ask user for confirmation to download the PDF
            response = input("Download this paper? (y/n): ")
            if response.lower() == "y":
                # Construct the PDF filename
                pdf_filename = f"{result.entry_id.split('/')[-1]}.pdf"

                # Check if the file already exists to prevent unnecessary downloads
                import os
                dirpath = "./pdf-downloads"
                filepath = os.path.join(dirpath, pdf_filename)
                if not os.path.exists(filepath):
                    print(f"Downloading: {pdf_filename}")
                    result.download_pdf(dirpath=dirpath, filename=pdf_filename)
                    print("Downloaded successfully!\n")
                else:
                    print(f"{pdf_filename} already exists. Skipping download...\n")
            elif response.lower() == "n":
                print("Skipping this paper...\n")
            else:
                print("Invalid input. Please enter 'y' or 'n'.\n")

    except Exception as e:
        print(f"An error occurred: {e}")

# Define your search query and parameters
query = "explainable AI XAI for LLM attention transformers"  # Replace with your search topic
max_results = 10  # Limit the number of results to download

download_arxiv_papers(query, max_results)
