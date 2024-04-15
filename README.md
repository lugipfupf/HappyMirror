# How to run
## Development mode
Get all you need by typing `pip install -e .`, then run the application directly from VSCode.

## Production mode
Make sure, waitress is installed. On Linux, you can do so by typing `sudo apt install python3-waitress`
Then run `waitress-serve --call 'HappyMirror:create_app'`
