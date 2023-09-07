Project Delivery Automator
This is a Python project designed to automate various tasks related to file handling, string searching, and email notifications. It serves as a generic solution but has been configured to achieve specific objectives:

Project Structure
The project's directory structure is organized as follows:


project_delivery_automator/
│
├── file_utilities/
│   ├── __init__.py
│   ├── file_lister.py
│   ├── unzipper.py
│   ├── searcher.py
│   ├── email_sender.py
│   ├── oracle_table_manager.py
│   └── cleanup.py
│
├── main.py
├── config.properties
├── cron_script.sh
├── docker-compose.yml
├── Dockerfile
├── README.md
└── output/
file_utilities/: Contains modules for file handling, decompression, string searching, email sending, Oracle database interaction, and cleanup.

output/: This directory is used to store decompressed files.

main.py: The main entry point of the project, responsible for file operations and searching.

config.properties: Configuration parameters for the project.

oracle_table_manager.py: Handles interactions with an Oracle database, including table and file existence checks, inserting processed values, and connection management.

cron_script.sh: This Bash script sets up environment variables for an Oracle Instant Client, navigates to the project directory in /app, and executes the main.py Python script while logging the output to /var/log/cron.log.

docker-compose.yml: A Docker Compose configuration file defining a service named "project-delivery-automator-service," which specifies the Docker image, port mappings, and restart policies.

Dockerfile: The Dockerfile responsible for building a Python container, installing dependencies, configuring the timezone, downloading the Oracle Instant Client, setting up a cron task, and running the cron service in the background.

README.md: This file, which provides detailed information about the project, including its structure, functionality, usage, and Docker-related instructions.

Functionality
The project includes several utility modules:

file_lister.py: Lists files in a web directory based on specific extensions and prefixes.

unzipper.py: Handles the decompression of ZIP files into a designated directory.

searcher.py: Searches for a specified string within the content of files.

email_sender.py: Sends email notifications to predefined recipients.

cleanup.py: Manages the deletion of decompressed and temporary files.

How to Run
To use this project:

Configure the URLs, folders, and search strings in the relevant configuration files to match your requirements.

Execute the main.py script using python main.py.


Creator: Juan Del Río Gómez

Creation Date: August 2023

