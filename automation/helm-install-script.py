import subprocess  # Import subprocess module to run external commands
import sys  # Import sys module for system-specific parameters and functions

def install_resources(chart_dir, release_name):
    """
    Install Helm resources using 'helm install' command.

    Args:
    chart_dir (str): Directory path of the Helm chart.
    release_name (str): Name for the release.

    Returns:
    None
    """
    subprocess.run(
        ["helm", "install", release_name, chart_dir],  # Execute 'helm install' command with specified arguments
        check=True,  # Ensure command execution is successful, else raise an exception
    )
    print("Helm resources installed successfully.")  # Display success message after installation

def print_usage():
    """
    Print usage instructions if incorrect arguments are passed.

    Returns:
    None
    """
    print(f"Usage: python3 {sys.argv[0]} <chart_directory> <release_name>")  # Display correct usage format
    sys.exit(1)  # Exit with status 1 indicating an error

if len(sys.argv) != 3:  # Check if the number of arguments passed is not equal to 3
    print_usage()  # If the condition is met, display usage instructions and exit the script

# Get command line arguments

specified_chart_dir = sys.argv[1]  # Assign the first argument as the specified_chart_dir
specified_release = sys.argv[2]  # Assign the second argument as the specified_release

install_resources(specified_chart_dir, specified_release)  # Call the install_resources function with specified arguments

