
simple1 = """
from PySSHPass.pysshpass import SSHClientWrapper

def test_ssh_client():
    # Replace with appropriate SSH credentials and commands
    ssh_client = SSHClientWrapper(
        host="{{ host }}",
        user="{{ user }}",
        password="{{ password }}",
        cmds="{{ cmds }}",
        invoke_shell=True,
        prompt="{{ prompt }}",
        prompt_count={{ prompt_count }},
        timeout=15,
        delay=0.5
    )

    ssh_client.connect()

    # Run the commands and capture the output
    output = ssh_client.run_commands()
    print(output)

    # Close the connection
    ssh_client.close()

if __name__ == "__main__":
    test_ssh_client()
"""
