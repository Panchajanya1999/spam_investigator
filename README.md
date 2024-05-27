# Spam Investigator

This project is a Spam Investigator that uses a machine learning model to classify messages from users in a Telegram groups as spam or not spam. The project is built using Python and the Flask web framework.

## Prerequisites

Before you begin, ensure you have the following software installed on your local machine:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository or download the ZIP file and extract it.

2. Navigate to the project directory:

    ```bash
    cd path/to/project
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure that your environment variables are set. You can copy the sample.env to a .env file and edit it as needed:

    ```bash
    cp sample.env .env
    ```

2. Build and start the Docker container:

    ```bash
    docker-compose up --build
    ```

3. Once started, you can stop the container with:

    ```bash
    docker-compose down
    ```

## File Structure

- `README.md`: This file.
- `requirements.txt`: Lists the Python packages required for the project.
- `sample.env`: A sample environment variables file.
- `run.py`: The script that runs `flask_spam_class.py` and `tg.py`.
- `flask_spam_class.py`: The Flask application script.
- `tg.py`: The second script to be executed.
- `dataset`: Directory containing any datasets used by the project.

## License

This project is licensed under the MIT License. See the [MIT](https://opensource.org/license/mit) file for details.

## Contributing

If you wish to contribute to this project, please create a pull request or submit an issue.

## Acknowledgements

- LOREM IPSUM

## Contact

For any questions or concerns, please contact:

- Panchajanya1999: [kernel@panchajanya.dev](mailto:kernel@panchajanya.dev)
