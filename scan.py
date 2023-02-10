import wmi


def scan_wifi():
    # Connect to the WMI service
    c = wmi.WMI()

    # Query the WMI service for available wireless networks
    networks = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # Loop over the list of networks and print out the relevant information
    for network in networks:
        if network.MACAddress is not None:
            print("Description: {}\nGUID: {}\n".format(network.Description, network.SettingID))


if __name__ == "__main__":
    scan_wifi()
