#!/bin/bash

PROJECT_DIR="./PlatformIO"

# Function to check if PlatformIO is installed
check_platformio() {
    command -v platformio > /dev/null 2>&1 || { 
        echo >&2 "PlatformIO is not installed. Please install it first."; 
        exit 1; 
    }
}

# Function to upload the project to the connected MCU
upload_project() {
    cd "$PROJECT_DIR" || exit
    echo "Uploading project to the connected MCU..."
    platformio run --target upload
    cd - || exit
}

# Main script
check_platformio
upload_project

echo "Upload process completed."
