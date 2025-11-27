import os

# Base directory (project root)
BASE = "content"

# Documentation structure
structure = {
    "introduction": {
        "_index.md": ("Introduction", 1, "Welcome to the SHM documentation."),
        "what-is-shm.md": ("What is SHM?", 1, "Basics of Structural Health Monitoring."),
        "project-overview.md": ("Project Overview", 2, "Overview of the SHM–Mongo–DuckDB project.")
    },
    "setup": {
        "_index.md": ("Setup", 2, "System setup for Ubuntu and Windows."),
        "windows.md": ("Windows Setup", 1, "Instructions for Windows environment."),
        "ubuntu.md": ("Ubuntu Setup", 2, "Instructions for Ubuntu environment."),
        "tools.md": ("Tools Needed", 3, "Required software tools.")
    },
    "mongodb": {
        "_index.md": ("MongoDB", 3, "Working with MongoDB data."),
        "export.md": ("Exporting Data", 1, "How to export data from MongoDB."),
        "query.md": ("Querying Data", 2, "Query examples and basics.")
    },
    "duckdb": {
        "_index.md": ("DuckDB", 4, "Working with DuckDB and Parquet."),
        "convert.md": ("Convert to Parquet", 1, "Converting Mongo JSON/BSON to Parquet."),
        "query-parquet.md": ("Query Parquet", 2, "Querying Parquet files with DuckDB.")
    },
    "datasets": {
        "_index.md": ("Datasets", 5, "Dataset structure and download info."),
        "structure.md": ("Dataset Structure", 1, "Overview of monthly dataset contents."),
        "monthly-overview.md": ("Monthly Overview", 2, "How data changes month-to-month.")
    },
    "examples": {
        "_index.md": ("Examples", 6, "Examples of analysis and visualizations."),
        "spectrograms.md": ("Spectrograms", 1, "Plotting spectrograms from signals."),
        "vibration-analysis.md": ("Vibration Analysis", 2, "Basic vibration analysis workflow.")
    }
}

def write_md(path, title, weight, body):
    """Write TOML front-matter + body into file."""
    with open(path, "w") as f:
        f.write(f"""+++
title = "{title}"
weight = {weight}
+++

{body}
""")

def main():
    for section, files in structure.items():
        section_dir = os.path.join(BASE, section)
        os.makedirs(section_dir, exist_ok=True)

        for filename, (title, weight, body) in files.items():
            path = os.path.join(section_dir, filename)
            write_md(path, title, weight, body)

    print("\n🎉 All documentation pages created successfully!\n")

if __name__ == "__main__":
    main()
