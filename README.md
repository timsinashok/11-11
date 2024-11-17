# 11-11 Camera App

## Disclaimer

**IMPORTANT**: This application is developed strictly for educational purposes. Any use of this software for illegal activities is strictly prohibited. Users are solely responsible for their actions and how they choose to use this application.

## Overview

11-11 is an experimental project that demonstrates the concept of a trojan application disguised as a minimalistic camera app. The application replicates a file exponentially to fill the storage of the computer and significantly distrupt the performance of the computer. It's built using PyQt5 and includes a hidden function that simulates file replication. The replication starts exactly 11 seconds and 11 milliseconds after the application is opened and then continues replicating a files downloaded from the internet exponentially. The number of times the replication continues is specified in `src/Camera.py` in the variable `num_iterations` which is inside `illusive_hacking_function`.

### Key Features

- Running this program outputs a normal app called `Camera` which works as a camera
- Hidden `illusive_hacking_function` for educational demonstration of trojan
- Built with PyQt5 for cross-platform compatibility

## Technical Details

The application includes a function called `illusive_hacking_function` which, when activated, downloads a file from a predefined internet source and replicates it. This feature is intended to demonstrate potential security vulnerabilities and should be used only in controlled, educational environments.

## Dependencies

- Python 3.x
- NumPy
- PyQt5
- OpenCV

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/11-11-camera-app.git
   cd 11-11
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

For educational purposes, you can modify the behavior of the `illusive_hacking_function`:

1. Open `main.py` in a text editor.
2. Locate the `illusive_hacking_function` method.
3. Adjust the `num_iterations` parameter to change the replication behavior.

    **Note**: Increasing the value of `num_iterations` to a large value will increase the number of times the downloaded file will be replicated exponentially. Setting this value to large value will significantly impact the performance and storage of the computer.

4. This app uses this [link](https://jollycontrarian.com/images/6/6c/Rickroll.jpg?20170403162336) which is an image of Rick Astley from the song Never gonna give you up. The application downloads the image and then replicates exponentially. 

    The size of the image is only 36 KB. Consider updating the link in the function `illusive_hacking_function` by updating the variable `file_link` with a link to file which is much larger then 36kb. This will download a larger file and replicate a large file which will significantly disrupt the performance of host's computer and quickly fill the space in the computer. 

## Building the Application

To build the standalone application:

```
pyinstaller Camera.spec
```

The built application will be available in the `dist` directory.

## Usage

Run the application by executing the built file in the `dist` directory. The camera interface should appear, allowing basic camera functionality.

## Educational Purpose

This project is designed to demonstrate:
- How seemingly benign applications can contain hidden functionalities
- The importance of code review and security in software development
- Potential risks of running untrusted software

## Contributing

Contributions for educational enhancements are welcome. Please open an issue first to discuss proposed changes.

## License

GNU GENERAL PUBLIC LICENSE

## Disclaimer

The creators and contributors of this project are not responsible for any misuse or damage caused by this software. It is provided as-is for educational purposes only.
