
from PySSHPass.pysshpass import SSHClientWrapper

def test_ssh_client():
    # Replace with appropriate SSH credentials and commands
    ssh_client = SSHClientWrapper(
        host="172.16.101.1",
        user="cisco",
        password="cisco",
        cmds="term len 0,,show cdp nei det",
        invoke_shell=True,
        prompt="#",
        prompt_count=3,
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
